from fastapi import FastAPI
from router.employee_router import router

app = FastAPI()
app.include_router(router)