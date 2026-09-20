import json
from pathlib import Path
DATA_FILE = Path("data/applications.json")
# This tells Python where to store applications.


def load_applications():
    try: 
        with open(DATA_FILE,"r") as file:
             applications=json.load(file)

        return applications
    except FileNotFoundError:
        return []
    
    except json.JSONDecodeError:
        print("Error: Applications file contains invalid JSON.")
        return []
# json.load() converts the JSON array into a Python list.


def save_applications(applications):
    DATA_FILE.parent.mkdir(exist_ok=True)
    # It creates the data folder if it doesn't exist. 🎉

    with open(DATA_FILE,"w") as file:
        json.dump(applications,file,indent=4) #applications=data
# json.dump() converts python data into JSON format 
# and saves or writes the JSON data directly into a file.


# TEST SECTION
if __name__ == "__main__": # this is used only when executes directly
    applications = [
        {
            "id": 1,
            "company": "OLG",
            "role": "Junior Developer"
        }
    ]

    save_applications(applications)

    loaded_data = load_applications()

    print(loaded_data)