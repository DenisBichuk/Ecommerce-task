# Ecom test task
------------


The service is created as the test task for ECOM.

# Installation and local deploy
Follow these simple steps to local deploy.
* Clone the repo:
```
git clone git@github.com:DmitriyMikhalev/ecom-test-task.git
```
* Run Docker app and docker-compose:
```
docker-compose up -d
```

* App is available. Follow the link to see docs
```
http://127.0.0.1:8000/swagger/
```


# Most used API endpoints for authentication 

------------


# Users
## Registration
```
POST http://127.0.0.1:8000/api/auth/users/

{
    "email": "email@google.com",
    "password": "paswzdf"
}
```
## Get authorization token
```
POST http://127.0.0.1:8000/api/auth/jwt/create/

{
    "email": "email@google.com",
    "password": "paswzdf"
}
```
## Get current user info
```
GET http://127.0.0.1:8000/api/auth/users/me/
```