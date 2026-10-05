from datetime import date
from pydantic import BaseModel


class ApplicationResponse(BaseModel):
    id: int
    company_name: str
    job_title: str
    status: str
    application_date: date
    notes: str | None = None

class ApplicationCreate(BaseModel):
    company_name: str
    job_title: str
    status: str
    application_date: date
    notes: str | None = None