from models import Application
from models import Application
from repository import ApplicationRepository


repository = ApplicationRepository()

test_application = Application(
    id=0,
    company="Test Company",
    role="Test Developer",
    status="Applied",
    applied_date="2026-09-28",
    notes="Temporary test application"
)

repository.add(test_application)

print("Test application added!")