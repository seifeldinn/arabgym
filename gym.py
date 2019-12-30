import os
import unittest

from app import blueprint
from flask_cors import CORS, cross_origin

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app.main import create_app, db
from app.main.model import add_user
from app.main.model import expenses
from app.main.model import member_sub
from app.main.model import trainers
from app.main.model import trainersLog


app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run(host="0.0.0.0", port="80")
    
@cross_origin(supports_credentials=True, debug = True)

@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1
    
if __name__ == '__main__':
    manager.run()
    db.create_all()

