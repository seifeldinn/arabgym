import uuid
import datetime
from dateutil.parser import parse
from sqlalchemy import or_, and_
import sqlalchemy
from flask import jsonify, make_response
from app.main import db
from app.main.model.expenses import Gym_Expenses
from app.main.model.member_sub import Gym_Subs


def new_expense(data):
    gymExpense = Gym_Expenses(
        purchase_name=data['purchase_name'],
        fees=data['fees'],
        purchase_date=data['purchase_date']        
        )
    save_changes(gymExpense)
    return 'success'

def get_a_user(public_id):
    return Gym_Expenses.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()

def deleteTables():
    num_rows_deleted = db.session.query(Gym_Expenses).delete()
    db.session.commit()


def sum(objects):
    theSum = 0
    for obj in objects:
        
        theSum = theSum + int(obj.fees)
        
    return theSum

def searchValues(searchString):
    keys = [ x.strip() for x in searchString.split(' ') ]
    values = []
    
    space = " "
    joined = (keys[0], keys[1], keys[2], keys[3])
    date = space.join(joined)
    finalDate = parse(str(date)).date()
    return finalDate
    
def searchMember(startDate, endDate):

    firstDate = searchValues(startDate)
    secondDate = searchValues(endDate)
    print(startDate)
    print(secondDate)

    expenses = (Gym_Expenses.query.filter(*[Gym_Expenses.purchase_date.between(firstDate, secondDate)]).all())
    incomes = (Gym_Subs.query.filter(*[Gym_Subs.subscription_date.between(firstDate, secondDate)]).all())

    maleIncome = []
    femaleIncome = []
    print(incomes)
    for income in incomes:
        if income.gender == "male":
            maleIncome.append(income)
        else:
            femaleIncome.append(income)
        
    maleIncomeReport = sum(maleIncome)
    femaleIncomeReport = sum(femaleIncome)
    expense = sum(expenses)
    report = {
        "MaleIncome": maleIncomeReport,
        "FemaleIncome": femaleIncomeReport,
        "expenses": expense
    }
    return report