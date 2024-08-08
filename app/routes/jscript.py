from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates

# 라우터생성
jscript_router = APIRouter()
# 템플릿 지정
templates = Jinja2Templates(directory='views/templates')


# 라우터 설정
@jscript_router.get('/')
async def index(req: Request):
    return templates.TemplateResponse('js/index.html', {'request': req})


@jscript_router.get('/hello')
async def hello(req: Request):
    return templates.TemplateResponse('js/01hello.html', {'request': req})


@jscript_router.get('/type')
async def type(req: Request):
    return templates.TemplateResponse('js/02type.html', {'request': req})


@jscript_router.get('/operator')
async def operator(req: Request):
    return templates.TemplateResponse('js/03operator.html', {'request': req})


@jscript_router.get('/condition')
async def condition(req: Request):
    return templates.TemplateResponse('js/04condition.html', {'request': req})


@jscript_router.get('/loop')
async def loop(req: Request):
    return templates.TemplateResponse('js/05loop.html', {'request': req})


@jscript_router.get('/array')
async def array(req: Request):
    return templates.TemplateResponse('js/06array.html', {'request': req})


@jscript_router.get('/while')
async def loopwhile(req: Request):
    return templates.TemplateResponse('js/07while.html', {'request': req})


@jscript_router.get('/function')
async def function(req: Request):
    return templates.TemplateResponse('js/08function.html', {'request': req})


@jscript_router.get('/callback')
async def callback(req: Request):
    return templates.TemplateResponse('js/09callback.html', {'request': req})


@jscript_router.get('/except')
async def exceptional(req: Request):
    return templates.TemplateResponse('js/10except.html', {'request': req})


@jscript_router.get('/bom')
async def bom(req: Request):
    return templates.TemplateResponse('js/11bom.html', {'request': req})


@jscript_router.get('/dom')
async def dom(req: Request):
    return templates.TemplateResponse('js/12dom.html', {'request': req})
