import unittest

from services import (
    get_next_id,
    create_application,
    update_application_status,
    delete_application,
    search_applications
)


class TestServices(unittest.TestCase):

    def test_get_next_id(self):
        applications = [
            {"id": 1},
            {"id": 2},
            {"id": 5}
        ]

        result = get_next_id(applications)

        self.assertEqual(result, 6)

    def test_empty_applications(self):
        result = get_next_id([])

        self.assertEqual(result, 1)

    def test_invalid_status(self):
        applications = []

        with self.assertRaises(ValueError):
            create_application(
                applications,
                "OLG",
                "Developer",
                "Invalid",
                "2026-09-20",
                "Test"
            )

    def test_create_application(self):
        applications = []

        application = create_application(
            applications,
            "OLG",
            "Customer Care Specialist",
            "Applied",
            "2026-09-20",
            "Test application"
        )

        self.assertEqual(application.company, "OLG")
        self.assertEqual(
            application.role,
            "Customer Care Specialist"
        )
        self.assertEqual(application.status, "Applied")
        self.assertEqual(application.id, 1)

    def test_update_application_status(self):
       applications = [
          {
            "id": 1,
            "company": "OLG",
            "role": "Developer",
            "status": "Applied"
          }
       ]

       result = update_application_status(
             applications,
             1,
            "Interview"
        )

       self.assertEqual(result["status"], "Interview")
    def test_delete_application(self):
           applications = [
            {
            "id": 1,
            "company": "OLG",
            "role": "Developer",
            "status": "Applied"
            }
            ]

           result = delete_application(applications, 1)

           self.assertEqual(result["id"], 1)
           self.assertEqual(len(applications), 0)

    def test_search_applications(self):
         applications = [
            {
            "id": 1,
            "company": "OLG",
            "role": "Developer",
            "status": "Applied"
            },
            {
            "id": 2,
            "company": "Walmart",
            "role": "Cashier",
            "status": "Applied"
             }
        ]

         results = search_applications(applications, "OLG")

         self.assertEqual(len(results), 1)
         self.assertEqual(results[0]["company"], "OLG")
if __name__ == "__main__":
    unittest.main()