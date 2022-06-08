from .settings import *

DEBUG = True

SECRET_KEY = "qpQ19}6?X+HU>sCUY2x,MLAB"
ALLOWED_HOSTS = ['127.0.0.1']

DATABESE= {
    'default': {
        'ENGINE': 'db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}