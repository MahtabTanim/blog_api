# Blog API

This is a simple Blog API project.

## Features

- Create, read, update, and delete blog posts
- User authentication and authorization
- Comment on blog posts

## Requirements

- Python 3.8+
- Django 3.2+
- Django REST framework

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/blogapi.git
    cd blogapi
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```sh
    python manage.py migrate
    ```

5. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Usage

- Access the API at `http://127.0.0.1:8000/api/`
- Access the admin panel at `http://127.0.0.1:8000/admin/`
