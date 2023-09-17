from src.payments.domain.interfaces import AbstractUnitOfWork


def create_order(uow: AbstractUnitOfWork, product_id: int, quantity: int):
    with uow:
        order = uow.payment.create_order(product_id, quantity)
        uow.commit()
        return order
