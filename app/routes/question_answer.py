from fastapi import APIRouter, HTTPException, Form
from app.utils.AWS_S3_utils import downloadPdfFromS3
from app.services.nlp_services import buildIndexFromDocuments, queryIndex
from app.utils.pdf_processing import extractTextFromPdf
from llama_index.core import Document
import os

router = APIRouter()

@router.post("/ask")
async def askQuestion(s3_key: str = Form(...), question: str = Form(...)):
    temp_directory = "temp"
    os.makedirs(temp_directory, exist_ok=True)
    local_path = os.path.join(temp_directory, os.path.basename(s3_key))

    try:
        downloadPdfFromS3(s3_key, local_path)
        text = extractTextFromPdf(local_path)
        documents = [Document(text=text)]

        index  = buildIndexFromDocuments(documents)
        answer = queryIndex(index, question)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if os.path.exists(local_path):
            os.remove(local_path)

    return {"question": question, "answer": answer}