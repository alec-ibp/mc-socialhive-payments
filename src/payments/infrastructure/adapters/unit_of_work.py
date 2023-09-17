from __future__ import annotations

from typing import Any

from src.payments.domain.models import Order
from src.payments.domain.interfaces import AbstractUnitOfWork
from src.payments.infrastructure.adapters.db import get_redis_session
from src.payments.infrastructure.adapters import repository


class RedisUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session: Any = None) -> None:
        if not session:
            self.session_factory = get_redis_session
        else:
            self.session_factory = session

    def __enter__(self):
        self.session = self.session_factory()
        Order._meta.database = self.session
        self.payment = repository.PaymentRepository(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def commit(self):
        return  # TODO check redis transaction
        self.session.commit()

    def rollback(self):
        return  # TODO check redis transaction
        self.session.rollback()
