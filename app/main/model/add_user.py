from .. import db, flask_bcrypt
import datetime
import jwt
from ..config import key

class GymUsers(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "Gym_Users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String())
    age = db.Column(db.String())
    phoneNumber = db.Column(db.String())
    gender = db.Column(db.String())
    photo = db.Column(db.String())

    def serialize(self):
            return {"id": self.id,
                    "name": self.name,
                    "age": self.age,
                    "phoneNumber": self.phoneNumber,
                    "gender": self.gender,
                    "photo": self.photo}

    
    
    


