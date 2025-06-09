from fastapi import APIRouter, UploadFile,File, HTTPException
from app.utils.AWS_S3_utils import uploadPdfToS3
from app.db.models import documents
from app.db.database import database
from datetime import datetime
import uuid
import os

router = APIRouter()

@router.post("/upload")
async def uploadPdf(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only pdf files are allowed")

    # os.remove(temp_path)
    temp_directory = "temp"
    os.makedirs(temp_directory, exist_ok=True)

    # Generate unique filename
    unique_id = str(uuid.uuid4())
    unique_filename = f"{unique_id}_{file.filename}"
    temp_path = os.path.join(temp_directory, unique_filename)

    with open(temp_path, "wb") as f:
        f.write(await file.read())

    s3_key = f"pdfs/{unique_filename}"
    s3_url = uploadPdfToS3(temp_path, s3_key)

    os.remove(temp_path)

    query  = documents.insert().values(
        filename = file.filename,
        s3_key = s3_key,
        uploaded_at = datetime.utcnow()
    )
    await database.execute(query)

    return {"message": "uploaded successfully", "s3_url": s3_url}
