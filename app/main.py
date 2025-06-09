from fastapi import FastAPI
from app.db.database import database
from app.routes.upload_pdf import router as upload_router
from app.routes.question_answer import router as qa_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="PDF Q&A App")

# Allow frontend origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000","http://localhost:5173", "https://pdfchatbott.netlify.app", "https://pdf-question-answer-frontend.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router, prefix="/pdf", tags=["Upload"])
app.include_router(qa_router, prefix="/question_answer", tags=["Question Answering"])

@app.get("/")
async def root():
    return {"message": "Welcome to AI Planet backend!"}

@app.on_event("startup")
async def on_startup():
    await database.connect()

@app.on_event("shutdown")
async def on_shutdown():
    await database.disconnect()
