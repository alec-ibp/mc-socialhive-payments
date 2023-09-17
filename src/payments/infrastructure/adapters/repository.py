import requests

from fastapi import status
from fastapi.exceptions import HTTPException  # should be generic exception and handled in the application layer

from src.payments.domain.interfaces import AbstractRepository
from src.payments.domain.models import Order, Product


class PaymentRepository(AbstractRepository):
    def __init__(self, session) -> None:
        self.session = session

    def create_order(self, product_id: int, quantity: float) -> Order:
        response = requests.get(f"http://0.0.0.0:8080/marketplace/products/{product_id}/details")
        if response.status_code != status.HTTP_200_OK:
            raise HTTPException(status_code=response.status_code, detail=str(response.content))

        product: Product | None = Product.parse_obj(response.json())

        if product.quantity <= quantity:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not enough products in stock")

        order: Order = Order(
            product_id=product.pk,
            price=product.price,
            fee=0.2 * product.price,
            total=1.2 * product.price
        )
        order.save()
        return order
