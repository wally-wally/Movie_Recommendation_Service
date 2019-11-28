from .base import *
from decouple import config
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='$sh)4n*h1px8&byrscp)0iarm*!+9in+6_)ov$px#fgz%dtjmk')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# if DEBUG:
#     import mimetypes
#     mimetypes.add_type("application/javascript", ".js", True)

ALLOWED_HOSTS = []
