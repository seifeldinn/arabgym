import uuid
import datetime
from datetime import date

from dateutil.parser import parse
from app.main import db
from app.main.model.add_user import GymUsers
from app.main.model.member_sub import Gym_Subs
from sqlalchemy import or_, and_, update
import json

def save_new_user(data):
    members = GymUsers.query.filter_by(name=data['name']).first()
    if not members:
        gymUsers = GymUsers(
            name=data['name'],
            age=data['age'],
            phoneNumber=data['phoneNumber'],
            gender= data['gender'],
            photo=data['photo']
        )
        save_changes(gymUsers)
        return gymUsers.id

    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists.',
        }
        return response_object, 409

def get_all_users():
        return GymUsers.query.all()


def deleteUser(public_id):
    initialMember = GymUsers.query.filter(and_(*[GymUsers.id.like(public_id)])).first()
    db.session.delete(initialMember)
    
    memberSubs = Gym_Subs.query.filter(and_(*[Gym_Subs.member_id.like(public_id)])).all()
    for membersub in memberSubs:
        db.session.delete(membersub)

    db.session.commit()

    return "Member Deleted"
def editMember(data):
    member = GymUsers.query.filter_by(id = data['id']).update(dict(name=data['name'], age=data['age'], phoneNumber = data['phoneNumber']))

    db.session.commit()
    return 'success'

def save_changes(data):
    db.session.add(data)
    db.session.commit()

def deleteTables():
    num_rows_deleted = db.session.query(GymUsers).delete()
    db.session.commit()

def genderSearch(memberGender):
    members = GymUsers.query.filter(and_(*[GymUsers.gender.like(memberGender)])).all()
    return members

def searchMember(searchString):
   
    keys = [ x.strip() for x in searchString.split(' ') ]
    values = []
    for i, key in enumerate(keys):
        values.append("%{key}%".format(key=key))

    members = GymUsers.query.filter(or_((GymUsers.id.like(value)) | (GymUsers.name.like(value)) for value in values )).all()
    return members

def memberCount():
    return Gym_Subs.query.filter(and_(*[Gym_Subs.endSubscription_date >= date.today()])).count()
