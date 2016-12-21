import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string' 
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	CTC_MAIL_SUBJECT_PREFIX = '[Cascades Tech Club]'
	CTC_MAIL_SENDER = 'CTC Admin <donotreply.ctc@gmail.com>' 
	CTC_ADMIN = os.environ.get('CTC_ADMIN') or 'Admin'
	WTF_CSRF_ENABLED = True

	@staticmethod
	def init_app(app): 
		pass


class DevelopmentConfig(Config):
	DEBUG = True
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'donotreply.ctc@gmail.com'
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'CascadesTechClub'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config): 
	TESTING = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    	'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
