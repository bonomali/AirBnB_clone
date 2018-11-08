# 0x00. AirBnB clone - The Console
---
## Description

This project aims to recreate the basic functionality of the AirBnB website from the back end to the front end. The project will be done in several steps. First step: create a console for future use as a limited-use Command line interpreter for an AirBnB clone. This shell was created and tested on Ubuntu 14.04 using Python 3.4.3. Your milage may vary with other distributions or versions. This console should be able to:
- Create a new object (ex: a new User or a new Place)
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

During this project we will cover:
- How to create a Python package
- How to create a command interpreter in Python using the `cmd` module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage `datetime`
- What is a `UUID`
- What is `*args` and how to use it
- What is `**kwargs` and how to use it
- How to handle named arguments in a function

---
## How to Install

TBD

---
## How to Use

Interactive Mode:
~~~
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
~~~

Non-Interactive Mode:
~~~
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
~~~

---
## Requirements for Python Scripts

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Code should use the `PEP 8` style (version 1.7 or more)
- All files must be executable
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)

## Requirements for Python Unittests

- Allowed editors: `vi`, `vim`, `emacs`
- All files should end with a new line
- All test files should be inside a folder `tests`
- All test files should be python files (extension: `.py`)
- All test files and folders should start with `test_`
- File organization in the tests folder should be the same as project:
	* for `models/base_model.py`, unit tests must be in: `tests/test_models/test_base_model.py`
	* for `models/user.py`, unit tests must be in: `tests/test_models/test_user.py`
- All tests should be executed by using this command: `python3 -m unittest discover tests`
- Can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base_model.py`
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
---

File|Description
---|---
README.md| A file containing the goal of the project and the requirements and restrictions followed while creating it
AUTHORS| A file listing the contributors to the repository

---
## Authors
Essence Boayue [Github](https://github.com/eboayue)|[LinkedIn](https://www.linkedin.com/in/essenceboayue/)|[Twitter](https://twitter.com/girlsaregeeks2)

Robert Glatzel [Github](https://github.com/robertglatzel)|[LinkedIn](https://www.linkedin.com/in/robert-glatzel/)|[Twitter](https://twitter.com/rglatzell)
