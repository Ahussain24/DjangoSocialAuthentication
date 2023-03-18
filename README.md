# DjangoSocialAuthentication
Social authentication functionality with google. And add user in a database

Social Authentication with Google and User Creation with Django Signals
Description
This is a task to create a social authentication functionality using Google as the authentication provider. After the user is authenticated, the user information should be saved in the database. Once the user is added to the database, a Customer object should be created using Django signals. A Customer object is a one-to-one relation with the User object.

Technologies Used
Python
Django
Google API
Setup
Clone this repository to your local machine.

Create a virtual environment and activate it.

Install the required dependencies using pip install -r requirements.txt.

Go to the Google Developers Console and create a new project. Then, create OAuth 2.0 credentials for your project.

Configure the Django application to use the Google API credentials. To do this, create a credentials.json file in the root directory of your project and add the Google API credentials to it.

NOTE : UPDATE YOUR CREDENTIALS IN THE SETTINGS file
Create a database for the Django application.

Run the Django migrations using the command python manage.py migrate.

Start the Django server using the command python manage.py runserver.

Visit http://localhost:8000/ to see the login page.

Click on the "Login with Google" button to authenticate with your Google account.

Once you are authenticated, your user information will be saved in the database and a Customer object will be created using Django signals.
