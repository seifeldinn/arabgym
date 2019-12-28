from flask import request
from flask_restplus import Resource

from ..util.dto import GymTrainers
from ..service.trainers_service import newTrainer, trainerSearch, deleteTables

api = GymTrainers.api
_user = GymTrainers.user


@api.route('/addTrainer/')
class Trainer(Resource):
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return newTrainer(data=data)

@api.route('/delete/')
class Edit(Resource):
    def get(self):
        """search for a specific user"""
        return deleteTables()

@api.route('/trainerSearch/<searchString>')
@api.param('searchString', 'Search String kokokoko')
class Search(Resource):
    @api.marshal_list_with(_user)
    def get(self, searchString):
        """search for a specific user"""
        return trainerSearch(searchString)

