from datetime import datetime
import uuid

from fastapi.responses import Response
from fastapi import status, APIRouter


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

@app.get('/orders')
def get_orders():
    return {'orders': [order]}

@app.post('/orders', status_code=status.HTTP_201_CREATED)
def create_order():
    return order

@app.get('/orders/{order_id}')
def get_order(order_id: uuid.UUID):
    return order

@app.put('/orders/{order_id}')
def update_order(order_id: uuid.UUID):
    return order

@app.delete('/orders/{order_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_order(order_id: uuid.UUID):
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.post('/orders/{order_id}/cancel')
def cancel_order(order_id: uuid.UUID):
    return order

@app.post('/orders/{order_id}/pay')
def pay_order(order_id: uuid.UUID):
    return order

