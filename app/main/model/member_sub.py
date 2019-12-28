from .. import db, flask_bcrypt
import datetime
import jwt
from ..config import key

class Gym_Subs(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "Member_Subscription"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    member_id = db.Column(db.String())
    fees = db.Column(db.String())
    subscription_date = db.Column(db.String())
    endSubscription_date = db.Column(db.String())
    photo = db.Column(db.String())
    gender = db.Column(db.String())
    originalFee = db.Column(db.String())
    owed = db.Column(db.String())


    def serialize(self):
        return {"id": self.id,
                "member_id": self.member_id,
                "fees": self.fees,
                "purchase_date": self.purchase_date,
                "endSubscription_date": self.purchase_date,
                "photo": self.photo,
                "originalFee": self.originalFee,
                "owed": self.owed
                }

