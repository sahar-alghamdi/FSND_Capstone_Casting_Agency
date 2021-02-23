# Full Stack Capstone Casting Agency API 

## Casting Agency

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies.

## Motivation for project

This project is implemented as a graduation requirement for FSND Program. It aims to practice all the knowledge we acquired from this program, includes:

- Coding in Python 3
- Relational Database Architecture
- Modeling Data Objects with SQLAlchemy
- Internet Protocols and Communication
- Developing a Flask API
- Authentication and Access
- Authentication with Auth0
- Authentication in Flask
- Role-Based Access Control (RBAC)
- Testing Flask Applications
- Deploying Applications

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/starter` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

## Database Setup
With Postgres running, create a database. In terminal run:

```bash
createdb casting_agency
```
## Running the server

From within the `starter` directory first ensure you are working using your created virtual environment.

Export the environment variables in the file `setup.sh`

To run the server, execute:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

## Testing
To run the tests, run
```bash
dropdb casting_agency
createdb casting_agency
python test_app.py
```

## Running Migrations
To run the local migrations using `manage.py` file
```bash
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

## API Reference

### Getting Started
- Base URL: this  API is hosted live via Heroku at, https://capstone-casting-agency-2.herokuapp.com/
- Authentication: 
    - This app required a valid authentication token. A token can be acquired through this [link](https://auth-sahar.us.auth0.com/authorize?audience=casting_agency&response_type=token&client_id=fMfsNx0VutgBsV8JWuYiDHIdKAYQ5X46&redirect_uri=https://127.0.0.1:8080/login-results)
    - Valid tokens for all the roles are provided in setup.sh file
    - Roles:
        - Casting Assistant: Can view actors and movies. (email: assistant@test.com, Password: Test@123)
        - Casting Director: All permissions a Casting Assistant has and Add or delete an actor from the database. Modify actors or movies. (email: director@test.com, Password: Test@123)
        - Executive Producer: All permissions a Casting Director has and add or delete a movie from the database. (email: executive@test.com, Password: Test@123)
    - Postman collection `Capstone_casting_agency` can be found in this repository that tests all endpoints.

### Error Handling 
Errors are returned as JSON objects in the following format
```
{
    "success": False,
    "error": 404,
    "message": "resource not found"
}
```
The API will return four error types when requests fail:

- 400: Bad Request
- 404: Resource Not Found
- 405: Method Not Allowed
- 422: Not Processable
- 401: Unauthorized

### Endpoints

#### Get /movies

- General
    - Returns a list of movies objects, success value.
- Sample: ```curl --location --request GET 'https://capstone-casting-agency-2.herokuapp.com/movies'  --header 'Authorization: Bearer JWT_token'```
```
{
    "movies": [
        {
            "id": 1,
            "release_date": "Sun, 19 Oct 2008 00:00:00 GMT",
            "title": "Into The Wild"
        }
    ],
    "success": true
}
```


#### Get /actors

- General
    - Returns a list of movies objects, success value.
- Sample: ```curl --location --request GET 'https://capstone-casting-agency-2.herokuapp.com/actors'  --header 'Authorization: Bearer JWT_token'```
```
{
    "actors": [
        {
            "age": 35,
            "gender": "male",
            "id": 1,
            "name": "Emile Hirsch"
        }
    ],
    "success": true
}
```

#### Post /movies

- General
    - Creates a new movie. Returns the created movie object and success value.
- Sample: ```curl --location --request POST 'https://capstone-casting-agency-2.herokuapp.com/moviess'  --header 'Authorization: Bearer JWT_token' --data-raw '{"title": "Into The Wild","release_date": "10-19-2007"}'```
```
{
    "movie": {
        "id": 1,
        "release_date": "Fri, 19 Oct 2007 00:00:00 GMT",
        "title": "Into The Wild"
    },
    "success": true
}
```

#### Post /actors

- General
    - Creates a new actor. Returns the created actor object and success value.
- Sample: ```curl --location --request POST 'https://capstone-casting-agency-2.herokuapp.com/actors'  --header 'Authorization: Bearer JWT_token' --data-raw '{"name": "Emile Hirsch", "age": 35,"gender": "male"}'```
```
{
    "actor": {
        "age": 35,
        "gender": "male",
        "id": 1,
        "name": "Emile Hirsch"
    },
    "success": true
}
```

#### Patch /movies/{movie_id}

- General
    - Modify an existed movie. Returns the modified movie object and success value.
- Sample: ```curl --location --request PATCH 'https://capstone-casting-agency-2.herokuapp.com/movies/1'  --header 'Authorization: Bearer JWT_token' --data-raw '{"title": "Into The Wild","release_date": "10-19-2007"}'```
```
{
    "movie": {
        "id": 1,
        "release_date": "Sun, 19 Oct 2008 00:00:00 GMT",
        "title": "Into The Wild 2"
    },
    "success": true
}
```

#### Patch /actors/{actor_id}

- General
    - Modify an existed actor. Returns the modified actor object and success value.
- Sample: ```curl --location --request POST 'https://capstone-casting-agency-2.herokuapp.com/actors'  --header 'Authorization: Bearer JWT_token' --data-raw '{"name": "Emile Hirsch", "age": 35,"gender": "male"}'```
```
{
    "actor": {
        "age": 35,
        "gender": "male",
        "id": 1,
        "name": "Emile Hirsch"
    },
    "success": true
}
```

#### Delete /movies/{movie_id}

- General:
    - Deletes the movie of the given ID if it exists. Returns the id of the deleted movie and success value.
- Sample: ```curl --location --request DELETE 'https://capstone-casting-agency-2.herokuapp.com//movies/1' --header 'Authorization: Bearer JWT_token'```
```
{
    "delete": "1",
    "success": true
}
```

#### Delete /actors/{actor_id}

- General:
    - Deletes the actor of the given ID if it exists. Returns the id of the deleted actor and success value.
- Sample: ```curl --location --request DELETE 'https://capstone-casting-agency-2.herokuapp.com//actors/1' --header 'Authorization: Bearer JWT_token'```
```
{
    "delete": "1",
    "success": true
}
```