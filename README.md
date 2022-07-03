
# AirBnB_clone

The project consists of several parts. Initially, it consists of
creating an AirBnB console. In other parts the database and the
front-end interface will be implemented. This is the first part, 
currently only the console was created.

As the database is not yet implemented, the information is stored
in a json file.

## Console
We have created a console that works just like a shell. The console
is a command interpreter, in this case it only works in  specific 
cases, such as createing objects, updateing attributes, destroying 
objects, etc. 

### To execute the console:
    - Interactive mode:
        vagrant@ubuntu-focal:~/holbertonschool-AirBnB_clone$ ./console.py
        (hbnb)help

        Documented commands (type help <topic>):
        ========================================
        EOF  all  count  create  destroy  help  quit  show  update

        (hbnb)

    - Non-interactive mode:
        vagrant@ubuntu-focal:~/holbertonschool-AirBnB_clone$ echo help | ./console.py 
        (hbnb)
        Documented commands (type help <topic>):
        ========================================
        EOF  all  count  create  destroy  help  quit  show  update

        (hbnb)
        vagrant@ubuntu-focal:~/holbertonschool-AirBnB_clone$
    

### Commands executed by the console
- quit / EOF: Exit the program
- help: Commands to be used or description of the commands
- create: Creates a new instance of BaseModel
- show: Prints the string representation of an instance based on the class name and id
- destroy: Deletes an instance based on the class name and id
- all: Prints all string representation of all instances based or not on the class name
- update: Updates an instance based on the class name and id by adding or updating attribute
- count: Print how many instances exit

## Existing classes

- BaseModel
- User: Inherits from BaseModel
- State: Inherits from BaseModel
- City: Inherits from BaseModel
- Amenity: Inherits from BaseModel
- Place: Inherits from BaseModel
- Review: Inherits from BaseModel

## Examples

- quit:

        vagrant@ubuntu-focal:~/holbertonschool-AirBnB_clone$ ./console.py 
        (hbnb)quit
        vagrant@ubuntu-focal:~/holbertonschool-AirBnB_clone$

- EOF / ctrl + D:

        vagrant@ubuntu-focal:~/holbertonschool-AirBnB_clone$ ./console.py 
        (hbnb)EOF
        vagrant@ubuntu-focal:~/holbertonschool-AirBnB_clone$

- create:

        vagrant@ubuntu-focal:~/holbertonschool-AirBnB_clone$ ./console.py 
        (hbnb)create User
        865274b8-9c27-4fef-ab1d-10c1522ae3e7
        (hbnb)

- show:

        (hbnb)show User 865274b8-9c27-4fef-ab1d-10c1522ae3e7
        [User] (865274b8-9c27-4fef-ab1d-10c1522ae3e7)  {'id': '865274b8-9c27-4fef-ab1d-10c1522ae3e7', 'created_at': datetime.datetime(2022, 7, 3, 16, 52, 31, 353251), 'updated_at': datetime.datetime(2022, 7, 3, 16, 52, 31, 353253)}
        (hbnb)

- all:

        (hbnb)all
        ["[User] (865274b8-9c27-4fef-ab1d-10c1522ae3e7)  {'id': '865274b8-9c27-4fef-ab1d-10c1522ae3e7', 'created_at': datetime.datetime(2022, 7, 3, 16, 52, 31, 353251), 'updated_at': datetime.datetime(2022, 7, 3, 16, 52, 31, 353253)}"]
        (hbnb)

- update:

        (hbnb)update User 865274b8-9c27-4fef-ab1d-10c1522ae3e7 Name "Betty"
        (hbnb)show User 865274b8-9c27-4fef-ab1d-10c1522ae3e7
        [User] (865274b8-9c27-4fef-ab1d-10c1522ae3e7)  {'id': '865274b8-9c27-4fef-ab1d-10c1522ae3e7', 'created_at': datetime.datetime(2022, 7, 3, 16, 52, 31, 353251), 'updated_at': datetime.datetime(2022, 7, 3, 16, 55, 51, 234923), 'Name': 'Betty'}
        (hbnb)

- count:

        (hbnb)User.count()
        1
        (hbnb)

- destroy:

        (hbnb)destroy User 865274b8-9c27-4fef-ab1d-10c1522ae3e7
        (hbnb)User.count()
        0
        (hbnb)





## Authors

This project was created by [Axel Bouvier](https://github.com/AxelBouvierM) and [Ezequiel Silva](https://github.com/ezesilva95) for Holberton School (Cohort #17)
