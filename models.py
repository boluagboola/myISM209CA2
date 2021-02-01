from main import db
from datetime import date

class User(db.Model):
 __tablename__= 'MTN_Users'

 firstname= db.Column(db.String(20), unique=False, nullable=False)
 surname = db.Column(db.String(20), unique=False, nullable=False)
 residentialaddress= db.Column(db.String(20), unique=False, nullable=True)
 dateofbirth = db.Column(db.Date,  nullable=False, default= date.today)
 nationality = db.Column(db.String(100), unique=False, nullable=False)
 nationalidentitynmber = db.Column(db.Integer, primary_key=True)

 # represent the object when it is queried for
 def __repr__(self):
  return '<Register {}>'.format(self.id)

