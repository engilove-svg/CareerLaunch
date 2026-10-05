from models import Application
from repository import ApplicationRepository
from services import ApplicationService


repository = ApplicationRepository()
service = ApplicationService(repository)


application = Application(
    id=0,
    company="Test Service Company",
    role="Junior Developer",
    status="Applied",
    applied_date="2026-09-28",
    notes="Testing service layer"
)

service.add_application(application)

print("Application added through service!")