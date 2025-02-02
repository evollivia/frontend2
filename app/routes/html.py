from fastapi import APIRouter, Request, Form
from starlette.templating import Jinja2Templates

# 라우터생성
html_router = APIRouter()
# 템플릿 지정
templates = Jinja2Templates(directory='views/templates')


# 라우터 설정
@html_router.get('/')
async def index(req: Request):
    return templates.TemplateResponse('html/index.html', {'request': req})


@html_router.get('/layout')
async def layout(req: Request):
    return templates.TemplateResponse('html/01layout.html', {'request': req})


@html_router.get('/text')
async def text(req: Request):
    return templates.TemplateResponse('html/02text.html', {'request': req})


@html_router.get('/link')
async def link(req: Request):
    return templates.TemplateResponse('html/03link.html', {'request': req})


@html_router.get('/list')
async def list(req: Request):
    return templates.TemplateResponse('html/04list.html', {'request': req})


@html_router.get('/table')
async def table(req: Request):
    return templates.TemplateResponse('html/05table.html', {'request': req})


@html_router.get('/image')
async def image(req: Request):
    return templates.TemplateResponse('html/06image.html', {'request': req})


@html_router.get('/form')
async def form(req: Request):
    return templates.TemplateResponse('html/07form.html', {'request': req})


@html_router.post('/formproc')
async def formok(req: Request, userid: str = Form(...), passwd: str = Form(...)):
    print(f'회원 가입 정보가 서버로 전송됨 : {userid} {passwd}')
    return templates.TemplateResponse('html/07form.html', {'request': req})


@html_router.get('/joinfrm')
async def joinfrm(req: Request):
    return templates.TemplateResponse('html/08joinfrm.html', {'request': req})


@html_router.get('/semantic')
async def semantic(req: Request):
    return templates.TemplateResponse('html/09semantic.html', {'request': req})


@html_router.get('/project1')
async def semantic(req: Request):
    return templates.TemplateResponse('html/10project1.html', {'request': req})
