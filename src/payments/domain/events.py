from dataclasses import dataclass


@dataclass
class Event:
    pass


@dataclass
class CreatePayment(Event):
    order_id: str
    price: int
