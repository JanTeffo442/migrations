import psycopg2

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, String, Integer
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


connection = psycopg2.connect(database="devdb", user="user", password="pass", host="localhost", port=5432)
cursor = connection.cursor()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:pass@127.0.0.1/devdb'

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
    rocketchat_user = db.Column(db.String(20))
    githubname = db.Column(db.String(30))
    idnumber = db.Column(db.String(13))
    personal_email_address = db.Column(db.String(50),unique=True)
    cohort = db.Column(db.String(50))

    def __init__(self, firstname, surname, rocketchat_user, githubname, idnumber, personal_email_address, cohort):
        self.firstname = firstname
        self.surname = surname
        self.rocketchat_user = rocketchat_user
        self.githubname = githubname
        self.idnumber = idnumber
        self.personal_email_address = personal_email_address
        self.cohort = cohort
        


#cursor.execute()
connection.commit()
connection.close()

if __name__== '__main__':
    manager.run()
