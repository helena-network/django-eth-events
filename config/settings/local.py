from .base import *

SECRET_KEY = 'localkey'
DEBUG = True

ETHEREUM_NODE_URL = 'http://localhost:8545'
ETHEREUM_MAX_WORKERS = 5

RABBIT_HOSTNAME = 'rabbit'
RABBIT_USER = 'gnosisdb'
RABBIT_PASSWORD = 'gnosisdb'
RABBIT_PORT = '5672'
BROKER_URL = 'amqp://{user}:{password}@{hostname}:{port}'.format(
    user=RABBIT_USER,
    password=RABBIT_PASSWORD,
    hostname=RABBIT_HOSTNAME,
    port=RABBIT_PORT
)

# IPFS
IPFS_HOST = 'http://ipfs'  # 'ipfs'
IPFS_PORT = 5001


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
    }
}
