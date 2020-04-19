import psycopg2

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, String, Integer
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


connection = psycopg2.connect(database="proddb", user="user", password="pass", host="localhost", port=5432)
cursor = connection.cursor()

query = """INSERT INTO recruits(firstname,surname,rocketchat_user,githubname,personal_email_address,cohort) 
VALUES 
('Glen','Livet','Glenzo','Glengit','glen.liv@example.com','C28 Creative'),
('Elsa','Brent','Elsa02','EBrentGit','elsa.b@gmail.com','C28 Strategy'),
('David','Kwakwa','Davik','Davidhub','david.kw@yahoo.com','C28 WebDev'),
('Madi','Leope','Leope45','Madhub','madi.leo@osn.io','C28 Data Eng'),
('Elliot','Segoale','Elliot79','EllioHub','zeb.e.segoale@all.com','C28 SysDev');"""


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
    rocketchat_user = db.Column(db.String(20))
    githubname = db.Column(db.String(30))
    personal_email_address = db.Column(db.String(30), unique= True)
    cohort = db.Column(db.String(50))

    def __init__(self, firstname, surname, rocketchat_user, githubname, personal_email_address, cohort):
        self.firstname = firstname
        self.surname = surname
        self.rocketchat_user = rocketchat_user
        self.githubname = githubname
        self.personal_email_address = personal_email_address
        self.cohort = cohort
        

cursor.execute(query)
connection.commit() 
connection.close()

if __name__== '__main__':
    manager.run()
