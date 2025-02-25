# Jeopardy Game Web Application

This is a `Jeopardy` game web application build using `Django`. It allows instructors to host a Jeopardy style quiz game in the classroom, with built in Arduino button functionality. The game board is displayed for students, and the instructor has a separate interface to manage questions, answers, and scores. The project includes features like importing questions from a `QTI` file, managing player scores, and tracking wagers.

## Features
* **Game Board**: Displays categories and questions.
* **Host Panel**: Allows instructor to control the game, see questions and answers, and update scores.
* **Player Management**: Keep track of players and their scores.
* **QTI Import**: Import quiz questions from a QTI file
* **Dockerized**: Runs in isolated Docker containers for easy setup.

## Prerequisites

* **Docker** and **Docker Compose** Installed. 
Download Link Below: [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)

* A basic understand of Django (optional for running the app, but useful for modifications)

## Installation & Setup

Follow these steps to run the application:

## 1. Clone the Repository
Start by cloning this repository to your local machine:

```bash 
git clone https://github.com/ZaEFe/Team3Jeopardy.git
cd jeopardy-game
```

## 2. Build the Docker Containers

Build the Docker images with the following command:

```bash
docker-compose build
```

## 3. Set Up the Database

Once the containers are built, start them up with:

```bash
docker-compose up
```

This will start the **web application** and the **PostgreSQL database**. The first time you run the app, you'll need to apply migrations to set up the database schema.

In another terminal window, run:

```bash
docker-compose exec web python manage.py migrate
```

## 4. Create an Admin Superuser (Optional)

If you want to access the Django admin panel, you can create an admin user:

```
docker-compose exec web python manage.py createsuperuser
```

## 5. Access the Application

* Open your browser and go to [http://localhost:8000](http://localhost:8000)
* To access the Django admin panel, go to [http://locahost:8000/admin](http://localhost:8000/admin) and log in using the admin credentials you created.

## 6. Import Questions from QTI (Optional)

If you have **QTI** file (an XML file containing questions and answers), you can import the questions into the game. You'll need to use the django management command.

First, place your QTI file in the project directory.

Then, run the following command to import the questions:

```bash
docker-compose exec web python manage.py import_qti your_qti_file.xml
```
This will parse the XML file and create the questions and categories in your database.

## 7. Stopping the Containers

When you're done, you can stop the docker containers with:

```bash
docker-compose down
```
This will stop and remove the containers. If you want to keep the data (e.g., questions, scores), you can skip this step, as Docker volumes are used to persist database data.

## How It Works

1. **Game Board**: The main page (`/`) shows a grid of categories with questions and dollar amounts. Click on a dollar amount to reveal the question and answer.
2. **Host Panel**: Accessible at
`/host_panel/`, this panel allows the instructor to control the game, including revealing questions, updating scores, and managing wagers.
3. **Player Scores**: Players' scores are automatically updated based on their answers.
4. **Wagers**: Players can place wagers on Daily Doubles and Final Jeopardy.

## Configuration

### Database Configuration
In the `settings.py` file, you can configure the PostgreSQL database connection. By default, the Docker Compose setup uses the `db` service (PostgreSQL) as the database host.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'jeopardy_db',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'db',
        'PORT': '5432',
    }
}
```

### Custom Commands

You can use the `import_qti.py` management command to import quiz questions from a **QTI** file.

```bash
docker-compose exec web python manage.py import_qti your_qti_file_here.xml
```
### Static Files
By default, static files (CSS, Javascript) will be served by Django in development. In production, you should configure `collectstatic` to serve them via a CDN or dedicated static server.

To collect static files, run:
```bash
docker-compose exec web python manage.py collectstatic
```
## 
### File Structure

Here's an overview of the project directory:

```php
jeopardy/
├── jeopardy/              # Main Django project directory
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── game/                   # Django app for the game logic
│   ├── migrations/         # Database migrations
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/          # HTML Templates
│   ├── management/         # Custom management commands
│   └── static/             # Static files (CSS/JS)
├── Dockerfile              # Dockerfile for containerization
├── docker-compose.yml      # Docker Compose configuration file
├── requirements.txt        # Python dependencies
└── manage.py               # Django's command-line utility
```
##
### Troubleshooting
* **Can't connect to the database**: Make sure the database container is running (`docker-compose up`).
* **Static files not loading**: Ensure that `collectstatic` was run to collect all static files.


