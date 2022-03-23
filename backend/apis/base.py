from fastapi import APIRouter

from apis.version1 import route_campaigns


api_router =  APIRouter()

api_router.include_router(route_campaigns.router, prefix="/campaign", tags=["campaigns"])