import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = "y5f2(_*5$sz!@z08*0v#i5fc36x@_7*6=7s@_wedxgxacjud0("

# DEBUG = True
DEBUG = False

# 本番環境用メール設定
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "bztitozzzzg@gmail.com"
EMAIL_HOST_PASSWORD = "zawmmyhpgykocsyx"
EMAIL_USE_TLS = True
