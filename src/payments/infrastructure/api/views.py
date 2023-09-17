from __future__ import annotations

from fastapi import APIRouter, status

from src.payments.application.payments import create_order
from src.payments.domain.models import Order, OrderRequest
from src.payments.infrastructure.adapters.unit_of_work import RedisUnitOfWork


router: APIRouter = APIRouter()


@router.post(
    path="/",
    status_code=status.HTTP_201_CREATED,
    response_model=Order,
)
async def create_payment(order: OrderRequest) -> Order:
    new_order: Order = create_order(RedisUnitOfWork(), order.id, order.quantity)
    return new_order
