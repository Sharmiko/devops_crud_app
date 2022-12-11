from datetime import datetime

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from devops_crud_app.orders import crud
from devops_crud_app.orders import messages
from devops_crud_app.orders.schemas import OrderSchema
from devops_crud_app.utils import render_response_example


router = APIRouter(prefix='/orders', tags=['orders'])


@router.post(
    path='/',
    description='Save order information',
    responses={
        200: render_response_example({
            'message': 'success',
            'inserted_order_key': 3
        })
    }
)
def insert_order(data: OrderSchema) -> JSONResponse:
    inserted_id = crud.insert_order(data=data)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'message': 'success',
            'inserted_order_key': inserted_id
        }
    )


@router.get(
    path='/',
    description='List all orders',
    responses={
        200: render_response_example({
            'orders': [
                {
                    "order_id": 4,
                    "name": "Burger",
                    "quantity": 2,
                    "total_price": 37.5,
                    "order_datetime": "2022-11-12 13:13:26"
                },
                {
                    "order_id": 5,
                    "name": "Red Wine",
                    "quantity": 1,
                    "total_price": 80,
                    "order_datetime": "2022-11-12 13:13:26"
                },
            ]
        })
    }
)
def list_orders() -> JSONResponse:

    result = []
    for row in crud.list_orders():
        temp = {}
        for key, value in row.items():
            if isinstance(value, datetime):
                value = value.strftime('%Y-%d-%m %H:%M:%S')
            temp[key] = value
        result.append(temp)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'orders': result
        }
    )


@router.get(
    path='/item/{item_id}',
    description='Get specific order using order id',
    responses={
        200: render_response_example({
            "order_id": 10,
            "name": "test",
            "quantity": 1,
            "total_price": 1,
            "order_datetime": "2022-11-12 13:20:51"
        }),
        400: render_response_example({
            'message': messages.ORDER_WITH_PROVIDED_ID_WAS_NOT_FOUND
        })
    }
)
def get_order(item_id: int) -> JSONResponse:

    details = {}
    item = crud.get_order(order_id=item_id)
    if not item:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                'message': messages.ORDER_WITH_PROVIDED_ID_WAS_NOT_FOUND
            }
        )

    for k, v in item:
        if isinstance(v, datetime):
            v = v.strftime('%Y-%d-%m %H:%M:%S')
        details[k] = v

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=details
    )


@router.delete(
    path='/item/{item_id}',
    description='Delete specific order using order id',
    responses={
        200: render_response_example({
            'message': 'success'
        }),
        400: render_response_example({
            'message': messages.ORDER_WITH_PROVIDED_ID_WAS_NOT_FOUND
        })
    }
)
def get_order(item_id: int) -> JSONResponse:

    deleted = crud.delete_order(order_id=item_id)
    if not deleted:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                'message': messages.ORDER_WITH_PROVIDED_ID_WAS_NOT_FOUND
            }
        )

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'message': 'success'
        }
    )
