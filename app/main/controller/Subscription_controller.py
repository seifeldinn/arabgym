from flask import request
from flask_restplus import Resource

from ..util.dto import MemberSubscription
from ..service.gym_subscription_service import new_subscription, deleteTables, searchMember, displaySubs

api = MemberSubscription.api
_user = MemberSubscription.user


@api.route('/')
class UserList(Resource):
    @api.doc('subscription list')
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_users()

    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return new_subscription(data=data)


@api.route('/delete/')
class Edit(Resource):
    def get(self):
        """search for a specific user"""
        return deleteTables()


@api.route('/<searchString>')
@api.param('searchString', 'Search String kokokoko')
class Search(Resource):
    @api.doc('list_of_units')
    @api.marshal_list_with(_user)
    def get(self, searchString):
        """search for a specific user"""
        return searchMember(searchString)

@api.route('/subReport/')
class Search(Resource):
    def get(self):

        startDate = request.args.get('startDate')
        endDate = request.args.get('endDate')
        return displaySubs(startDate, endDate)
        

