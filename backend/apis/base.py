from fastapi import APIRouter

from apis.version1 import route_campaigns
#from apis.version1 import route_costs
 

api_router = APIRouter()


api_router.include_router(route_campaigns.router, prefix="/campaigns",tags=["campaigns"])
