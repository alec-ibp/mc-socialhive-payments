from dataclasses import dataclass, asdict


@dataclass
class Event:
    pass


@dataclass
class CreatePayment(Event):
    order_id: str
    price: int


@dataclass
class CompletedPayment(Event):
    pk: str
    product_id: str
    price: float
    fee: float
    total: float
    status: str

    def dict(self):
        return asdict(self)
