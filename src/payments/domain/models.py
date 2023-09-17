from enum import Enum

from pydantic import BaseModel
from redis_om.model import HashModel


class OrderStatus(str, Enum):
    CREATED = "created"
    PAID = "paid"
    CANCELED = "canceled"
    REFUNDED = "refunded"


class Order(HashModel):
    product_id: str
    price: float
    fee: float
    total: float
    status: OrderStatus = OrderStatus.CREATED


class OrderRequest(BaseModel):
    id: str
    quantity: int


class Product(HashModel):
    price: float
    quantity: int
