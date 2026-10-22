from fastapi import APIRouter

router = APIRouter(
    prefix="/api/tasks"
)

front_router = APIRouter(
    prefix="/tasks"
)

@router.get("/")
async def list_tasks():
    pass