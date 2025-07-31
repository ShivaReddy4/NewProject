# NewProject

This is a basic Django REST API project for managing notes and books. It includes full CRUD functionality and filtering capabilities.

## 🔧 Features

- Create, read, update, and delete books and notes
- Filter books by author or publication year
- Built with Django and Django REST Framework

## 📁 Project Structure

NewProject/
├── NewProject/ # Main project settings
├── notes/ # App for notes
├── books/ # App for books
├── manage.py # Django's CLI tool


## 🚀 Setup Instructions

1. Clone the repository:
  
  git clone https://github.com/ShivaReddy4/NewProject.git
  cd NewProject

2. Create virtual environment and activate:
 python -m venv env
 env\Scripts\activate  # On Windows

3. Install dependencies:
 Copy
 Edit
 pip install -r requirements.txt

4. Run migrations:
 Copy
 Edit
 python manage.py makemigrations
 python manage.py migrate

5. Run the development server:
 Copy
 Edit
 python manage.py runserver

6.Visit the API

http://127.0.0.1:8000/api/notes/


