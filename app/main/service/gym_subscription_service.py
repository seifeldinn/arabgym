import uuid
import datetime
from dateutil.parser import parse

from sqlalchemy import or_, and_
import sqlalchemy
import sqlite3

from app.main import db
from app.main.model.member_sub import Gym_Subs
from app.main.model.add_user import GymUsers


def new_subscription(data):
    subscribed = GymUsers.query.filter_by(id=data['member_id']).first()
    image = subscribed.photo
    memberGender = subscribed.gender
    # if not subscribed:
    gymSubscriber = Gym_Subs(
        member_id=data['member_id'],
        fees=data['fees'],
        subscription_date=data['subscription_date'],
        endSubscription_date=data['endSubscription_date'],
        photo= image,
        gender= memberGender,
        originalFee= data['originalFee'],
        owed= data['owed']
        )
    save_changes(gymSubscriber)
    return 'success'

def deleteTables():
    num_rows_deleted = db.session.query(Gym_Subs).delete()
    db.session.commit()

def get_all_users():
        return Gym_Subs.query.all()


def get_a_user(public_id):
    return Gym_Subs.query.filter_by(public_id=public_id).first()

def editSubscription(data):
    editedSubscription = Gym_Subs.query.filter_by(subscription_date=data['subscription_date']).first()
    editedSubscription.fees = data.fees
    editedSubscription.subscription_date = data.subscription_date
    editedSubscription.endSubscription_date = data.endSubscription_date
    editedSubscription.session.comit()

def deleteSubscription(userId):
    initialMember = GymUsers.query.filter(and_(*[Gym_Subs.member_id.like(memberId)])).first()
#     if deletedSubscription.subscription_date

def save_changes(data):
    db.session.add(data)
    db.session.commit()


def searchValues(searchString):
    keys = [ x.strip() for x in searchString.split(' ') ]
    values = []
    
    space = " "
    joined = (keys[0], keys[1], keys[2], keys[3])
    date = space.join(joined)
    finalDate = parse(str(date)).date()
    return finalDate

def displaySubs(startDate, endDate):
    firstDate = searchValues(startDate)
    secondDate = searchValues(endDate)
    return Gym_Subs.query.filter(and_(*[Gym_Subs.endSubscription_date >= Gym_Subs.endSubscription_date.between(firstDate, secondDate)])).all()

def searchMember(searchString):
   
    subscribedArr = []
    keys = [ x.strip() for x in searchString.split(' ') ]
    values = []
    for i, key in enumerate(keys):
        values.append("%{key}%".format(key=key))

    subscribed = Gym_Subs.query.filter(and_(*[Gym_Subs.member_id.like(member_id) for member_id in values])).all()
    if not subscribed:
        subscribed = GymUsers.query.filter(and_(*[GymUsers.id.like(member_id) for member_id in values])).first()
        subscribedArr.append(subscribed)
        print("koko")
        return subscribedArr
    else:
        return subscribed 
    