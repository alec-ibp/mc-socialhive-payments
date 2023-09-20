from typing import Any

from src.payments.domain.events import Event, CreatePayment


def handler(event: Event, by_batch: bool = False):
    if by_batch:
        for handler in HANDLERS[type(event)]:
            handler(event)
    else:
        return HANDLERS[type(event)](event)


def create_payment_event(event: CreatePayment) -> Any:
    print("Sending charge payment event")
    # just mocking a delay
    import time
    time.sleep(5)
    return event


HANDLERS: dict[Event, callable] = {
    CreatePayment: create_payment_event
}
