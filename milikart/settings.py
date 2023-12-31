"""
Django settings for milikart project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!tm92g$mh61_+udur&kd=&h8x-oqxvm2iu^kmi5i0)w!l56%t&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop.apps.ShopConfig',
    'cart.apps.CartConfig',
    'orders.apps.OrdersConfig',
    'payment.apps.PaymentConfig',
    'coupons.apps.CouponsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'milikart.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
            ],
        },
    },
]
#Context processors are executed in all the requests that use RequestContext. You might 
# want to create a custom template tag instead of a context processor if your functionality 
# is not needed in all templates, especially if it involves database queries.


WSGI_APPLICATION = 'milikart.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'shop',
    'USER': 'root',
    'PASSWORD': 'mili@88877',
    'HOST': '127.0.0.1',
    'port':'3306',
}
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MEDIA_URL='media/'
MEDIA_ROOT=BASE_DIR/'media'

#settings for cart session
CART_SESSION_ID='cart'
#this is to append slash at the ending
APPEND_SLASH=False

#below settings are to send email to users after order placed
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'djangomail888@gmail.com'
EMAIL_HOST_PASSWORD = 'dpxazdtbkfryewfc'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


#below settings are for stripe payment method
STRIPE_PUBLISHABLE_KEY='pk_test_51MsJ1fSDyujjV1csKRuTs28gjKcj80dmNkfnDesAw0JjPr1JF5zFIDWPyGIwQ2N4h3S4FBt4xpXZTWQF4L9eL7Jg00oFAKQ7n7'
STRIPE_SECRET_KEY='sk_test_51MsJ1fSDyujjV1cskzapbSUrlj7huq96mmQH1XCKuTYrArPgsffsEJrL5mrTsCApgirdd7vJlPPgSBkQsRniYK7i00K2wxnZKm'
STRIPE_API_VERSION='2022-08-01'
STRIPE_WEBHOOK_SECRET='whsec_ca5027a85085bda4833ef70f2e7e0541b211659ebc0a3bcef6542ea2fb0693c6'

STATIC_ROOT = BASE_DIR / 'static'