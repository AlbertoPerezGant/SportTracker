from fastapi import APIRouter, UploadFile, File
from app.services.workouts import process_workouts

router = APIRouter()

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    results = process_workouts(content)
    return results
