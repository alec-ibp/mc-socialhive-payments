from __future__ import annotations

from abc import ABC, abstractmethod

from .models import Order


class AbstractRepository(ABC):
    @abstractmethod
    def create_order(self, order: Order) -> None:
        raise NotImplementedError


class AbstractUnitOfWork(ABC):
    payment: AbstractRepository

    def __enter__(self) -> AbstractUnitOfWork:
        return self

    def __exit__(self, *args) -> None:
        self.rollback()

    @abstractmethod
    def commit(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def rollback(self) -> None:
        raise NotImplementedError
