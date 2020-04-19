import psycopg2

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, String, Integer
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


connection = psycopg2.connect(database="proddb", user="user", password="pass", host="localhost", port=5432)
cursor = connection.cursor()

query = """INSERT INTO recruits(firstname,surname,chatname,githubname,idnumber,personal_email_address,chort) 
VALUES 
('Solly','Monate','Solman','Sollyhub','9211215773072','solly.m@example.com','C26 Web Design'),
('Visat','Moeng','Visat23','VisatMhub','0001014562073','visam@gmail.com','C26 Data Sci'),
('Donald','Sepeng','D0nn@1','DonasGH','9106156342081','s.donald@yahoo.com','C26 Strategy'),
('Bongi','Manamela','Manams','BongiGH','9812012465084','bongim@osn.io','C26 Data Eng'),
('Cedrick','Matome','Cedri52','CedriMat','9807196231087','cedrickm.b@all.com','C26 SysDev');"""


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
    personal_email_address = db.Column(db.String(30), unique= True)
    chort = db.Column(db.String(100))
    #cohort = db.Column(db.String(50))

    def __init__(self, firstname, surname, chatname, githubname, idnumber, personal_email_address, chort):
        self.firstname = firstname
        self.surname = surname
        self.chatname = chatname
        self.githubname = githubname
        self.idnumber = idnumber
        self.personal_email_address = personal_email_address
        self.chort = chort
        #self.cohort = cohort
        

cursor.execute(query)
connection.commit() 
connection.close()

if __name__== '__main__':
    manager.run()
