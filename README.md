# PDF Question Answering Backend

This is a FastAPI backend that enables users to upload PDF documents, extract text from them, and ask questions using Google's Gemini LLM via the LlamaIndex framework. It uses AWS S3 for storage and Supabase (PostgreSQL) as the database.

---

## Tech Stack

- **FastAPI** – Backend web framework
- **AWS S3** – File storage
- **Supabase** – Database (PostgreSQL) and auth (optional)
- **LlamaIndex** – Indexing & querying PDFs
- **Gemini (Google Generative AI)** – LLM for question answering
- **Alembic** – Database migrations
- **Fitz (PyMuPDF)** – PDF text extraction
- **Boto3** – AWS SDK for Python
- **Databases** – Async database layer
- **Dotenv** – Environment config

---

## 📁 Project Structure

backend/
│
├── app/
│   ├── db/
│   │   ├── database.py          # Database connection setup using databases
│   │   └── models.py            # SQLAlchemy models for the documents table
│   │
│   ├── routes/
│   │   ├── upload_pdf.py        # Route for uploading PDF to S3 and saving metadata
│   │   └── question_answer.py   # Route for asking questions and getting answers from PDF
│   │
│   ├── services/
│   │   └── nlp_services.py      # LLM and embedding integration using Gemini via LangChain
│   │
│   ├── utils/
│   │   ├── AWS_S3_utils.py       # Upload/download helper functions for AWS S3
│   │   └── pdf_processing.py    # PDF text extraction using PyMuPDF (fitz)
│   │
│   └── main.py                  # FastAPI app initialization and route registration
│
├── temp/                        # Temporary directory for storing files before upload (auto-created)
├── .env                         # Environment variables (DATABASE_URL, AWS keys, Gemini API key, etc.)
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation (you’re reading it!)


---

## ⚙️ Environment Variables

Create a `.env` file in the `backend/` directory:

# Database
DATABASE_URL=postgresql://username:password@host:port/dbname

# AWS
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_REGION=your_aws_region
S3_BUCKET_NAME=your_s3_bucket


GOOGLE_API_KEY=your_google_api_key

# API Endpoints

UPLOAD PDF
POST: /pdf/upload
Formdata: file: PDF file

ASK AUESTION
POST: /question_answer/ask
Formdata: s3_key, question

Clone repository

git clone 
cd backend

Create virtual environment
python -m venv venv
source venv/bin/activate // for windows venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload

Alembic migrations

alembic init alembic
alembic revision --autogenerate -m "create documents table"
alembic upgrade head

