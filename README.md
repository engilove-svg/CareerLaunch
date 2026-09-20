
# CareerLaunch 🚀

CareerLaunch is a Python-based job application tracking system that helps users manage and analyze their job applications.

## Features

- Add job applications
- View all applications
- Search applications by company or role
- Edit application details
- Delete applications
- Update application status
- View application statistics
- View monthly application statistics
- JSON data persistence
- Automated unit testing

## Technologies Used

- Python
- Object-Oriented Programming
- Dataclasses
- JSON
- File Handling
- Unit Testing
- Git & GitHub

## Project Structure

CareerLaunch/
├── main.py
├── models.py
├── services.py
├── storage.py
├── data/
│   └── applications.json
├── tests/
│   └── test_services.py
└── README.md

## How to Run

1. Clone the repository.
2. Open the project folder.
3. Run the application:

```bash
python main.py
```

## Run Tests

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

## Future Improvements

- SQLite database
- Skill gap analysis
- Web interface using Django
- Job recommendation system
- Dashboard with charts