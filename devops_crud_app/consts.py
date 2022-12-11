import os


POSTGRES = {
    'HOST': os.getenv('POSTGRES_HOST', 'localhost'),
    'PORT': os.getenv('POSTGRES_PORT', 5432),
    'USER': os.getenv('POSTGRES_USER', 'postgres'),
    'PASSWORD': os.getenv('POSTGRES_PASSWORD', None),
    'DB': os.getenv('POSTGRES_DB', 'devops_crud')
}
