from datetime import datetime
import enum
import uuid
from pydantic import BaseModel, Field, field_validator


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
    quantity: int | None = Field(default=1, ge=1)

    @field_validator("quantity")
    def quantity_not_sero(cls, value: int | None):
        assert value != 0
        return value

    class Config:
        extra = 'forbid'


class CreateOrderSchema(BaseModel):
    order: list[OrderItemSchema] = Field(..., min_length=1)
    
    class Config:
        extra = 'forbid'


class GetOrderSchema(CreateOrderSchema):
    id: uuid.UUID
    created: datetime
    status: OrderStatus


class GetOrdersSchema(BaseModel):
    orders: list[GetOrderSchema]
