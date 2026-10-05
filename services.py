from models import Application
from repository import ApplicationRepository


class ApplicationService:

    def __init__(self, repository):
        self.repository = repository

    def add_application(self, application):
        self.repository.add(application)

    def get_all_applications(self):
        return self.repository.get_all()

    def get_application(self, application_id):
        return self.repository.get_by_id(application_id)

    def update_application(self, application_id, application):
        return self.repository.update(application_id, application)

    def delete_application(self, application_id):
        return self.repository.delete(application_id)