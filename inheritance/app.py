from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
db = declarative_base()

# Creating table for our Databse
class User(db):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    fname = Column(String(22))
    lname = Column(String(22))
    username = Column(String(22), unique=True)
    password = Column(String(50))
    email = Column(String(22))
    status = Column(String(10))
    role = Column(String(10))

class Students(db):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    fname = Column(String(22))
    lname = Column(String(22))
    email = Column(String(22))
    role = Column(String(10))

# SQL object which will contane
class Employee(db):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    fname = Column(String(22))
    lname = Column(String(22))
    email = Column(String(22))
    role = Column(String(10))
    pay = Column(String(10))

# When user run the script  it will go to Database and create everything
if __name__ == '__main__':
    database = create_engine('sqlite:///DataBase/example.db')
    db.metadata.create_all(bind=database)
