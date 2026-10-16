CRUD Web Application

A web application developed with Flask and MySQL to demonstrate the implementation of CRUD operations and database-driven functionality.

Overview

This project demonstrates how a web application can create, retrieve, update, and delete records through a user interface connected to a relational database.

Features

- Create new records.
- Display and retrieve existing records.
- Update stored information.
- Delete records.
- Connect the backend to a MySQL database.
- Build a web interface using HTML and Tailwind CSS.
- Use JavaScript for client-side interactions where needed.

Tech Stack

- Backend: Python, Flask
- Database: MySQL
- Frontend: HTML, Tailwind CSS, JavaScript
- Local Development: WAMP / MySQL

Project Structure

project/
├── app.py
├── DB/
├── templates/
├── static/
│   ├── css/
│   └── js/
└── README.md

Adjust the folder names to match the actual repository.

Getting Started

Prerequisites

- Python 3
- WAMP or another MySQL server
- pip

Installation

1. Clone the repository:
   
   git clone https://github.com/dioppapi/crud_flask
cd ptsr

2. Install the required Python packages:
   
   pip install Flask mysql-connector-python
   
   Install any other dependencies used by the application.

3. Start the MySQL server.

4. Import the project's SQL database dump, if provided.

5. Configure the database connection in the application.

6. Run the application:
   
   python app.py

7. Open the local address displayed in the terminal.

Learning Objectives

This project provided practical experience with:

- Flask routing and request handling.
- CRUD operations.
- SQL database integration.
- Separating application logic, templates, and static assets.
- Building interactive web interfaces.

Author

Developed as a software engineering learning project.
