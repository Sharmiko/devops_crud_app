from sqlalchemy import insert, select, delete

from devops_crud_app.orders.schemas import OrderSchema
from devops_crud_app.orders.models import orders
from devops_crud_app.db import engine


def insert_order(data: OrderSchema) -> int:
    connection = engine.connect()
    try:
        ins = insert(orders)
        result = connection.execute(ins, **data.dict())
        return result.inserted_primary_key[0]
    finally:
        connection.close()


def list_orders() -> list:
    connection = engine.connect()
    try:
        sel = select(orders)
        cursor = connection.execute(sel)
        return cursor.fetchall()
    finally:
        connection.close()


def get_order(order_id: int) -> dict:
    connection = engine.connect()
    try:
        sel = select(orders).where(orders.c.order_id == order_id)
        cursor = connection.execute(sel)
        item = cursor.first()
        if item:
            return item.items()
    finally:
        connection.close()


def delete_order(order_id: int) -> bool:
    connection = engine.connect()
    try:
        delete_sql = delete(orders).where(orders.c.order_id == order_id)
        cursor = connection.execute(delete_sql)
        return bool(cursor.rowcount)
    finally:
        connection.close()
