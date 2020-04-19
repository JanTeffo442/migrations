import psycopg2

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, String, Integer
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


connection = psycopg2.connect(database="proddb", user="user", password="pass", host="localhost", port=5432)
cursor = connection.cursor()

query = """UPDATE recruits SET cohort='C25 Data Eng' WHERE id=1;
UPDATE recruits SET cohort='C25 Data Eng' WHERE id=2;
UPDATE recruits SET cohort='C25 Data Eng' WHERE id=3;
UPDATE recruits SET cohort='C25 Data Eng' WHERE id=4;
UPDATE recruits SET cohort='C25 Data Eng' WHERE id=5
;"""

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:pass@127.0.0.1/proddb'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager= Manager(app)

manager.add_command('db', MigrateCommand)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))

class Recruit(db.Model):
    __tablename__ = 'recruits'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(25))
    surname = db.Column(db.String(25))
    chatname = db.Column(db.String(20))
    githubname = db.Column(db.String(30))
    idnumber = db.Column(db.String(13))
    cohort = db.Column(String(50), unique=True)
    

    def __init__(self, firstname, surname, chatname, githubname, idnumber, cohort):
        self.firstname = firstname
        self.surname = surname
        self.chatname = chatname
        self.githubname = githubname
        self.idnumber = idnumber
        self.cohort = cohort
        

cursor.execute(query)
connection.commit() 

if __name__== '__main__':
    manager.run()
