import os

SETTINGS_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.dirname(SETTINGS_DIR)

##################################################################
#
# SECRET SETTINGS
#
##################################################################
SECRET_KEY = '%n@()m&!ie01263sea(lwj0lnk1vuv56jy)ppt*&1q@085%!rh'

try:
    from secret_settings import *
except ImportError:
    print("Couldn't find secret_settings file. Creating a new one.")
    secret_settings_loc = os.path.join(SETTINGS_DIR, "secret_settings.py")
    with open(secret_settings_loc, 'w') as secret_settings:
        secret_key = ''.join([chr(ord(str(x)) % 90 + 33) for x in os.urandom(40)])
        secret_settings.write("SECRET_KEY = '''%s'''\n" % secret_key)
        from secret_settings import *
        
        
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

####################################################################
#
# TEMPLATE SETTINGS
#
###################################################################

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, "templates"),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    
    # for django-admin-tools
    'django.core.context_processors.request',
    
    # django allauth
    'allauth.account.context_processors.account',
    'allauth.socialaccount.context_processors.socialaccount',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

ALLOWED_HOSTS = []

####################################################################
#
# INSTALLED APPS
#
####################################################################

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    
    # django crispy forms
    #'crispy_forms',
    
    # site apps
    'wasteless_plates',
    'wasteless_plates.home',
    'wasteless_plates.recipes',
    
    # Django Allauth
    'allauth',
    'allauth.account',
    
)

###################################################################
#
# MIDDLEWARES
#
###################################################################

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
)

###################################################################
#
# URL SETTINGS
#
###################################################################
ROOT_URLCONF = 'wasteless_plates.urls'


WSGI_APPLICATION = 'wasteless_plates.wsgi.application'


###################################################################
#
# DATABASE SETTINGS
#
###################################################################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'db.sqlite3'),
    }
}

###################################################################
#
# TIMEZONE SETTINGS
#
###################################################################

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = False

USE_L10N = True

USE_TZ = False

###################################################################
#
# BLEACH SETTINGS
#
##################################################################
import bleach

ALLOWED_HTML_TAGS = bleach.ALLOWED_TAGS + ['h1', 'h2', 'h3', 'p', 'img']

ALLOWED_HTML_ATTRS = bleach.ALLOWED_ATTRIBUTES
ALLOWED_HTML_ATTRS.update({'img': ['src', 'alt'],})

##################################################################
#
# AUTHENTICATION SETTINGS
#
##################################################################

# Redirect to / upon login
LOGIN_REDIRECT_URL = "/"

# Users don't have to provide an email address when registering
ACCOUNT_EMAIL_REQUIRED = False

# Users don't need to verify their email address since it's not required
ACCOUNT_EMAIL_VERIFICATION = False

# Email settings
ACCOUNT_EMAIL_SUBJECT_PREFIX = "<Wasteless_Plates>"

ACCOUNT_AUTHENTICATION_METHOD = "username"

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # default
    'allauth.account.auth_backends.AuthenticationBackend',
)

ANONYMOUS_USER_ID = -1

ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda u: "/profile/%s/" % u.username,
}

SITE_ID = 1

###################################################################
#
# PRODUCTION SETTINGS
#
##################################################################
USE_X_FORWARDED_HOST = True
ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'wasteless_plates.pw',
    '.wasteless_plates.pw',
]


STATIC_URL = '/static/'

CRISPY_TEMPLATE_PACK = 'bootstrap3'
