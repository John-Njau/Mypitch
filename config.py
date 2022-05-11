import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgres://qplimxwduuflyi:b6e1f62b9a7462f2152f7f57ea80155e112adb4b86f986a17e301e187b154d31@ec2-54-172-175-251.compute-1.amazonaws.com:5432/de0el35k0asfhf'

    # UPLOADED_PHOTOS_DEST = 'app/static/photos'
    
    #email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://qplimxwduuflyi:b6e1f62b9a7462f2152f7f57ea80155e112adb4b86f986a17e301e187b154d31@ec2-54-172-175-251.compute-1.amazonaws.com:5432/de0el35k0asfhf'
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitchdb'
    # DEBUG = True

    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
    # uri = os.getenv('DATABASE_URL')
    # if uri and uri.startswith('postgres://'):
    #     uri = uri.replace('postgres://', 'postgresql://', 1)
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
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitchdb'
    DEBUG = True


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitchdb_test'



config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
