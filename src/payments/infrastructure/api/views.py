from __future__ import annotations

from fastapi import APIRouter, status

from src.payments.application.payments import create_order
from src.payments.domain.models import Order
from src.payments.infrastructure.adapters.unit_of_work import RedisUnitOfWork


router: APIRouter = APIRouter()


@router.post(
    path="/",
    status_code=status.HTTP_201_CREATED,
    response_model=Order,
)
async def create_payment(order: Order) -> Order:
    return create_order(RedisUnitOfWork(), order)
