from fastapi import Request, APIRouter
from database.postservice import *

hashtag_router = APIRouter(prefix="/hashtag", tags=["Управление хештегами"])

# @hashtag_router.post()