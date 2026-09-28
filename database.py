
import psycopg


def get_connection():
    return psycopg.connect(
        host="localhost",
        dbname="careerlaunch",
        user="postgres",
        password="Khushasees12@",
        port=5432
    )

#"Give me all job applications stored in the database."
def get_applications():
    connection = get_connection()
    cursor = connection.cursor()
#A cursor is the object Python uses to send SQL commands to PostgreSQL.
    cursor.execute("SELECT * FROM applications")

    applications = cursor.fetchall()

    cursor.close()
    connection.close()

    return applications


if __name__ == "__main__":
    applications = get_applications()

    for application in applications:
        print(application)