import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Movie, Actor


class CapstoneTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "casting_agency"
        self.database_path = "postgresql://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_movie = {
            'title': 'Anansi Boys2',
            'release_date': '10-19-2009'
        }

        self.new_actor = {
            "name": "Emile Hirsch2",
            "age": 35,
            "gender": "male"
        }

        self.executive_producer = {'Authorization': os.environ['EXECUTIVE_PRODUCER_TOKEN']}

        self.casting_director  = {'Authorization': os.environ['CASTING_DIRECTOR_TOKEN']}

        self.casting_assistant  = {'Authorization': os.environ['CASTING_ASSISTANT_TOKEN']}

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_movies(self):
        """Test get movies success"""

        res = self.client().get('/movies', headers=self.casting_assistant)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_400_if_get_movies_fails(self):
        """Test get movies fail if there are no movies"""

        res = self.client().get('/movies', headers=self.casting_assistant)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')

    def test_get_actors(self):
        """Test get actors success"""

        res = self.client().get('/actors', headers=self.executive_producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_400_if_get_actors_fails(self):
        """Test get actors fail if there are no actors"""

        res = self.client().get('/actors', headers=self.executive_producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')


    def test_create_new_movie(self):
        res = self.client().post('/movies', json=self.new_movie, headers=self.executive_producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['movie'])
    
    def test_422_if_movie_creation_fails(self):
        res = self.client().post('/movies', json={}, headers=self.executive_producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_create_new_actor(self):
        res = self.client().post('/actors', json=self.new_actor, headers=self.casting_director)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['actor'])
    
    def test_422_if_actor_creation_fails(self):
        res = self.client().post('/actors', json={}, headers=self.casting_director)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_edit_movie(self):
        res = self.client().patch('/movies/1', json=self.new_movie, headers=self.casting_director)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['movie'])
    
    def test_422_if_movie_edit_fails(self):
        res = self.client().patch('/movies/1', headers=self.executive_producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_edit_actor(self):
        res = self.client().patch('/actors/1', json=self.new_movie, headers=self.executive_producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['actor'])
    
    def test_422_if_actor_edit_fails(self):
        res = self.client().patch('/actors/1', headers=self.executive_producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_delete_movie(self):
        res = self.client().delete('/movies/2', headers=self.executive_producer)
        data = json.loads(res.data)

        movie = Movie.query.filter(Movie.id == 2).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(int(data['delete']), 2)
        self.assertEqual(movie, None)  

    def test_404_if_movie_does_not_exist(self):
        res = self.client().delete('/movies/1000', headers=self.executive_producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_delete_actor(self):
        res = self.client().delete('/actors/2', headers=self.executive_producer)
        data = json.loads(res.data)

        actor = Actor.query.filter(Actor.id == 2).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(int(data['delete']), 2)
        self.assertEqual(actor, None)  

    def test_404_if_actor_does_not_exist(self):
        res = self.client().delete('/actors/1000', headers=self.executive_producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
