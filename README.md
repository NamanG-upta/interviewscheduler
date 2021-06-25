# interviewscheduler

This is an Interview scheduler app build using Django, dbSqlite . In this app, user can create, edit or delete interviews between 2 different persons. Also, user can upload resume for the interview. 

# Steps to Run 

## Creating the virtual environment

```
python -m venv env
env/scripts/activate

```

## Running the program

```
pip install django
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser ( create your user by giving the various fields )
python manage.py runserver

```

```

1. Open the /admin url page.
2. Give your username and password of user you just created
3. Go to the /admin/auth/user and create 2-3 users.
4. And go to home and then go to /admin/interview_planner/interview/ and create the interviews.
5. You can create, update, delete and view the scheduled interviews.

```