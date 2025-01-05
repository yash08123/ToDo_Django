# Django Todo App

A simple Todo application built with Django, featuring user authentication and MySQL database integration.

## Features

- User authentication (signup, login, logout)
- Create, read, update, and delete (CRUD) operations for todos
- User-specific todo lists
- MySQL database for data storage
- Bootstrap for responsive UI

## Prerequisites

- Python 3.x
- Django 5.1.4
- MySQL Server
- MySQL client for Python (`mysqlclient`)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yash08123/ToDo_Django.git
   cd todo_project
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the MySQL database:**

   - Log into MySQL as root:

     ```bash
     mysql -u root -p
     ```

   - Create the database and user:

     ```sql
     CREATE DATABASE todo_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
     CREATE USER 'todo_user'@'localhost' IDENTIFIED BY 'todo_password';
     GRANT ALL PRIVILEGES ON todo_db.* TO 'todo_user'@'localhost';
     FLUSH PRIVILEGES;
     ```

5. **Configure the database in `settings.py`:**

   Update the `DATABASES` section in `todo_project/todo_project/settings.py` with your MySQL credentials:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'todo_db',
           'USER': 'root',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '3306',
           'OPTIONS': {
               'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
           }
       }
   }
   ```

6. **Run migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

8. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

9. **Access the application:**

   Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage

- Sign up for a new account or log in with an existing account.
- Add, complete, or delete todos.
- View your todo list.

## Troubleshooting

- If you encounter a `django.db.utils.OperationalError: (1045, "Access denied for user...")`, ensure your MySQL credentials in `settings.py` are correct and that the MySQL server is running.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements.

## Contact

For any questions or issues, please contact [yashnagarkar124@gmail.com](mailto:yashnagarkar124@gmail.com). 