from src.payments.domain.interfaces import AbstractRepository
from src.payments.domain.models import Order


class PaymentRepository(AbstractRepository):
    def __init__(self, session) -> None:
        self.session = session

    def create_order(self, order: Order) -> Order:
        # order.save() TODO restore when rds is implemented
        return order
