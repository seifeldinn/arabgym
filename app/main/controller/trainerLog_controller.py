from flask import request
from flask_restplus import Resource
from dateutil.parser import parse

from ..util.dto import GymTrainersLog
from ..service.trainerLog_service import trainerArrival, trainerSearch, editTrainer, trainerLog, deleteTables

api = GymTrainersLog.api
_user = GymTrainersLog.user


@api.route('/trainerArrival/')
class TrainerLog(Resource):   
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user)
    def post(self):
        """Creates a new User """
        data = request.json
        return trainerArrival(data=data)

@api.route('/editTrainer/')
class Edit(Resource):
    @api.response(202, 'User successfully updated.')
    @api.doc('edit trainer')
    @api.expect(_user)

    def post(self):
        """search for a specific user"""
        data = request.json
        return editTrainer(data=data)

@api.route('/delete/')
class Edit(Resource):
    def get(self):
        """search for a specific user"""
        return deleteTables()


@api.route('/trainerSearch/<searchString>')
@api.param('searchString')
class Search(Resource):
    @api.doc('list_of_units')
    def get(self, searchString):
        # print(searchString)
        """search for a specific user"""
        return trainerSearch(searchString)



@api.route('/trainerFullLog/')
class TrainerLog(Resource):
    @api.doc('list_of_units')

    def get(self):
        
        startDate = request.args.get('startDate')
        endDate = request.args.get('endDate')
        userId = request.args.get('userId')
       
        return trainerLog(startDate, endDate, userId)


