## <h1 align="center">💭Learning Objectives ණ⃛(ᵒ͈̑ᴗ̂ᵒ͈̑ )” </h1>

## How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function
## <h1 align="center"> 🚨Requirements🚨 ✋(˶0 - 0˶)🤚 </h1>
<h3 align="left"> Python Scripts 🧑‍💻🇵‌🇾‌🐍 </h3>

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)


## <h1 align="center"> Python Unit Tests 🏘️ </h1>
- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- You have to use the unittest module
- All your test files should be python files (extension: .py)
- All your test files and folders should start by test_
- Your file organization in the tests folder should be the same as your project
- e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
- e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
- All your tests should be executed by using this command: python3 -m unittest discover tests
- You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
- All your modules should have a documentation (python3 -c ---'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')

## <h1 align="left"> Starting the Interpreter 👨🏽‍💻🧑🏻‍💻🧑🏼‍💻: </h1>
- Open a terminal: Launch a command prompt or terminal window on your computer.
- Navigate to the script: Use the cd command to navigate to the directory where the script is located.
- Execute the script: Execute the script: Run the script using its filename, type python ./console.py  and press Enter.

 ## <h1 align="left"> Using the Interpreter </>: </h1>
 Once the interpreter starts, you'll interact with it through text commands. The specific commands available will depend on your implementation, but common ones might include:

- Create: Used to create new objects like users, places, reservations, etc. (e.g., create user <username> <email>).
- Show: Displays details of specific objects (e.g., show place <place_id>).
- Update: Modifies attributes of existing objects (e.g., update user <user_id> <new_email>).
- Delete: Removes objects (e.g., delete reservation <reservation_id>).
- List: Shows a list of all objects of a specific type (e.g., list users).
- Search: Finds objects based on specific criteria (e.g., search place city:<city_name> price:<max_price>).
- Help: Provides information about available commands and their usage.
- Quit: Exits the interpreter.

