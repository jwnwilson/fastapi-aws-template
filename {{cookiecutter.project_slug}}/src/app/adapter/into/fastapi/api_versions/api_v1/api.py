from fastapi import APIRouter

from .routes.healthcheck import router_v1 as healthcheck_router
from .routes.property import router_v1 as property_router

api_router_v1 = APIRouter()

api_router_v1.include_router(
    healthcheck_router,
    tags=["Healthcheck"],
    prefix="/heathcheck",
)
api_router_v1.include_router(
    property_router,
    tags=["Property"],
    prefix="/property",
)
