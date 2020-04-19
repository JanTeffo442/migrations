import psycopg2

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, String, Integer
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


connection = psycopg2.connect(database="proddb", user="user", password="pass", host="localhost", port=5432)
cursor = connection.cursor()

query = """INSERT INTO recruits(firstname,surname,rocketchat_user,githubname,idnumber,personal_email_address,cohort) 
VALUES 
('Maloma','Peter','Malomza','Peterhub','9208215773072','pmaloma.m@example.com','C27 Multimedia'),
('Nadir','Naidoo','NNaidoo','Nadir','0010014562073','nnaidoo@gmail.com','C27 Data Sci'),
('Denel','Selepe','Denel1','Selegit','9107156342082','denel.slp@yahoo.com','C27 Strategy'),
('Salome','Baloi','SalBa','BaloHub','9802012465084','salome.b@osn.io','C27 Data Eng'),
('Zeb','Matabane','Zeb22','ZebMhun','9807176231087','zeb.matab@all.com','C27 SysDev');"""


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
    idnumber = db.Column(db.String(13))
    personal_email_address = db.Column(db.String(30), unique= True)
    #chort = db.Column(db.String(100))
    cohort = db.Column(db.String(50))

    def __init__(self, firstname, surname, rocketchat_user, githubname, idnumber, personal_email_address, cohort):
        self.firstname = firstname
        self.surname = surname
        self.rocketchat_user = rocketchat_user
        self.githubname = githubname
        self.idnumber = idnumber
        self.personal_email_address = personal_email_address
        #self.chort = chort
        self.cohort = cohort
        

cursor.execute(query)
connection.commit() 
connection.close()

if __name__== '__main__':
    manager.run()
