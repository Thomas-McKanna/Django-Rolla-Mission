# TheRollaMissionDjango
Django website for CS 4096 (Spring 2020).

## Important

There are certain steps you should take anytime you pull this repo. If this is your first time using the project, please skip to Setup below.

1. Run `secret/makemigrations.sh` (or .bat for Windows).
2. Run `secret/migrate.sh` (or .bat for Windows).
3. Finally, run the server with `secret/run.sh` (or .bat for Windows)

Note that you must receive the secret folder from the maintainer of this repo, as it contains secret keys for accessing AWS.

## Setup

- Download and install Postgres on your local machine. If prompted for a username, use "postgres". **When prompted for the password, use "password"**. This is important in ensuring that the setting in Django are correct. 

- Either through the terminal (psql) or via a GUI, **create a database named "mission".**

- Clone this repository to your computer.

- Use python to pip install virtualenv on your machine. This will be used to create a virtual python environment from which to install all of the dependencies for the app, including Django. Once you have virtualenv installed, navigate to the project repository and run `virtualenv venv -p python3`. To activate the virtual environment, run `source venv/bin/activate` (note: this command will be different for Windows). You will need to activate this virtual environment any time you want to work on the project.

- Run `pip install -r requirements.txt` to install all the necessary python dependencies.

- Get a copy of the `secrets` folder from the maintainer of this repo and copy it into the repository.

- Run `secret/migrate.sh` (or .bat for Windows) to create the necessary database tables.

- Run `secret/createsuperuser.sh` (or .bat for Windows)  to make a user for logging into the admin interface. It doesn't really matter what the username and password are, but I suggest username "admin" and password "password".

- Run `secret/run.sh` (or .bat for Windows) to start the server.


