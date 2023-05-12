###############
Creating an App
###############

************
Introduction
************

Although we have a basic project strucutre, we need to add an app,
which is a web application that performs some task for us.
To get started, we will create a simple app that consists of static pages
and does not rely on a database.

These pages will be:

*   a home page
*   a contact page
*   an about page

Such an app, although basic, can be used as a fully-functional personal site
and is a total "complete" product.


.. note::
  Django's layout is that a project will contain multiple apps,
  with each app being an independent bundle of functionality.

  When using this Django-specific definition of "app", it is important to not confuse
  this term with the project as a whole; sometimes people often casually refer to their
  entire project as being the app but this can create some ambiguity in what's being
  referred to.
  For this guide, we follow Django's terminology and use the word app to refer to a
  specific bundle of functionality as mentioned above.


***************
Starting an App
***************


#.  In your base directory, use the following command to start an app.
    We use the :file:`manage.py` module with the ``startapp`` command followed by the name
    of our app, which in this case is called `basics`:

    .. code-block:: console

      python manage.py startapp basics

This will create all the default files and folders, that automatically incorporate the
app name we passed to it - i.e. `basics`.

You should be able to see this directory structure in the VS Code explorer pane.

.. image:: _static/creating-an-app/new-app-tree.png
  :width: 400
  :alt: Default directory tree of new app

Since the created app is literally a Python package, its name should adhere to Python
conventions - i.e. snake case and ideally one word.

*******************************
Understanding the App Structure
*******************************

Like before, Django has created multiple files for us.

Here is a brief summary of the roles of each module created:

* **admin.py** 

  * This is where we can register our app to the admin interface.
    The admin interface is provided by Django and can be used to interact
    with the database via the browser. We will not be using the admin interface in
    this guide so this module can be ignored.

* **apps.py** 

  * This contains automatically generate configuration information for our 
    app and does not need to be changed.

* **models.py** 

  * This is where we define models. A model contains the information 
    Since we will not be using the database for our basics app, this module can 
    be deleted for clarity.

* **tests.py** 

  * This module is where tests can be written to check if our app is functioning correctly.
    We will not be writing tests in this guide so this module can be deleted.

* **views.py** 

  * Views are defined in this module. Views are what map a user's request to a
    specific URL to the template returned to the user will as a response.
    In processing the template before it is sent, views are able to interact with
    the database via our models and populate the template with data.

You may also notice that - when we run the ``startapp`` command for the first time -
a :file:`db.sqlite3` file has been created, which is a SQLite database.
Although our `basics` will not require a database, we can leave this here for now as we
will be using it later.


*******************
Registering our App
*******************

Whenever we start a new app, we should make sure to register it in our :file:`settings.py`
module (that is in our "site" directory). This is so that Django is aware to
include it in our project.

#.  In :file:`settings.py`, add the name of our app to the ``INSTALLED_APPS`` list:

    .. code-block:: python
      :emphasize-lines: 8

      INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'basics',
      ]

.. tip::

  When we add a new element to the end of a list, Python allows us to put a trailing comma
  after this last element (as shown above).

  Doing this ensures that this line does not need to be altered if we add another element
  to the end of the list later.
