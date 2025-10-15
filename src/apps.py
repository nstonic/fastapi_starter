from fastapi import FastAPI
from starlette.responses import PlainTextResponse

hellow_world_app = FastAPI()


@hellow_world_app.get("/")
async def hello() -> PlainTextResponse:
    return PlainTextResponse("Hello world!")
