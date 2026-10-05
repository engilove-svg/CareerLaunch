import psycopg
from psycopg.rows import dict_row

DATABASE_URL = "postgresql://postgres:Khushasees12@@localhost:5432/careerlaunch"


def get_connection():
    return psycopg.connect(
        host="localhost",
        port=5432,
        dbname="careerlaunch",
        user="postgres",
        password="Khushasees12@"
    )


class ApplicationRepository:

    def add(self, application):
        with get_connection() as connection:
            with connection.cursor(row_factory=dict_row) as cursor:#A cursor is the object we use to execute SQL commands.
                cursor.execute(
                    """
                    INSERT INTO applications
                    (
                        company_name,
                        job_title,
                        status,
                        notes,
                        application_date
                    )
                    VALUES (%s, %s, %s, %s, %s)
                    RETURNING
                        id,
                        company_name,
                        job_title,
                        status,
                        notes,
                        application_date
                    """,
                    (
                        application.company_name,
                        application.job_title,
                        application.status,
                        application.notes,
                        application.application_date,
                    )
                )
                new_application= cursor.fetchone()
            connection.commit()

            return new_application

    def get_all(self):
        with get_connection() as connection:
            with connection.cursor(row_factory=dict_row) as cursor:
                cursor.execute(
                    """
                    SELECT
                        id,
                        company_name,
                        job_title,
                        status,
                        notes,
                        application_date
                    FROM applications
                    ORDER BY id
                    """
                )

                return cursor.fetchall()#all rows
    def get_by_id(self, application_id):
        with get_connection() as connection:
            with connection.cursor(row_factory=dict_row) as cursor:
                cursor.execute(
                    """
                    SELECT
                        id,
                        company_name,
                        job_title,
                        status,
                        notes,
                        application_date
                    FROM applications
                    WHERE id = %s
                    """,
                    (application_id,)
                )

                return cursor.fetchone()# one row

    def update(self, application_id, application):
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    UPDATE applications
                    SET
                        company_name = %s,
                        job_title = %s,
                        status = %s,
                        notes = %s,
                        application_date = %s
                    WHERE id = %s
                    """,
                    (
                        application.company,
                        application.role,
                        application.status,
                        application.notes,
                        application.applied_date,
                        application_id,
                    )
                )

            connection.commit()

    def delete(self, application_id):
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    DELETE FROM applications
                    WHERE id = %s
                    """,
                    (application_id,)
                )

            connection.commit()