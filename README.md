# TheRollaMissionDjango
Django website for CS 4096 (Spring 2020).

## Setup

- Download and install Postgres on your local machine. Make sure to remember the password you choose.

- Clone this repository to your computer.

- Use python to pip install virtualenv on your machine. This will be used to create a virtual python environment from which to install all of the dependencies for the app, including Django. Once you have virtualenv installed, navigate to the project repository and run `virtualenv venv -p python3`. To activate the virtual environment, run `source venv/bin/activate` (note: this command will be different for Windows). You will need to activate this virtual environment any time you want to work on the project.

- Run `pip install -r requirements.txt` to install all the necessary python dependencies.

- Run `python manage.py migrate` to create the necessary database tables.

- Run `python manage.pu runserver` to start the server.


