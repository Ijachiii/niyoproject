# Niyo Project

# Project Title
## Task Management API

# Project Description
A RESTful API for a simple task management system with the following features
- User Authentication: Implement authentication using JWT tokens.
- CRUD Operations: Implement endpoints for creating, reading, updating, and deleting tasks.
- Data Persistence: Use a database of your choice to store task data.
- Input Validation: Validate input data to ensure data integrity and security.

# Installation
Step-by-step instructions on how to set up the project locally.
1. Clone the repository

`git clone https://github.com/Ijachiii/niyoproject.git`

`cd niyoproject`

2.  Set up a virtual environment and activate it:

`python -m venv .venv`

`source env/bin/activate`  # On Windows use `.venv\Scripts\activate`

3. Install the required dependencies:

`python -m pip install -r requirements.txt`

4. Apply database migrations:

`python manage.py migrate`

5. Create a superuser for accessing the admin interface:

`python manage.py createsuperuser`

6. Run the development server

`python manage.py runserver`

# Documentation
The project's Swagger documentation can be accessed at `http://127.0.0.1:8000/schema/swagger-ui`. Base url for this project when run locally is `http://127.0.0.1:8000`.