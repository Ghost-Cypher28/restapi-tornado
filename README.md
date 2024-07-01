# Tornado API RESTful - Python

## English

This is a example, to implements a http web server (API RESTfull) in python with tornado framework, mongo, redis and docker..


### Routes

* GET - `/api/v1/users` - Get all users
* GET - `/api/v1/users/{user_id}` - Get only the user for the id entered in the parameter
* POST - `/api/v1/user` - Create new user
* PUT - `/api/v1/users/{user_id}` - Edit the user referring to the id entered in the parameter
* DELETE - `/api/v1/users/{user_id}` - Delete the user referring to the id entered in the parameter

### Architecture

* **Handlers** - It is the layer responsible for manipulating requests and performing business rules.

* **Persistence** - Layer responsible for data manipulation.

    * **Schemas** - Data modeling.
    
    * **Database** - Connection and manipulation with database.
    
* **Tests** - Layer with unit application tests

* **Util** - Gathers higher-use (repetitive) codes in the project.


### Tests
Run all unit application tests
* `cd project-folder`
* `python -m unittest`

### Run
After preparing your environment and your virtualenv, follow the steps:

* `cd project-folder`
* `pip install -r requirements.txt`
*  set the environment variables (examples in file: .env.example) on your machine, or manually change the settings.py file.
* `python server.py`

Run application with docker:
* `cd project-folder`
* `docker build -t api-tornado-img .`
*  set the environment variables in the following command and run it.
* `docker run -d -p 8080:8080 --name api-tornado -e MONGO_URI="mongodb://user:password@host:port/database" -e REDIS_HOST="127.0.0.1" -e REDIS_PORT=6379 -e REDIS_PASS="your-redis-pass" api-tornado-img:latest`
* your application is running in 8080 port

##
