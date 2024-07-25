from fastapi import APIRouter, Request, Form
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

# 라우터생성
sungjuk_router = APIRouter()
# 템플릿 지정
templates = Jinja2Templates(directory='views/templates')


# 라우터 설정
@sungjuk_router.get('/', response_class=HTMLResponse)
async def sungjuk(req: Request):
    return templates.TemplateResponse('sungjuk/sungjuk.html', {'request': req})


@sungjuk_router.post('/', response_class=HTMLResponse)
async def sungjuk(req: Request,
                  name: str = Form(...), korean: int = Form(...),
                  english: int = Form(...), math: int = Form(...)):
    print(name, korean, english, math)
    total = korean + english + math
    average = total / 3
    grade = '가'
    if average >= 90:
        grade = '수'
    elif average >= 80:
        grade = '우'
    elif average >= 70:
        grade = '미'
    elif average >= 60:
        grade = '양'
    return templates.TemplateResponse('sungjuk/result.html',
                                      {'name': name, 'korean': korean, 'english': english, 'math': math,
                                       'total': total, 'average': average, 'grade': grade, 'request': req})
