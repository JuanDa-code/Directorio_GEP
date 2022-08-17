import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_directorio',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        "OPTIONS": {
            'init_command': "SET sql_mode='STRICT_ALL_TABLES', innodb_strict_mode=1",
            'charset': 'utf8mb4',
            "autocommit": True,
        },
    }
}