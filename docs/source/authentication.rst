##############
Authentication
##############

Django conveniently provides us with authentication functionality out-of-the-box (i.e. a 
login and logout system). Authentication is important as it allows us to limit who is
able to interact with our project.

.. note::
    It is important to realise that we should never store passwords in plaintext in the
    database. Obviously, this is totally insecure since passwords can be viewed by those
    with database access or via data breachs. Instead, passwords are "hashed" and stored
    as a string (along with other info) in the database. Fortunately, Django's authentication
    system does this automatically for us and there is no need to modify the behaviour of
    this `password management <https://docs.djangoproject.com/en/4.2/topics/auth/passwords/>`_.

================================
Creating the Users App and Model
================================

We will need to create a users app that will contain a users model that will store
the details for our users.

#.  In your base directory, use the following command to start an app called `users`:

    .. code-block:: console

      python manage.py startapp users

#.  Register our app in :file:`settings.py` by adding ``users`` to the
    ``INSTALLED_APPS`` list:

    .. code-block:: python
      :emphasize-lines: 10

      INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'basics',
        ...
        'users',
      ]

#.  In :file:`users/models.py`, create a user model:

    .. literalinclude:: _static/authentication/models.py
        :language: python

    *   We inherit from Django's ``AbstractUser``, which means our ``User`` class automatically
        has the default authentication fields (e.g. username, password, email).
    *   Techincally, we can get authentication to work without this step by not
        definining a users model at all.
    *   But by creating this model explicitly, it allows us to customise our ``User`` model
        instead of relying on the default one, which would be difficult to tranisition away
        from if we wanted to use our own tailored version of it at a later date.
    *   More info can be found in the
        `Django documentation. <https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#substituting-a-custom-user-model>`_


#.  In :file:`settings.py`, add the following setting to reference
    our newly-created custom user model:

    .. code-block:: python

        AUTH_USER_MODEL = 'users.User'

====================
Creating a Superuser
====================

We can create our first user for our project. Specifically, we will create a superuser,
which is user that has the highest priveleges - you can think of it being like an
administrator role.

#.  In your base directory,run the following command:

    .. code-block:: console

      python manage.py createsuperuser

#.  Follow the interactive prompt by entering various details

    *   At this stage, you do not need to provide your real name, email etc. - they
        can be totally made up.
    
    .. danger::
        
        Do not use a weak password nor one that you use for other personal logins!
        You can use a password generator instead to generate a secure password.
        In fact, Django will warn you if you provide a weak password.

=============
Viewing Users
=============

User records can be viewed either through the command line or via the VS Code extension
for SQLite. The steps below us the command line method using the Django ORM.

#.  Run the following command:

    .. code-block:: console

        python manage.py shell

#.  Import the user model:

    .. code-block:: python

        from example.users import User

#.  Query the model to retrieve all user records:

    .. code-block:: python
        
        User.objects.all()


================================
Creating a Login and Logout View
================================

To authenticate users, we need to provide them with views to do so.
