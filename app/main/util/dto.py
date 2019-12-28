from flask_restplus import Namespace, fields

class GymUsersDto:
     api = Namespace('Gym_Users', description='user related operations')
     user = api.model('Gym_Users', {
        'name': fields.String(required=True, description='Member Name'),
        'age': fields.String(required=True, description='Member Age'),
        'phoneNumber': fields.String(required=True, description='Member Phone Number'),
        'id': fields.String(),
        'gender': fields.String(),
        'photo': fields.String()

    })

class MemberSubscription:
    api = Namespace('Member_Subscription', description='Subscription related operations')
    user = api.model('Member_Subscription', {
        'member_id':fields.String(description='Member''s id'),
        'fees': fields.String( description='Member''s fees'),
        'subscription_date': fields.String(description='Subscription Date'), 
        'endSubscription_date': fields.String(required=True, description='Subscription End Date'),
        'photo': fields.String(),
        'gender': fields.String(),
        'originalFee':fields.String(),
        'owed':fields.String()

    })

class GymExpenses:
    api = Namespace('Gym_Expenses', description='Expenses related operations')
    user = api.model('Gym_Expenses', {
        'purchase_name': fields.String(),
        'fees': fields.String(),
        'purchase_date': fields.String() 
    })

class GymTrainers:
    api = Namespace('Gym_Trainers', description='trainer related operations')
    user = api.model('Gym_Trainers', {
        'name': fields.String(required=True),
        'age': fields.String(required=True),
        'phoneNumber': fields.String(required=True),
        'id': fields.String()       
    })
class GymTrainersLog:
    api = Namespace('Gym_Trainers_Log', description='trainer related operations')
    user = api.model('Gym_Trainers_Log', {
        'trainerId':fields.String(),
        'trainerName': fields.String(),
        'arrival': fields.String(),
        'departure': fields.String()       
    })