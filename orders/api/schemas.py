from datetime import datetime
import enum
import uuid
from pydantic import BaseModel, Field


class CoffeeSize(enum.Enum):
    small = "small"
    medium = "medium"
    big = "big"


class OrderStatus(enum.Enum):
    created = "created"
    progress = "progress"
    cancelled = "cancelled"
    dispatched = "dispatched"
    delivered = "delivered"


class OrderItemSchema(BaseModel):
    product: str
    size: CoffeeSize
    quantity: int = Field(default=1, ge=1)


class CreateOrderSchema(BaseModel):
    order: list[OrderItemSchema] = Field(..., min_length=1)


class GetOrderSchema(CreateOrderSchema):
    id: uuid.UUID
    created: datetime
    status: OrderStatus


class GetOrdersSchema(BaseModel):
    orders: list[GetOrderSchema]
