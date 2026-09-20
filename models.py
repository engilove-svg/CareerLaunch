# A Model defines what information each job application contains.

# @dataclass automatically generates the __init__() method for your class,
# so you don't need to write it manually.

from dataclasses import dataclass

@dataclass
class Application:
    id : int
    company : str
    role : str
    status : str
    applied_date : str
    notes : str