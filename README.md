# Taghive DevOps Homework Assignment

## Goal

This repo includes a very simple application which we want to dockerize and secure.  Security standards should be taken from the [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/index.html) and should pertain to Docker image security only.

## Prerequisites

To run the task on the local machine below are required

- Install Docker on the machine with version 20.10.17 so that image scanner also avialable for security scan
- Install Task on the machine to execute the tasks which are defined under Taskfile.yml
- Install Minikube with kubectl on the machine to deploy the services into local cluster 

## setup

To deploy the services into Local cluster, below are the files created with required changes

- Created Dockerfile for each service , used multilayer image to seperate build and deployment
- Created python virtual environment to setup dependencies as per the owsap best practices
- Created non root user and executed the application with that user as per the owsap best practices
- Created wsgi.py for each service and used gunicorn http server in Dockerfile as per the owsap best practices
- Created deployment manifest files for each service to deploy the services into local cluster 
- Created Taskfile.ym with tasks to execute build, scan , deploy in one go
- Updated app-b service code to create database with table and rows which are mentioned in schema.sql
- Updated app-a service code the, result from app_b getting in bytes datatype, it is failing in comparison so converted byte to string

## Testing:

## Build and Deploy Setup:

- Create seperate branches for each enviornment like develop-dev-env, release-qa-env, etc..
- Enable webhook on the repo , so that when ever changes are pushed to particular branch corresponding job will be triggered
- in the build process, add the steps 
- pull the latest code
- run the unit test cases, if any test cases are failed fail the job and send email communication to the team
- run the security scan of the images , fail the job if any vunerbilities are found and sned email communication to the team
- tag the image and store the image in to registry if above validations are passed
- in the deployment process
- connect to the cluster and deploy the mainfest files to cluster
- mainfest file should contain deployment and service objects 
- add all the stages in the pipeline of jenkins and create job with the pipeline

## secure applicatoin

- Restrict API service access by integrating with LDAP 
- Use RBAC and create Roles and Rolebinding on cluster object level to limit the access of objects for users
- Expose frontend services only and restrict backend services expose outside by using clusterip 



## Getting Started in Local Development

Please create and source your virtualenv before beginning. 

Running the apps locally:

```bash
task run-app
```

Making a request

```bash
curl http://127.0.0.1:5000/hello

curl -X POST -H 'Authorization: mytoken' http://127.0.0.1:5000/jobs
```

Simulating a lot of requests

```bash
ab -m POST -H "Authorization: mytoken" -n 500 -c 4 http://127.0.0.1:5000/jobs
```
