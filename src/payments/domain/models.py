from enum import Enum

from redis_om.model import HashModel


class OrderStatus(str, Enum):
    CREATED = "created"
    PENDING = "pending"
    COMPLETED = "completed"
    CANCELED = "canceled"
    REFUNDED = "refunded"


class Order(HashModel):
    product_id: str
    price: float
    fee: float
    total: float
    status: OrderStatus = OrderStatus.CREATED
