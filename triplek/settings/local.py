from .base import *
from decouple import config

SECRET_KEY = config('SECRET_KEY', default='5c^#zvhp!ud94)ch@b8qxdwozfg=u)59+kn*l@rwmy9$xf_mn_')

DEBUG = True

ALLOWED_HOSTS = []