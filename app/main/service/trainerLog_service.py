import uuid
from datetime import datetime
import maya
from dateutil.parser import parse
from flask import jsonify, make_response

from sqlalchemy import or_, and_
import sqlalchemy

from app.main import db
from app.main.model.trainersLog import Gym_Trainers_Log 


def trainerArrival(data):
    trainers = Gym_Trainers_Log.query.filter(Gym_Trainers_Log.trainerId.like(data['trainerId'])).all()
    print(trainers)
    if not trainers:
        trainer = Gym_Trainers_Log(
        trainerName=data['trainerName'],
        arrival=data['arrival'],
        trainerId=data['trainerId'])
        save_changes(trainer)
        return 'Arrival Recorded' 
    for trainer in trainers:
        if parse(str(trainer.arrival)).date() == parse(str(datetime.today())).date():
    
            return "trainer already signed today"
        else:

            trainer = Gym_Trainers_Log(
            trainerName=data['trainerName'],
            arrival=data['arrival'],
            trainerId=data['trainerId'])
            save_changes(trainer)
            return 'Arrival Recorded'
    

def editTrainer(data):
    print(data)
    # arrivedTrainer = Gym_Trainers_Log.query.filter(and_(Gym_Trainers_Log.trainerName.like(data['trainerName']),
                                                        # Gym_Trainers_Log.arrival.like(data['arrival']))).first()

    trainers = Gym_Trainers_Log.query.filter(Gym_Trainers_Log.trainerId.like(data['trainerId'])).all()
    
    for trainer in trainers:
        if parse(str(trainer.arrival)).date() == parse(str(datetime.today())).date():
    
            trainer.departure = data["departure"]
            db.session.commit()
            return "success"

def deleteTables():
    num_rows_deleted = db.session.query(Gym_Trainers_Log).delete()
    db.session.commit()

    
def save_changes(data):
    db.session.add(data)
    db.session.commit()

def searchValues(searchString):
    keys = [ x.strip() for x in searchString.split(' ') ]
    values = []
    for i, key in enumerate(keys):
        values.append("%{key}%".format(key=key))
    return values

def extractDate(searchString):
    keys = [ x.strip() for x in searchString.split(' ') ]
    values = []
    
    space = " "
    joined = (keys[0], keys[1], keys[2], keys[3])
    date = space.join(joined)
    finalDate = parse(str(date)).date()
    return finalDate

def trainerSearch(searchString):
   
    values = searchValues(searchString)
    members = Gym_Trainers_Log.query.filter(and_(*[Gym_Trainers_Log.trainerId.like(value) for value in values])).all()

    for member in members:
        if not member.departure:
            if parse(str(member.arrival)).date() == parse(str(datetime.today())).date():
                return jsonify(member.serialize())
            else:
                return "null"
        if member.departure:
            if parse(str(member.departure)).date() == parse(str(datetime.today())).date():
                return "user already inside"

def trainerLog(startDate, endDate, userId):
    startDateValues = extractDate(startDate)
    endDateValues = extractDate(endDate)

    # trainerFullLog = Gym_Trainers_Log.query.filter(Gym_Trainers_Log.arrival.between(startDateValues, endDateValues) ,
                                                        # Gym_Trainers_Log.trainerId.like(userId)).all()

    trainerFullLog = Gym_Trainers_Log.query.filter(Gym_Trainers_Log.trainerId.like(userId)).all()
    trainerList = []
    for trainer in trainerFullLog:
        if extractDate(trainer.arrival)>=startDateValues and extractDate(trainer.arrival)<=endDateValues:
            dicc = {
                "trainerId": trainer.trainerId,
                "trainerName": trainer.trainerName,
                "arrival": trainer.arrival,
                "departure": trainer.departure 
            }
            trainerList.append(dicc)
    return trainerList

    

    # return trainerFullLog

    