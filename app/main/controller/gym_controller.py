from flask import request
from flask_restplus import Resource

from ..util.dto import GymUsersDto
from ..service.gym_members_service import save_new_user, get_all_users, searchMember, editMember, deleteTables, deleteUser, genderSearch, memberCount

api = GymUsersDto.api
_user = GymUsersDto.user


@api.route('/')
class UserList(Resource):
    @api.doc('list_of_gym_users')
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
        return save_new_user(data=data)


@api.route('/<searchString>')
@api.param('searchString', 'Search String kokokoko')
class Search(Resource):
    @api.doc('list_of_units')
    @api.marshal_list_with(_user)
    def get(self, searchString):
        """search for a specific user"""
        return searchMember(searchString)

@api.route('/editUser/')
class Edit(Resource):
    @api.marshal_list_with(_user)
    def get(self):
        """search for a specific user"""
        data = request.json
        return editMember(data)

@api.route('/delete/')
class Edit(Resource):
    def get(self):
        """search for a specific user"""
        return deleteTables()

@api.route('/deleteUser')
class Delete(Resource):
    def get(self):
        memberId = request.args.get('memberId')
        return deleteUser(memberId)

@api.route('/genderSearch')
class GenderSearch(Resource):
    def get(self):
        memberGender = request.args.get('memberGender')
        return genderSearch(memberGender)

@api.route('/membersCount')
class MembersCount(Resource):
    def get(self):
        koko = request.args.get('koko')
        print("kokokoko")
        return memberCount()


@api.route('/koko')
class count(Resource):
    def get(self):
        return memberCount()