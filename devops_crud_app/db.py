from sqlalchemy import create_engine

from devops_crud_app.consts import POSTGRES

engine = create_engine(
    f'postgresql+psycopg2://{POSTGRES["USER"]}:{POSTGRES["PASSWORD"]}@'
    f'{POSTGRES["HOST"]}:{POSTGRES["PORT"]}/{POSTGRES["DB"]}'
)
