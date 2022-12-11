from datetime import datetime

from sqlalchemy import Table, Column, String, Integer, Float, DateTime

from devops_crud_app.metadata import metadata
from devops_crud_app.db import engine


orders = Table('orders', metadata,
               Column('order_id', Integer(), primary_key=True),
               Column('name', String(50)),
               Column('quantity', Integer()),
               Column('total_price', Float()),
               Column('order_datetime', DateTime(), default=datetime.utcnow)
               )


metadata.create_all(engine)
