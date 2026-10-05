from fastapi import FastAPI, HTTPException
from repository import ApplicationRepository


app = FastAPI(
    title="CareerLaunch API",
    description="Job Application Tracker API",
    version="1.0.0"
)


repository = ApplicationRepository()


@app.get("/")
def home():
    return {
        "message": "Welcome to CareerLaunch API"
    }


@app.get("/applications")
def get_applications():
    applications = repository.get_all()
    return applications


@app.get("/applications/{application_id}")
def get_application(application_id: int):
    application = repository.get_by_id(application_id)

    if application is None:
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )

    return application
