
from storage import load_applications, save_applications

from services import (
    create_application,
    application_to_dict,
    search_applications,
    delete_application,
    update_application_status,
    get_application_statistics,
    get_monthly_statistics,
    update_application
)


def main():
    applications = load_applications()

    while True:
        print("\nWelcome to CareerLaunch!")
        print("1. View applications")
        print("2. Add application")
        print("3. Search applications")
        print("4. Delete application")
        print("5. Update status")
        print("6. View statistics")
        print("7. View monthly statistics")
        print("8. Edit application")
        print("Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n-----Your Applications--------")

            if not applications:
                print("No applications found.")

            for app in applications:
                print(f"ID: {app['id']}")
                print(f"Company: {app['company']}")
                print(f"Role: {app['role']}")
                print(f"Status: {app['status']}")
                print(f"Date: {app['applied_date']}")
                print(f"Notes: {app['notes']}")
                print("-" * 30)

        elif choice == "2":
            company = input("Enter company name: ")
            role = input("Enter job role: ")

            status = input(
                "Enter status "
                "(To Apply/Applied/Interview/Offer/Rejected/Withdrawn): "
            )

            applied_date = input(
                "Enter application date (YYYY-MM-DD): "
            )

            notes = input("Enter notes: ")

            try:
                application = create_application(
                    applications,
                    company,
                    role,
                    status,
                    applied_date,
                    notes
                )

                applications.append(
                    application_to_dict(application)
                )

                save_applications(applications)

                print("\nApplication saved successfully!")
                print(application)

            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "3":
            keyword = input(
                "Enter company name to search: "
            )

            results = search_applications(
                applications,
                keyword
            )

            if not results:
                print("No applications found.")

            else:
                print("\nSearch Results:")

                for app in results:
                    print(f"ID: {app['id']}")
                    print(f"Company: {app['company']}")
                    print(f"Role: {app['role']}")
                    print(f"Status: {app['status']}")
                    print(f"Date: {app['applied_date']}")
                    print(f"Notes: {app['notes']}")
                    print("-" * 30)
        elif choice == "4":
            try: 
               application_id = int(input("Enter application ID to delete: "))

               deleted_application = delete_application(
                   applications,
                   application_id
                )

               if deleted_application:
                    save_applications(applications)
                    print("Application delted successfully!")
               else:
                    print("Application not found.")
            except ValueError:
                print("Please enter a valid numeric ID.")
        elif choice == "5":
                try:
                        application_id = int(
                            input("Enter application ID to update: ")
                        )
                
                        new_status = input(
                            "Enter new status "
                            "(To Apply/Applied/Interview/Offer/Rejected/Withdrawn): "
                        )
                
                        updated_application = update_application_status(
                            applications,
                            application_id,
                            new_status
                        )
                
                        if updated_application:
                            save_applications(applications)
                            print("Application status updated successfully!")
                            print(updated_application)
                        else:
                            print("Application not found.")
                
                except ValueError as error:
                    print(f"Error: {error}")

        elif choice == "6":
            statistics=get_application_statistics(applications)

            print("\nApplication Statistics:")

            if not statistics:
                print("No application found.")
            else:
                for status,count in statistics.items():
                    print(f"{status}: {count}")
 
        elif choice == "7":
           monthly_statistics= get_monthly_statistics(applications)

           print("\nMonthly Application Statistics:")

           if not monthly_statistics:
               print("No applications found.")
           else:
               for month,count in monthly_statistics.items():
                   print(f"{month}: {count}applications")
        elif choice == "8":
            try:
                application_id = int(
                    input("Enter application ID to edit: ")
                )

                company = input("Enter new company name: ")
                role = input("Enter new job role: ")
                notes = input("Enter new notes: ")

                updated_application = update_application(
                    applications,
                    application_id,
                    company,
                    role,
                    notes
                )

                if updated_application:
                    save_applications(applications)
                    print("Application updated successfully!")
                    print(updated_application)
                else:
                    print("Application not found.")

            except ValueError:
                print("Please enter a valid numeric ID.")
                
        elif choice == "8":
            print("Goodbye!")
            break
                
        else:
            print("Invalid choice. Please try again.")
                
                
if __name__ == "__main__":
    main()