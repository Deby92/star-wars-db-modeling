import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    userName = Column(String(100), unique=True, nullable=False)
    firstName = Column(String(50), unique=True, nullable=False)
    lastName = Column(String(50),)
    Email = Column(String(50), unique=True, nullable=False)

class People(Base):
    __tablename__ = 'People'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String(250),)
    skin_color = Column(String(250),)
    eye_color = Column(String(250),)
    gender= Column(String(250),)

class Planets(Base):
    __tablename__ = 'Planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    rotation_period = Column(String(250),)
    orbital_period = Column(String(250),)
    diameter = Column(Integer)
    climate = Column(String(250),)
    gravity = Column(String(250),)

class Vehicles(Base):
    __tablename__ = 'Vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250),)
    manufacturer = Column(String(250),)
    cost_in_credits = Column(Integer)
    length = Column(String(250),)
    crew = Column(Integer, nullable=False)
    passengers = Column(Integer, unique=True, nullable=False)

class Favorites_people(Base):
     __tablename__ = 'Favorites_people'
     user_id = Column(String(100), ForeignKey('User.id'), primary_key=True)
     people_id = Column(Integer, ForeignKey('People.people_id'),)

class favorites_vehicles(Base):
     __tablename__ = 'Favorites_vehicles'
     user_id = Column(String(100), ForeignKey('User.id'), primary_key=True )
     vehicles_id = Column(Integer, ForeignKey('Vehicles.vehicles_id'),)

class favorites_planets(Base):
     __tablename__ = 'Favorites_planets'
     user_id = Column(String(100), ForeignKey('User.id'), primary_key=True)
     planets_id = Column(Integer, ForeignKey('Planets.planets_id'),)
     

def to_dict(self):
    return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')