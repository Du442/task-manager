from fastapi import FastAPI

app = FastAPI(
    title="Task Manager",
    description="API to register, search, update and delete tasks."
)

@app.get("/")
def index():
    return {"message": "Hello world!"}