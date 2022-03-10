# PROJECT SETUP
    # Open the OS terminal

    # Create a new folder with the name of the project you want
    mkdir PROJECTNAME

    # Then enter in it
    cd PROJECTNAME

    # If you wish, you can install globally so you can easily create VIRTUAL ENVIRONMENT
    pip install virtualenv

    # Create VIRTUAL ENVIRONMENT named venv (default name we use)
    virtualenv venv

    # Activate the new VIRTUAL ENVIRONMENT
        # Mac OS / Linux
        source venv/bin/activate

        # Windows
        venv\Scripts\activate
          # in case of error, run next line and try again the first command
          Set-ExecutionPolicy Unrestricted -Scope Process

    # Install DJANGO pip package, this will let us create our new DJANGO project and its dependencies
    python -m pip install Django

    # Create our new DJANGO project
    django-admin startproject PROJECTNAME .

    # This will create the following stucture

    # PROJECTNAME/
    #    manage.py
    #    PROJECTNAME/
    #        __init__.py
    #        settings.py
    #        urls.py
    #        asgi.py
    #        wsgi.py
    
    # We use POSTGRESQL for our DATABASES, so make sure to install it in your computer before you continue
    # Now we need to create the PROJECTNAME's DATABASE, to do it, follow the next steps:
        # Mac OS / Linux
        1. sudo su postgres
        2. psql template1
        3. CREATE DATABASE PROJECTNAME;
        4. CREATE USER PROJECTNAME WITH PASSWORD '123456!';
        5. GRANT ALL ON DATABASE PROJECTNAME TO PROJECTNAME;
        
        # Windows
        1. Open SQL Shell
        2. Log in like Admin in postgres database (password is "admin" )
        3. CREATE DATABASE PROJECTNAME;
        4. CREATE USER PROJECTNAME WITH PASSWORD '123456!';
        5. GRANT ALL ON DATABASE PROJECTNAME TO PROJECTNAME;

    # We need to install the POSTGRESQL database adapter, this will let PROJECTNAME handle our new DATABASE
    pip install psycopg2-binary

    # Now we need to go to our PROJECTNAME settings.py and include our DATABASE handler, this will allow our
    # PROJECTNAME to connect to its database

    # Now we will install the Allauth package to handle authentication, registration, account management as well as 3rd party (social) account authentication.
    pip install django-allauth


# SETTINGS.PY FILE CONFIGURATION

    # Change the installed PROJECTNAME configuration:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

    # To
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'PROJECTNAME',
            'USER': 'PROJECTNAME',
            'PASSWORD': '123456!',
            'HOST': 'localhost',
            'PORT': '',
        }
    }



    # In the internationalization section, we can change the default values with the following
    # If it needs to be another language different from Costa Rican spanish, you can find the options here: http://www.i18nguy.com/unicode/language-identifiers.html
    LANGUAGE_CODE = 'es-cr'
    TIME_ZONE = 'America/Costa_Rica'

    # In the static files section, we wil add the next code bellow the only line defined for it
    # In this case, we are saying our static files will be stored in a folder named assets, don't forget to create it
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'assets'),
    ]

    PUBLIC_STORAGE_ROOT = os.path.join(BASE_DIR, 'assets', 'uploads', 'public/')
    MEDIA_STORAGE_ROOT = os.path.join(BASE_DIR, 'assets', 'uploads', 'media/')

    MEDIA_URL = '/uploads/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'assets', 'uploads/')
    MEDIAFILES_DIRS = [
        PUBLIC_STORAGE_ROOT,
        MEDIA_STORAGE_ROOT
    ]

    # To give the project a folder to check for templates, we need to add the following code in the TEMPLATES list, in the DIRS list
    # Don't forget to create the folder as well
    'templates', 'templates/layouts'

    # To add the DJANGO messages framework, we need to add the following line
    # It will store the messages in the current session created by DJANGO
    MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

    # We will add a time limit for the users sessions
    # Session lasts an hour (IN SECONDS)
    SESSION_COOKIE_AGE = 60 * 60

    # Default format for DateFields
    DATE_INPUT_FORMATS = ['%Y-%m-%d']

    # We wil add a custom variable in our settings to create a global pagination default value
    DEFAULT_PAGINATION_AMOUNT = 5

# If you don't need to install more dependecies in the project, you can create the projects migrations
python manage.py makemigrations


# Then run the following command to add the created migrations to PROJECTNAME's DATABASE
python manage.py migrate
