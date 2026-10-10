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

class ApplicationUpdate(BaseModel):
    company_name: str | None = None
    job_title: str | None = None
    status: str | None = None
    application_date: date | None = None
    notes: str | None = None