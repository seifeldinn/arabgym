import uuid
import datetime

from sqlalchemy import or_, and_
import sqlalchemy

from app.main import db
from app.main.model.trainers import Gym_Trainers 

def newTrainer(data):
    trainer = Gym_Trainers(
        name=data['name'],
        age=data['age'],
        phoneNumber=data['phoneNumber']        
    )
    save_changes(trainer)
    return trainer.id

def get_a_user(public_id):
    return Gym_Trainers.query.filter_by(public_id=public_id).first()

def deleteTables():
    num_rows_deleted = db.session.query(Gym_Trainers).delete()
    db.session.commit()

    
def save_changes(data):
    db.session.add(data)
    db.session.commit()

def trainerSearch(searchString):
   
    keys = [ x.strip() for x in searchString.split(' ')]
    values = []
    for i, key in enumerate(keys):
        values.append("%{key}%".format(key=key))
        
    return Gym_Trainers.query.filter(and_(*[Gym_Trainers.name.like(name) for name in values])).all()
