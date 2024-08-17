from fastapi import Response, status
from fastapi import FastAPI
from app.routers import repositories

app = FastAPI()
app.include_router(repositories.router)


@app.get("/")
async def root():
    return Response(status_code=status.HTTP_418_IM_A_TEAPOT)
