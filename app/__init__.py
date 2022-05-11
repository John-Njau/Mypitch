from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask_mail import Mail
from flask_login import LoginManager
import os
# from flask_uploads import UploadSet, IMAGES, configure_uploads

# app initialization
app = Flask(__name__)

# uri = os.getenv('DATABASE_URL')
# if uri and uri.startswith('postgres://'):
#     uri = uri.replace('postgres://', 'postgresql://', 1)
#     SQLALCHEMY_DATABASE_URI = uri
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pitchdb.db'
# app.config['SQLALCHEMY_DATABASE_URI']='postgresql://vgksglwxuyjrpr:59b4e4d0e47fb6d6ca798c8d1021b43800f17b5a911951b73bbfe617cb6130ab@ec2-54-164-40-66.compute-1.amazonaws.com:5432/demm736i6va5ib'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# flask extensions initialization
bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
mail = Mail()
# photos = UploadSet('photos', IMAGES)

def create_app(config_name):
    # app configurations
    app.config.from_object(config_options[config_name])
    
    #mail instance
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    
    #configure upload set
    # configure_uploads(app, photos)
    
    
    #main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    # auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
