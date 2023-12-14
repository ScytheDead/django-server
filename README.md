# Python Django Project

This is a simple Django web server project designed to manage the Product model via Django's admin interface and provide an interface for managing users with API calls to a Python proxy server. The Python proxy server forwards requests from the Python script to the Express API server. The project leverages Django ORM to interact with an SQLite database.

## Python Version

This project requires a specific version of Python to run successfully. Ensure that you have Python installed, and the recommended version is specified below.

- Python: `>=3.9`

## Project Dependencies

- asgiref v3.7.2
- certifi v2023.11.17
- charset-normalizer v3.3.2
- Django v4.2.8
- idna v3.6
- pip v21.2.4
- python-dotenv v1.0.0
- requests v2.31.0
- setuptools v58.0.4
- sqlparse v0.4.4
- typing_extensions v4.9.0
- urllib3 v2.1.0

## Environment Configuration

This project utilizes a configuration file named `.env` to store sensitive information and configuration settings. Below is an example of the content you might include in your `.env` file:

```env
FLASK_PROXY_URL='http://localhost:60000/api/users'
SECRET_KEY='django-insecure-c297+z6xm0)t==*rw@&$u@j5c5yhjafeh#)0rg3*t+e+&r$@s9'
DATABASE='db.sqlite3'
DATABASE_ENGINE='django.db.backends.sqlite3'
```

## Installation

1. Clone the repository:

  ```bash
  git clone https://github.com/ScytheDead/django-server.git

  cd django-server
  ```

2. In the project directory, create a virtual environment.

  ```bash
  python3 -m venv venv
  ```

3. Activate the virtual environment:

    - On macOS/Linux:

      ```bash
      source venv/bin/activate
      ```

    - On Windows:

      ```bash
      .\venv\Scripts\activate
      ```

After activation, you should see the virtual environment name in your terminal prompt.

4. Install project dependencies:

  ```bash
  pip install -r requirements.txt
  ```

This ensures that the required Python packages are installed within the virtual environment.

5. Run migrations to create the database:

  ```bash
  cd myproject

  python manage.py makemigrations

  python manage.py migrate
  ```

6. Create a superuser by writing the following command:

  ```bash
  python manage.py createsuperuser
  ```

We then write the following credentials step by step:

- Username
- Email address
- Password
- Password (again)


7. After create a superuser, start the project using the following command:

  ```bash
  python manage.py runserver
  ```

## Admin Interface

### Logging into the Admin Dashboard

- Open your web browser and go to `http://localhost:8000/admin`

- Log in with the superuser credentials you created during the project setup.

- Once logged in, you will be redirected to the admin dashboard.

### Managing Products

- Navigate to the 'MYAPP' section.

- Inside the 'MYAPP' section, you'll find the 'Products' subsection.

- In this section, you can perform CRUD operations to manage your products effectively.

## User Management Interface.

- In your web browser, navigate to `http://localhost:8000/users`.

- This is a user management page where you can perform CRUD operations to manage users efficiently.

- Utilize the user management interface to create, retrieve, update, and delete user records.

This page interfaces with the Python Proxy Server, which is running on `http://localhost:60000`. All API calls made on this page are directed to the Python Proxy Server.

## NOTE
- Remember to activate the virtual environment each time you work on the project to ensure you're using the correct dependencies.

- To deactivate the virtual environment when you're done:

```bash
deactivate
