import os
from sqlalchemy import Column, String, Integer, Date, create_engine
from flask_sqlalchemy import SQLAlchemy
import json


database_path = 'postgresql://postgres@localhost:5432/casting_agency'

#database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
'''
def db_drop_and_create_all():
    db.drop_all()
    db.create_all()


'''
Movie
Have title and release date
'''
class Movie(db.Model):  
    __tablename__ = 'Movie'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(Date)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    '''
    insert()
        inserts a new model into a database
        EXAMPLE
            movie = Movie(title, release_date)
            movie.insert()
    '''
    def insert(self):
        db.session.add(self)
        db.session.commit()


    '''
    delete()
        deletes a  model from a database
        EXAMPLE
            movie = Movie.query.filter(Movie.id == id).one_or_none()
            movie.delete()
    '''
    def delete(self):
        db.session.delete(self)
        db.session.commit()


    '''
    update()
        updates a model in a database
        EXAMPLE
            movie = Movie.query.filter(Movie.id == id).one_or_none()
            movie.title = 'Into The Wild'
            movie.update()
    '''
    def update(self):
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date
            }

    def __repr__(self):
        return json.dumps(self.format())


'''
Movie
Have title and release date
'''
class Actor(db.Model):  
    __tablename__ = 'Actor'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    '''
    insert()
        inserts a new model into a database
        EXAMPLE
            actor = Actor(name, age, gender)
            actor.insert()
    '''
    def insert(self):
        db.session.add(self)
        db.session.commit()


    '''
    delete()
        deletes a  model from a database
        EXAMPLE
            actor = Actor.query.filter(Actor.id == id).one_or_none()
            actor.delete()
    '''
    def delete(self):
        db.session.delete(self)
        db.session.commit()


    '''
    update()
        updates a model in a database
        EXAMPLE
            actor = Actor.query.filter(Actor.id == id).one_or_none()
            actor.title = 'Emile Hirsch'
            actor.update()
    '''
    def update(self):
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }

    def __repr__(self):
        return json.dumps(self.format())


