from flask import request
from flask_restplus import Resource
from dateutil.parser import parse


from ..util.dto import GymExpenses
from ..service.expenses_service import new_expense, searchMember, deleteTables

api = GymExpenses.api
_user = GymExpenses.user


@api.route('/')
class UserList(Resource):
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return new_expense(data=data)

@api.route('/delete/')
class Edit(Resource):
    def get(self):
        """search for a specific user"""
        return deleteTables()

@api.route('/monthReport/')
class Search(Resource):
    def get(self):
        startDate = request.args.get('startDate')
        endDate = request.args.get('endDate')
        return searchMember(startDate, endDate)