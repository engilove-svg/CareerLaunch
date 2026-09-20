from dataclasses import asdict
from datetime import datetime

from models import Application


VALID_STATUSES = [
    "Applied",
    "Interview",
    "Offer",
    "Rejected",
    "Withdrawn"
    "ToApply"
]

def validate_date(applied_date):
    try:
        datetime.strptime(applied_date, "%Y-%m-%d")
        return True
    except ValueError:
        return False
    
def get_next_id(applications):
    if not applications:
        return 1

    return max(app["id"] for app in applications) + 1


def create_application(
    applications,
    company,
    role,
    status,
    applied_date,
    notes
):
    if not company.strip():
        raise ValueError("Company name cannot be empty.")

    if not role.strip():
        raise ValueError("Job role cannot be empty.")

    if status not in VALID_STATUSES:
        raise ValueError("Invalid application status.")
    if not validate_date(applied_date):
        raise ValueError(
            "Invalid date. Use YYYY-MM-DD format."
    )

    application = Application(
        id=get_next_id(applications),
        company=company.strip(),
        role=role.strip(),
        status=status,
        applied_date=applied_date,
        notes=notes.strip()
    )

    return application

def application_to_dict(application):
    return asdict(application)
# It converts your Application object into a dictionary that json.dump() can save.

#Now, add a search function
def search_applications(applications, keyword):
    results = []

    for app in applications:
        if (
            keyword.lower() in app["company"].lower()
            or keyword.lower() in app["role"].lower()
        ):
            results.append(app)

    return results

def delete_application(applications, application_id):
    for index, app in enumerate(applications):
        if app["id"] == application_id:
            return applications.pop(index)

    return None

def update_application_status(
    applications,
    application_id,
    new_status
):
    # Validate the new status
    if new_status not in VALID_STATUSES:
        raise ValueError("Invalid application status.")

    # Find the application
    for app in applications:
        if app["id"] == application_id:
            app["status"] = new_status
            return app

    # Application not found
    return None

# analytics
def get_application_statistics(applications):
    statistics = {}

    for app in applications:
        status = app["status"]

        if status in statistics:
            statistics[status] += 1
        else:
            statistics[status] = 1

    return statistics

# Monthly application analytics

def get_monthly_statistics(applications):
    monthly_statistics = {}

    for app in applications:
        try:
            date = datetime.strptime(
                app["applied_date"],
                "%Y-%m-%d"
            )

            month = date.strftime("%B %Y")

            if month in monthly_statistics:
                monthly_statistics[month] += 1
            else:
                monthly_statistics[month] = 1

        except (ValueError, KeyError):
            print(
                f"Skipping invalid date for application ID "
                f"{app.get('id', 'Unknown')}"
            )

    return monthly_statistics

#The ID uniquely identifies the application, so we can edit the correct record.

def update_application(
    applications,
    application_id,
    company,
    role,
    notes
):
    for app in applications:
        if app["id"] == application_id:
            app["company"] = company.strip()
            app["role"] = role.strip()
            app["notes"] = notes.strip()

            return app

    return None