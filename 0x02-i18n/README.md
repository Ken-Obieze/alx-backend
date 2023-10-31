# Internationalization (i18n) with Flask and Babel

This project is a Flask web application that demonstrates internationalization (i18n) using Flask and Babel. It includes features such as locale selection, parametrized templates, URL parameter-based locale switching, and a mock user login system. The project also allows users to set their preferred locale and time zone.

## Getting Started

These instructions will help you set up and run the project on your local machine.

## Requirements

* All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
* All your files should end with a new line
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle style (version 2.5)
* The first line of all your files should be exactly #!/usr/bin/env python3
* All your *.py files should be executable
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions and methods should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
* All your functions and coroutines must be type-annotated.

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com//Ken-Obieze/alx-backend.git
   ```
2. Navigate to the project directory:

   ```bash
   cd 0x02-i18n
   ```
3. Install the required Python packages:

   ```bash
   pip3 install flask_babel==2.0.0
   ```

## Usage
1. Run the Flask application:

   ```bash
   python app.py
   ```
2. Access the application in your web browser at http://127.0.0.1:5000/.

## Features
* Locale selection using Flask-Babel.
* User-specific locale and time zone settings.
* URL parameter-based locale switching.
* Mock user login system for testing.
* Displaying the current time in the user's preferred time zone.

### Files
* app.py: The Flask application with routing and logic.
* 0-app.py - 7-app.py: The Flask application with routing and logic.
* templates/index.html: HTML template for the home page.
* templates/0-index.html - 7-index.htnl: HTML template for the home page.
* translations/: Directory containing translation files.
* README.md: Project documentation.
