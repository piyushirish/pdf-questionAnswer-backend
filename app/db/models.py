from sqlalchemy import DateTime, MetaData, String, Integer, Table, Column
from datetime import datetime

metadata = MetaData()

documents = Table(
    "documents",
    metadata,
    Column("id", Integer, primary_key = True),
    Column("filename", String, nullable = False),
    Column("s3_key", String, unique = True, nullable=False),
    Column("uploaded_at", DateTime, default=datetime.utcnow),

)