from fastapi import FastAPI
from mangum import Mangum
from MyApp.api.routers import router

__all__ = ["api"]

api = FastAPI(
    title="FastAPI-Lambda-Docker",
    description="An example API deployed to AWS lambda in a docker container",
)
api.include_router(router=router)

handler = Mangum(app=api)
