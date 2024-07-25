from fastapi import APIRouter
from starlette.templating import Jinja2Templates

# 라우터생성
css_router = APIRouter()
# 템플릿 지정
templates = Jinja2Templates(directory='views/templates')

# 라우터 설정