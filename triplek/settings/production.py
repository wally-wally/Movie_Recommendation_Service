from .base import *
from decouple import config
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# if DEBUG:
#     import mimetypes
#     mimetypes.add_type("application/javascript", ".js", True)

ALLOWED_HOSTS = ['triple-k.prgypar4mi.ap-northeast-2.elasticbeanstalk.com']
