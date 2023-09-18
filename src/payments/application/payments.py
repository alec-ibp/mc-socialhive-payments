from __future__ import annotations

from src.payments.domain.models import Order, OrderStatus
from src.payments.domain.interfaces import AbstractUnitOfWork
from src.payments.domain.events import CreatePayment
from src.payments.application.messagebus import handler


def create_order(uow: AbstractUnitOfWork, order_request: Order) -> Order | None:
    with uow:
        order: Order = uow.payment.create_order(order=order_request)
        uow.commit()
    with uow:
        handler(CreatePayment(order.pk, order.total))
        # TODO update order status with uow
        return order


def complete_order(uow: AbstractUnitOfWork, order: Order) -> Order | None:
    with uow:
        uow.payment.update_status(order=order, status=OrderStatus.PENDING)
        uow.commit()
