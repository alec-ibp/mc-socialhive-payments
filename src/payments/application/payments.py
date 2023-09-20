from __future__ import annotations

from src.payments.domain.models import Order, OrderStatus
from src.payments.domain.interfaces import AbstractUnitOfWork
from src.payments.domain.events import CreatePayment
from src.payments.application.messagebus import handler


def create_order(uow: AbstractUnitOfWork, order_request: Order) -> Order | None:
    with uow:
        order: Order = uow.payment.create_order(order=order_request)
        uow.commit()
        return order


def charge_order(uow: AbstractUnitOfWork, order: Order) -> None:
    with uow:
        uow.payment.update_status(order=order, status=OrderStatus.PENDING)
        uow.commit()

    handler(CreatePayment(order.pk, order.total))

    with uow:
        uow.payment.update_status(order=order, status=OrderStatus.COMPLETED)
        uow.commit()


def get_payment_order(uow: AbstractUnitOfWork, order_id: str) -> Order:
    with uow:
        return uow.payment.get_payment_order(order_id)
