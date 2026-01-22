from fastapi import routing, File, UploadFile, HTTPException, Depends

from services.handle_requests import HandleRequests
from core.mysql_db import get_cursor

route = routing.APIRouter()


@route.post('/upload', status_code=201)
def create_terrorist(file: UploadFile = File(...), cursor = Depends(get_cursor)):
    
    if not file.filename.lower().endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are allowed")
    
    count = HandleRequests(cursor).handle_upload(file)

    return {
        "status": "success",
        "inserted_records": count
        }
        