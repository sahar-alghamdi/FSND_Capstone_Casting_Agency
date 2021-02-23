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
- Base URL: this app is hosted as a base URL. The backend app is hosted at, http://127.0.0.1:5000/
- Authentication: 
    - This app required a valid authentication token. A token can be acquired through this [link](https://auth-sahar.us.auth0.com/authorize?audience=casting_agency&response_type=token&client_id=fMfsNx0VutgBsV8JWuYiDHIdKAYQ5X46&redirect_uri=https://127.0.0.1:8080/login-results)
    - Valid tokens for all the roles are provided in setup.sh file
    - Roles:
        - Casting Assistant: Can view actors and movies.
        - Casting Director: All permissions a Casting Assistant has and Add or delete an actor from the database. Modify actors or movies.
        - Executive Producer: All permissions a Casting Director has and add or delete a movie from the database.

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

#### Get /actors

#### Post /movies

#### Post /actors

#### Patch /movies/{movie_id}

#### Patch /actors/{actor_id}

#### Delete /movies/{movie_id}

#### Delete /actors/{actor_id}