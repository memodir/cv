# CV development and deployment guideline 

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/fd24ee6f1fae4927ae7530dbe4578eb3)](https://app.codacy.com/app/seawaywen/cv?utm_source=github.com&utm_medium=referral&utm_content=memodir/cv&utm_campaign=Badge_Grade_Settings)


## Dev on Mac OSX
#### 1. pre-install packages

Install the postgresql client  

    $ brew install postgresql

Check the postgresql service is down:  

    $ brew services list 
 
    Name           Status  User Plist  
    postgresql     stopped

Install the node v10.x

    $ brew install node 

Install the yarn  

    $ brew install yarn  


#### 2. bootstrap

Go to the project-root-folder and run:

    $ make bootstrap

This will setup the virtualenv and install all the python dependencies


then go the project-root-folder/static_src and run:
    
    $ yarn
    $ yarn dev 

#### 3. database
    $ make setup-db

this command will pull the postgres docker image and create a docker container, all the db data will store under 
~/Desktop folder by default

    $ make start-db
    
#### 4. run the dev server and start your development
    $ make run
    
    
    

## Dev with Docker
#### Use the docker build && start service
    $ docker-compose up [--build]

### some useful docker commands
#### 1. attach to one container to debug 
    $ docker container exec -it cv_web_1 bash

#### 2. removed all the dangling images
    $ docker rmi `docker images -q -f dangling=true`




## Deploy with Kubernetes  
#### database setup
    1. Persistent volume with file type
    $ kubectl apply -f kubernetes/db/persistent-volume-file.yaml
    
    2. Deploy the postgresql database
    $ kubectl apply -f kubernetes/db/deploy.yaml


#### deploy app and nginx 
    1. django application deployement
    $ kubectl apply -f kubernetes/app/app-deploy.yaml
    
    2. nginx deployment
    $ kubectl apply -f kubernetes/app/nginx-deploy.yaml
    
    3. service setup
    $ kubectl apply -f kubernetes/app/service.yaml

#### monitor commands
    $ kubectl get pod --watch  
    
    $ kubectl get deployment --watch  
    
    $ kubectl get service --watch  
    
    $ kubectl logs deployement-instant-id -f



## Testing
#### Use the coverage to check the code(testcase) coverage
    $ make coverage ARGS='src'

    $ make coverage-report-html  

Then you can find the generated coverage HTML version report under ROOT/htmlcov/



## Dockerized Postgres db management 
#### pull a postgres docker 
    $ docker pull postgres

#### start a postgres docker
    $ docker run -i -t -p 5432:5432 postgres

#### attach a shell to the docker instance
    $ docker exec -it inst-name /bin/bash

#### connect to the dock postgres via psql
    $ psql -h localhost -p 5432 -U postgres


## DB operation
#### init database with all migrations applied
    $ make setup-db

#### stop database (keep the data)
    $ make stop-db

#### start database
    $ make start-db

#### terminate the database
    $ make destroy-db

#### create a super user
    $ make createsuperuser


## FrontEnd
#### Install and manage the Node
Use nvm to manage the different node version  

Install the long term support version node:  

    $ nvm install node --lts

Display all installed node version  

    $ nvm list  

Use the specfic version  

    $ nvm use v10.3.0


#### Install the required packages
    $ yarn

#### Use the webpack to build the asset
    $ yarn run build  

if you need the build automatically with the file changes  

    $ yarn run watch

A task is defined to run the build with the running server

    $ yarn dev  

Production build   

    $ yarn prod-build  

# work version: "vue-loader": "^14.2.2",
"extract-text-webpack-plugin": "^4.0.0-beta.0",

