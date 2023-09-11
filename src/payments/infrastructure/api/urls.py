from fastapi import APIRouter

from src.payments.infrastructure.api.views import router as marketplace_router


router: APIRouter = APIRouter()
router.include_router(marketplace_router, prefix="/payments", tags=["payments"])
