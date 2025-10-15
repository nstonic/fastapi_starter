import uvicorn
from fastapi import FastAPI

from apps import hellow_world_app

main_app = FastAPI()
main_app.mount("/", hellow_world_app)

if __name__ == '__main__':
    uvicorn.run(main_app, host="0.0.0.0", port=8000)
