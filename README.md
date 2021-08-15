# registration
prerequisite
-----------------------
- python should be available in the machine
- create a python virtual environ (> python -m venv env_name)
- activate the environment (> env_name/Scripts/activate)
- install all packages using (pip install -r requirements.txt)

- Go to project directory and open setting.py file for MySQL  and SMTP mail server configuration

Specify your database name, user, password, port ,host

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'student_registration',
        'USER': 'root',
        'PASSWORD': '*******',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
Specify your from mail username and password in SMTP configuration
# SMTP Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = '**************'
EMAIL_HOST_PASSWORD = '************'

- go to project directory run python manage.py makemigations
- run python manage.py migrate( it will create table for you in MySQL

-Run the project
 python manage.py runserver

