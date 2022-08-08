# AirBnB clone

##Description
This is a team project part of ALX Full stack Software Engineering Program

## Usage

To launch the console application in interactive mode simply run:
Abeg do
`./console.py`

To run in the non-interactive mode:

`echo "your-command-goes-here" | ./console.py `

### Commands

| Commands          | Description                                                                                                                                             | Usage                                        |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| **help** or **?** | Displays documented commands.                                                                                                                           | **help**                                     |
| **quit**          | Exits the program.                                                                                                                                      | **quit**                                     |
| **EOF**           | Ends the program. Used when files are passed into the program.                                                                                          | N/A                                          |
| **create**        | Creates a new instance of the \<class_name\>. Stores in a JSON file, the object's serialized string representation and prints the id of created object. | **create** \<class_name\>                    |
| **show**          | Prints the string representation of an instance based on the class name and id.                                                                         | **show** \<class_name class_id\>             |
| **destroy**       | Deletes and instance base on the class name and id.                                                                                                     | **destroy** \<class_name class_id\>          |
| **all**           | Prints all string representation of all instances based or not on the class name                                                                        | **all** or **all** \<class_name class_id\>   |
| **update**        | Updates an instance based on the class name and id by adding or updating attribute from a dictionary or without a dictionary                            | **update** \<class_name class_id key value\> |

### Models

- `models/` directory contains classes used for this project:
- The class `BaseModel` defines all common attributes/methods for other classes and is the base class for the project.
- Other classes that inherit from the `BaseModel` class include:
  - `User`
  - `Place`
  - `City`
  - `Amenity`
  - `State`
  - `Review`
- The `FileStorage` class serializes instances of all the classes above to a JSON file and also deserializes JSON file to instances.

### Tests

All tests of the application are located in the `tests/` folder.
To execute all unit tests, run:
`python3 -m unittest discover tests `
from the root directory. Adding option `-v` reduces verbosity of the results

