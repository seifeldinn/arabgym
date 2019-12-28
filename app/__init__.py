
from flask_restplus import Api
from flask import Blueprint

from .main.controller.gym_controller import api as gym_ns
from .main.controller.Subscription_controller import api as sub_ns
from .main.controller.expenses_controller import api as gym_exp
from .main.controller.trainers_controller import api as gym_tra
from .main.controller.trainerLog_controller import api as tra_log

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(gym_ns, path='/gymUsers')
api.add_namespace(sub_ns, path='/gymSubs')
api.add_namespace(gym_exp, path='/gymExp')
api.add_namespace(gym_tra, path='/gymTra')
api.add_namespace(tra_log, path='/traLog')


