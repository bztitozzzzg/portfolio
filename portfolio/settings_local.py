import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 本番環境用メール設定
"""
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "xxxxxxxx@gmail.com"
EMAIL_HOST_PASSWORD = ""
EMAIL_USE_TLS = True
"""
SECRET_KEY = "y5f2(_*5$sz!@z08*0v#i5fc36x@_7*6=7s@_wedxgxacjud0("
# reCAPTCHA
RECAPTCHA_SITE_KEY = "6Lf1b8giAAAAABNKx6RNeI8C_9oo0qBDNS-nUGAj"
RECAPTCHA_SECRET_KEY = "6Lf1b8giAAAAAAUYvL4nzxlMN-EJhxnOf9SdG9z0"
DEBUG = True
