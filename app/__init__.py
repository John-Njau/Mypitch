from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask_mail import Mail
from flask_login import LoginManager
from flask_simplemde import SimpleMDE
from flask_uploads import UploadSet, configure_uploads, IMAGES

# app initialization
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pitchdb.db'


# flask extensions initialization
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
mail = Mail(app)
login_manager = LoginManager(app)
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
simple = SimpleMDE(app)
mail = Mail(app)

def create_app(config_name):
    # app configurations
    app.config.from_object(config_options[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['SECRET_KEY'] = 'ketyzdxfcghj'
    # app.config['SQLALCHEMY_db_URI'] = 'sqlite:///pitchdb.db'
    
    
    #main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    # auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
