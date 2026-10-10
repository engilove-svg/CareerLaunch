from fastapi import FastAPI, HTTPException, Response
from repository import ApplicationRepository
from schemas import ApplicationCreate, ApplicationResponse, ApplicationUpdate


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

@app.get("/applications", response_model=list[ApplicationResponse])
def get_applications():
    applications = repository.get_all()
    return applications


@app.get("/applications/{application_id}", response_model=ApplicationResponse)
def get_application(application_id: int):
    application = repository.get_by_id(application_id)

    if application is None:
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )

    return application

@app.post(
    "/applications",
    response_model=ApplicationResponse,
    status_code=201
)
def create_application(application: ApplicationCreate):
    new_application = repository.add(application)
    return new_application

@app.delete("/applications/{application_id}", status_code=204)
def delete_application(application_id: int):
    application = repository.get_by_id(application_id)

    if application is None:
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )

    repository.delete(application_id)

    return Response(status_code=204)

@app.patch("/applications/{application_id}", response_model=ApplicationResponse)
def update_application(
    application_id: int,
    application_update: ApplicationUpdate
):
    application = repository.get_by_id(application_id)
    if application is None:
        raise HTTPException(
        status_code=404,
        detail="Application not found"
    )
    updates = application_update.model_dump(exclude_unset=True)

    application.update(updates)
    updated_application = repository.update(
        application_id,
        application
    )

    return updated_application