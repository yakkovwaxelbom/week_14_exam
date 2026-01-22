from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn

from core.mysql_db import SQLManager
from core.handle_errors import register_error_handlers
from routes.upload_route import route as upload_route



@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLManager.connect()
    SQLManager.bad_init()
    yield 
    SQLManager.close()



app = FastAPI(lifespan=lifespan)
register_error_handlers(app)
app.include_router(upload_route)


# if __name__ == '__main__':
#     uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
