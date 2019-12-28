from .. import db, flask_bcrypt
import datetime
import jwt
from ..config import key

class Gym_Trainers_Log(db.Model):
    """ User Model for storing trainer related details """

    __tablename__ = "Gym_Trainers_Log"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    trainerId = db.Column(db.String())
    trainerName = db.Column(db.String())
    arrival = db.Column(db.String())
    departure = db.Column(db.String())

    def serialize(self):
        return {"id": self.id,
                "trainerId": self.trainerId,
                "trainerName": self.trainerName,
                "arrival": self.arrival,
                "departure": self.departure}

