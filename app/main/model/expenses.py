from .. import db, flask_bcrypt
import datetime
import jwt
from ..config import key

class Gym_Expenses(db.Model):
    """ User Model for storing expenses related details """

    __tablename__ = "Gym_Expenses"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    purchase_name = db.Column(db.String())
    fees = db.Column(db.String())
    purchase_date = db.Column(db.String())

    def serialize(self):
        return {"id": self.id,
                "purchase_name": self.purchase_name,
                "fees": self.fees,
                "purchase_date": self.purchase_date
                }
