/*
 * Copyright (c) 2017, NVIDIA CORPORATION. All rights reserved.
 *
 */
package dfc

import (
	"crypto/md5"
	"encoding/hex"
	"errors"
	"fmt"
	"io"
	"net/http"
	"os"
	"strconv"

	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/s3"
	"github.com/aws/aws-sdk-go/service/s3/s3manager"
	"github.com/golang/glog"
)

func createsession() *session.Session {
	// TODO: avoid creating sessions for each request
	return session.Must(session.NewSessionWithOptions(session.Options{
		SharedConfigState: session.SharedConfigEnable}))

}

func (obj *awsif) listbucket(w http.ResponseWriter, bucket string) error {
	glog.Infof("listbucket : bucket = %s ", bucket)
	sess := createsession()
	svc := s3.New(sess)
	params := &s3.ListObjectsInput{Bucket: aws.String(bucket)}
	resp, err := svc.ListObjects(params)
	if err != nil {
		return webinterror(w, err.Error())
	}
	// TODO: reimplement in JSON
	for _, key := range resp.Contents {
		glog.Infof("bucket = %s key = %s", bucket, *key.Key)
		keystr := fmt.Sprintf("%s", *key.Key)
		fmt.Fprintln(w, keystr)
	}
	return nil
}

// This function download S3 object into local file.
func (cobj *awsif) getobj(w http.ResponseWriter, fqn string, bucket string,
	objname string) (file *os.File, err error) {

	var bytes int64
	file, err = initobj(fqn)
	if err != nil {
		glog.Errorf("Failed to initialize file %s, err: %v", fqn, err)
		return nil, err
	}
	sess := createsession()
	s3Svc := s3.New(sess)

	obj, err := s3Svc.GetObject(&s3.GetObjectInput{
		Bucket: aws.String(bucket),
		Key:    aws.String(objname),
	})
	defer obj.Body.Close()
	if err != nil {
		glog.Errorf("Failed to download key %s from bucket %s, err: %v", objname, bucket, err)
		file.Close()
		return nil, err
	}
	// Get ETag from object header
	omd5, _ := strconv.Unquote(*obj.ETag)

	hash := md5.New()
	writer := io.MultiWriter(file, hash)
	_, err = io.Copy(writer, obj.Body)
	if err != nil {
		glog.Errorf("Failed to copy obj err: %v", err)
		checksetmounterror(fqn)
		file.Close()
		return nil, err

	}
	hashInBytes := hash.Sum(nil)[:16]
	fmd5 := hex.EncodeToString(hashInBytes)
	if omd5 != fmd5 {
		errstr := fmt.Sprintf("Object's %s MD5sum %v does not match with file(%s)'s MD5sum %v",
			objname, omd5, fqn, fmd5)
		glog.Error(errstr)
		err := os.Remove(fqn)
		if err != nil {
			glog.Errorf("Failed to delete file %s, err: %v", fqn, err)
		}
		file.Close()
		return nil, errors.New(errstr)
	} else {
		glog.Infof("Object's %s MD5sum %v does MATCH with file(%s)'s MD5sum %v",
			objname, omd5, fqn, fmd5)
	}
	glog.Infof("Downloaded bucket %s key %s file %s", bucket, objname, fqn)
	err = finalizeobj(fqn, hashInBytes)
	if err != nil {
		glog.Errorf("Unable to finalize file %s, err: %v", fqn, err)
		file.Close()
		return nil, err
	}
	stats := getstorstats()
	stats.add("bytesloaded", bytes)
	return file, nil
}

func (cobj *awsif) putobj(r *http.Request, w http.ResponseWriter,
	bucket string, objname string) error {
	sess := createsession()
	// Create an uploader with the session and default options
	uploader := s3manager.NewUploader(sess)
	// Upload the file to S3.
	_, err := uploader.Upload(&s3manager.UploadInput{

		Bucket: aws.String(bucket),
		Key:    aws.String(objname),
		Body:   r.Body,
	})
	if err != nil {
		glog.Errorf("Failed to put key %s into bucket %s, err: %v", objname, bucket, err)
		return webinterror(w, err.Error())
	} else {
		glog.Infof("Uploaded key %s into bucket %s", objname, bucket)
	}
	//TODO stats
	return nil
}