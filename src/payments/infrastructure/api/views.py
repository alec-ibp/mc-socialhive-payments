from __future__ import annotations

from fastapi import APIRouter, status, BackgroundTasks

from src.payments.application.payments import create_order, charge_order, get_payment_order
from src.payments.domain.models import Order
from src.payments.infrastructure.adapters.unit_of_work import RedisUnitOfWork


router: APIRouter = APIRouter()


@router.post(
    path="/",
    status_code=status.HTTP_201_CREATED,
    response_model=Order,
)
async def create_payment(order: Order, background_tasks: BackgroundTasks) -> Order:
    new_order: Order = create_order(RedisUnitOfWork(), order)
    background_tasks.add_task(charge_order, RedisUnitOfWork(), new_order)
    return new_order


@router.get(
    path="/{order_id}",
    status_code=status.HTTP_200_OK,
    response_model=Order,
)
async def get_order(order_id: str) -> Order:
    return get_payment_order(RedisUnitOfWork(), order_id)
