from src.payments.domain.interfaces import AbstractRepository
from src.payments.domain.models import Order, OrderStatus


class PaymentRepository(AbstractRepository):
    def __init__(self, session) -> None:
        self.session = session

    def create_order(self, order: Order) -> Order:
        order.save()
        return order

    def update_status(self, order: Order, status: OrderStatus) -> None:
        order.status = status.value
        order.save()

    def get_payment_order(self, order_id: str) -> Order:
        return Order.get(order_id)
