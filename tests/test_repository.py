from models import Application
from repository import ApplicationRepository


repository = ApplicationRepository()

application = Application(
    id=0,
    company="OLG",
    role="Customer Care Specialist",
    status="Applied",
    applied_date="2026-09-28",
    notes="Applied through OLG careers"
)

repository.add(application)

print("Application added successfully!")