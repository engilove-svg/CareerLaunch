
import psycopg


def get_connection():
    return psycopg.connect(
        host="localhost",
        dbname="careerlaunch",
        user="postgres",
        password="pswd",
        port=5432
    )


def get_applications():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM applications")

    applications = cursor.fetchall()

    cursor.close()
    connection.close()

    return applications


if __name__ == "__main__":
    applications = get_applications()

    for application in applications:
        print(application)