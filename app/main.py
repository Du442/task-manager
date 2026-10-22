from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles

from app.routes.tasks import *

app = FastAPI(
    title="Task Manager",
    description="API to register, search, update and delete tasks."
)

app.include_router(router)
app.include_router(front_router)

templates = Jinja2Templates(directory="templates")

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context={"message": "access /tasks route! :)"})