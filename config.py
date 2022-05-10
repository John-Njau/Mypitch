import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitchdb'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://vgksglwxuyjrpr:59b4e4d0e47fb6d6ca798c8d1021b43800f17b5a911951b73bbfe617cb6130ab@ec2-54-164-40-66.compute-1.amazonaws.com:5432/demm736i6va5ib'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    
    #email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    

class ProdConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitchdb'
    # DEBUG = True

    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
    uri = os.getenv('DATABASE_URL')
    if uri and uri.startswith('postgres://'):
        uri = uri.replace('postgres://', 'postgresql://', 1)
        
        SQLALCHEMY_DATABASE_URI=uri
    # pass
    
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitchdb'.replace("://","ql://",1)
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    
    
    # #email configurations
    # MAIL_SERVER = 'smtp.googlemail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')


class DevConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitchdb'
    DEBUG = True


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitchdb_test'



config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
