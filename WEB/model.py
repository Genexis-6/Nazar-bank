from . import db,app
from flask_login import UserMixin
from datetime import datetime
# AZUDONI VICTORY CHUWKUNEKU WORK

class Debit(db.Model):
    __tablename__ = 'Debit'
    id = db.Column(db.Integer,primary_key = True)
    text =  db.Column(db.String(100),nullable=True)
    debit_amount = db.Column(db.String(255), nullable=False,default=0.0)
    user_id = db.Column(db.Integer,db.ForeignKey('login.id'),nullable = False)
    date = db.Column(db.DateTime,default=datetime.now())
    # AZUDONI VICTORY CHUWKUNEKU WORK

class Track_Transaction(db.Model):
    __tablename__ = 'Track_Transaction'
    id = db.Column(db.Integer,primary_key = True)
    text =  db.Column(db.String(100),nullable=True)
    transfer_amount = db.Column(db.String(255), nullable=False,default=0.0)
    user_id = db.Column(db.Integer,db.ForeignKey('login.id'),nullable = False)
    date = db.Column(db.DateTime,default=datetime.now())
    

class Track_Deposite(db.Model):
    __tablename__ = 'Track_Deposite'
    id = db.Column(db.Integer,primary_key = True)
    text =  db.Column(db.String(100),nullable=True)
    deposite_amount = db.Column(db.String(255), nullable=False,default=0.0)
    user_id = db.Column(db.Integer,db.ForeignKey('login.id'),nullable = False)
    date = db.Column(db.DateTime,default=datetime.now())
    
    

class Dollar(db.Model):
    __tablename__ = 'dollar'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100),nullable=False)
    amount = db.Column(db.Float, nullable=False,default=0.0)
    user_id = db.Column(db.Integer,db.ForeignKey('balance.id'),nullable = False)
    date = db.Column(db.DateTime,default=datetime.utcnow)
    


class Savings(db.Model):# AZUDONI VICTORY CHUWKUNEKU WORK
    __tablename__ = 'savings'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100),nullable=False)
    amount = db.Column(db.Float, nullable=False,default=0.0)
    user_id = db.Column(db.Integer,db.ForeignKey('balance.id'),nullable = False)
    date = db.Column(db.DateTime,default=datetime.utcnow)
    
  
    # AZUDONI VICTORY CHUWKUNEKU WORK
class Utility(db.Model):
    __tablename__ = 'utility'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100),nullable=False)
    amount = db.Column(db.Float, nullable=False,default=0.0)
    user_id = db.Column(db.Integer,db.ForeignKey('balance.id'),nullable = False)
    date = db.Column(db.DateTime,default=datetime.utcnow)
    
  
class Current(db.Model):# AZUDONI VICTORY CHUWKUNEKU WORK
    __tablename__ = 'current'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100),nullable=False)
    amount = db.Column(db.Float, nullable=False,default=0.0)
    user_id = db.Column(db.Integer,db.ForeignKey('balance.id'),nullable = False)
    date = db.Column(db.DateTime,default=datetime.utcnow)
    
  




class Balance(db.Model):
    __tablename__ = 'balance'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100),nullable=False)
    money = db.Column(db.Float, nullable=False,default=0.0)
    user_id = db.Column(db.Integer,db.ForeignKey('login.id'),nullable = False)
    date = db.Column(db.DateTime,default=datetime.utcnow)
    
    current = db.relationship('Current', backref='balance',uselist=False)
    utility = db.relationship('Utility', backref='balance',uselist=False)
    savings = db.relationship('Savings', backref='balance',uselist=False)
    dollar = db.relationship('Dollar', backref='balance',uselist=False)
    
    
   # AZUDONI VICTORY CHUWKUNEKU WORK 
    
class LoginDataBase(db.Model,UserMixin):
    __tablename__ = 'login'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100), nullable = False)
    username = db.Column(db.String(100),nullable = False)
    phone = db.Column(db.String(100),nullable = False)
    password = db.Column(db.String(255),nullable = False)
    accnum = db.Column(db.String(25),nullable = False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    balance = db.relationship('Balance', backref='login',uselist=False)
    track = db.relationship('Track_Deposite', backref='login',uselist=False)
    trans = db.relationship('Track_Transaction', backref='login',uselist=False)
    debit = db.relationship('Debit', backref='login',uselist=False)
    



# AZUDONI VICTORY CHUWKUNEKU WORK

class Admin(db.Model, UserMixin):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key = True)
    code = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String(255), nullable = False)