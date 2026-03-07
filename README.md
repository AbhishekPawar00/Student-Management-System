# Student Management System (Django)

## Project Description

This is a Django-based Student Management System that allows users to manage student records. The system includes authentication and CRUD operations for students.

## Features

* User Registration
* User Login and Logout
* Add Student
* Edit Student
* Delete Student
* View Student List
* Search Student
* Django Admin Panel

## Technologies Used

* Python
* Django
* HTML
* Bootstrap
* SQLite

## Setup Instructions

### 1 Clone Repository

git clone https://github.com/AbhishekPawar00/student-management-system.git

### 2 Navigate to Project

cd student-management-system

### 3 Create Virtual Environment

python -m venv myvenv

### 4 Activate Environment

Windows:
myvenv\Scripts\activate

Mac/Linux:
source myvenv/bin/activate

### 5 Install Dependencies

pip install -r requirements.txt

### 6 Run Migrations

python manage.py migrate

### 7 Create Superuser

python manage.py createsuperuser

### 8 Run Server

python manage.py runserver

## Access URLs

Login Page:
http://127.0.0.1:8000/login/

Register Page:
http://127.0.0.1:8000/register/

Student List:
http://127.0.0.1:8000/students/

Admin Panel:
http://127.0.0.1:8000/admin/

## Author

Abhishek Dattatray Pawar
