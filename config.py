import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\xd4\x80v!\x0e\xbe\xd1\x8e\x05T\xe8c\x18\x0fo\\'
    # MONGODB_SETTINGS = {
    #     'db' : 'UTA_Enrollment',
    #    'host': 'mongodb://mongo:27017/UTA_Enrollment' f
    #}