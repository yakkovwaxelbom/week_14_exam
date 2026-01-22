from fastapi import Request
from fastapi.responses import JSONResponse
from core.errors import MySQLGeneralError
from fastapi import FastAPI


def register_error_handlers(app: FastAPI):

    @app.exception_handler(MySQLGeneralError)
    def mysql_error_handler(request: Request, exe: MySQLGeneralError):
        return JSONResponse(status_code=500, content={'massage': exe.msg})

