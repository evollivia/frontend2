from fastapi import APIRouter, Request, Form
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from app.schema.EMP import Employee

# 라우터생성
emp_router = APIRouter()
# 템플릿 지정
templates = Jinja2Templates(directory='views/templates')


@emp_router.get('/', response_class=HTMLResponse)
async def emp(req: Request):
    return templates.TemplateResponse('emp/emp.html', {'request': req})


@emp_router.post('/', response_class=HTMLResponse)
async def emp(req: Request, empid: str = Form(...), fname: str = Form(...), lname: str = Form(...),
              email: str = Form(...), phone: str = Form(...), hdate: str = Form(...),
              jobid: str = Form(...), sal: int = Form(...), comm: int = Form(...),
              mgrid: int = Form(...), deptid: str = Form(...)):
    print(empid, fname, lname, email, phone, hdate, jobid, sal, comm, mgrid, deptid)
    emps = Employee(empid=empid, fname=fname, lname=lname,
                    email=email, phone=phone, hdate=hdate, jobid=jobid,
                    sal=sal, comm=comm, mgrid=mgrid, deptid=deptid)
    return templates.TemplateResponse('emp/result.html', {'emp': emps, 'request': req})
