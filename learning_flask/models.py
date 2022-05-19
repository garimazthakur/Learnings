from uuid import UUID
from matplotlib.pyplot import table
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
# from sqlalchemy import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import relationship
from flask import Flask
import uuid
app= Flask(__name__) 

SECRET_KEY='c1b6653f2af3ef38389f562bf8681107'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:123456@localhost:5432/flask2"
db= SQLAlchemy(app)
migrate=Migrate(app, db)

association_table=  db.Table('association', db.Model.metadata, 
                                db.Column('left_id', ForeignKey('left.id')),
                                db.Column('right_id', ForeignKey('right.id'))
                            )
              
class Employer(db.Model):
    _tablename__= "employer"
    id=db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    company = db.Column(db.String(255))
    first_name = db.Column(db.String(255)) #employer's
    last_name = db.Column(db.String(255)) #employer's
    email = db.Column(db.String(255)) 
    employees = db.relationship('Employees',secondary=association_table, backref='employer')

    def __init__(self, company, first_name, last_name, email, employees):
        self.company=company
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.employees=employees


class Employees(db.Model):
    __tablename__="employees"
    id=db.Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    worksfor = db.Column(db.String(255))
    employer_id= db.Column(UUID(as_uuid=True), db.ForeignKey('employer.id'))

    def __init__(self, worksfor, first_name, last_name, email, employer_id):
        self.worksfor=worksfor
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.employer_id=employer_id

