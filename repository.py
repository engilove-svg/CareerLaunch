import psycopg


DATABASE_URL = "your_postgresql_connection_string"


def get_connection():
    return psycopg.connect(DATABASE_URL)


def add_application(application):
    with get_connection() as connection:
        with connection.cursor() as cursor:
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
                """,
                (
                    application.company,
                    application.role,
                    application.status,
                    application.notes,
                    application.applied_date,
                )
            )

        connection.commit()


def get_all_applications():
    with get_connection() as connection:
        with connection.cursor() as cursor:
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

            return cursor.fetchall()