from datetime import datetime
import uuid

from fastapi.responses import Response
from fastapi import status, APIRouter, HTTPException

from orders.api.schemas import CreateOrderSchema, GetOrderSchema, GetOrdersSchema


app = APIRouter()

order = {
        'id': uuid.uuid4(),
        'status': 'delivered',
        'created': datetime.utcnow(),
        'order': [
            {
                'product': 'cappuccino',
                'size': 'medium',
                'quantity': 1
            }
        ]
}

ORDERS = []


@app.get('/orders', response_model=GetOrdersSchema)
def get_orders():
    return ORDERS

@app.post('/orders', status_code=status.HTTP_201_CREATED)
def create_order(order_details: CreateOrderSchema):
    order = order_details.model_dump()
    order['id'] = uuid.uuid4()
    order['created'] = datetime.now()
    order['status'] = 'created'
    ORDERS.append(order)
    return order

@app.get('/orders/{order_id}', response_model=GetOrderSchema)
def get_order(order_id: uuid.UUID):
    for order in ORDERS:
        if order['id'] == order_id:
            return order
    raise HTTPException(
        status_code=404, detail=f'Order with id {order_id} not found'
    )

@app.put('/orders/{order_id}')
def update_order(order_id: uuid.UUID, order_details: CreateOrderSchema):
    for order in ORDERS:
        if order['id'] == order_id:
            order.update(order_details.model_dump())
            return order
    raise HTTPException(
        status_code=404, detail=f'Order with id {order_id} not found'
    )

@app.delete('/orders/{order_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_order(order_id: uuid.UUID):
    for index, order in enumerate(ORDERS):
        if order['id'] == order_id:
            ORDERS.pop(index)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(
        status_code=404, detail=f'Order with id {order_id} not found'
    )

@app.post('/orders/{order_id}/cancel')
def cancel_order(order_id: uuid.UUID):
    for order in ORDERS:
        if order['id'] == order_id:
            order['status'] = 'cancelled'
            return order
    raise HTTPException(
        status_code=404, detail=f'Order with id {order_id} not found'
    )

@app.post('/orders/{order_id}/pay')
def pay_order(order_id: uuid.UUID):
    for order in ORDERS:
        if order['id'] == order_id:
            order['status'] = 'progress'
            return order
    raise HTTPException(
        status_code=404, detail=f'Order with id {order_id} not found'
    )

