import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import db_drop_and_create_all, setup_db, Movie, Actor
from auth import AuthError, requires_auth


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    # db_drop_and_create_all()

    @app.route('/')
    def index():
        return "Hello World"

    @app.route('/movies')
    @requires_auth('get:movies')
    def get_movies(self):
        movies = Movie.query.order_by(Movie.id).all()
        formatted_movies = [movie.format() for movie in movies]

        if len(formatted_movies) == 0:
            abort(400)

        return jsonify({
            'success': True,
            'movies': formatted_movies
        })

    @app.route('/actors')
    @requires_auth('get:actors')
    def get_actors(self):
        actors = Actor.query.order_by(Actor.id).all()
        formatted_actors = [actor.format() for actor in actors]

        if len(formatted_actors) == 0:
            abort(400)

        return jsonify({
            'success': True,
            'actors': formatted_actors
        })

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def create_movie(self):
        body = request.get_json()

        if (body is None):
            abort(422)

        new_title = body.get('title')
        new_release_date = body.get('release_date')

        # if one or more of the inputs in the new movie form is empty
        if (new_title is None) or (new_release_date is None):
            abort(422)

        try:
            movie = Movie(title=new_title, release_date=new_release_date)
            movie.insert()

            return jsonify({
                'success': True,
                'movie': movie.format()
            })

        except:
            abort(422)

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def create_actor(self):
        body = request.get_json()

        if (body is None):
            abort(422)

        new_name = body.get('name')
        new_age = body.get('age')
        new_gender = body.get('gender')
        # if one or more of the inputs in the new actor form is empty
        if (new_name is None) or (new_age is None) or (new_gender is None):
            abort(422)

        try:
            actor = Actor(name=new_name, age=new_age, gender=new_gender)
            actor.insert()

            return jsonify({
                'success': True,
                'actor': actor.format()
            })

        except:
            abort(422)

    @app.route('/movies/<id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def edit_movie(self, id):
        movie = Movie.query.get(id)
        try:
            if movie is None:
                abort(404)

            body = request.get_json()

            if (body is None):
                abort(422)

            new_title = body.get('title')
            new_release_date = body.get('release_date')

            if new_title is not None:
                movie.title = new_title

            if new_release_date is not None:
                movie.release_date = new_release_date

            movie.update()

            return jsonify({
                'success': True,
                'movie': movie.format()
            })

        except:
            abort(422)

    @app.route('/actors/<id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def edit_actor(self, id):
        actor = Actor.query.get(id)
        try:
            if actor is None:
                abort(404)

            body = request.get_json()

            if (body is None):
                abort(422)

            new_name = body.get('name')
            new_age = body.get('age')
            new_gender = body.get('gender')

            if new_name is not None:
                actor.name = new_name

            if new_age is not None:
                actor.age = new_age

            if new_gender is not None:
                actor.gender = new_gender

            actor.update()

            return jsonify({
                'success': True,
                'actor': actor.format()
            })

        except:
            abort(422)

    @app.route('/movies/<id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(self, id):
        movie = Movie.query.get(id)
        try:
            if movie is None:
                abort(404)

            movie.delete()

            return jsonify({
                'success': True,
                'delete': id
            })

        except:
            abort(422)

    @app.route('/actors/<id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(self, id):
        actor = Actor.query.get(id)
        try:
            if actor is None:
                abort(404)

            actor.delete()

            return jsonify({
                'success': True,
                'delete': id
            })

        except:
            abort(422)

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    @app.errorhandler(AuthError)
    def handle_auth_error(err):
        response = jsonify(err.error)
        response.status_code = err.status_code
        return response

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
