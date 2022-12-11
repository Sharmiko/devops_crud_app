import os


POSTGRES = {
    'HOST': os.getenv('POSTGRES_HOST', 'localhost'),
    'USER': os.getenv('POSTGRES_USER', 'postgres'),
    'PASSWORD': os.getenv('POSTGRES_PASSWORD', None),
    'DB': os.getenv('POSTGRES_DB', 'devops_crud')
}
