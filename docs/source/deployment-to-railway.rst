#####################
Deployment to Railway
#####################

************
Introduction
************

The Django project can be deployed using Railway: a "Platform as a Service" (PaaS) company,
which offers a (limited) free tier.

There are several changes that need to occur to make our repo ready for deployment:

*   **Web Server** - use Gunicorn

*   **Database** - use remote PostgreSQL instance

*   **Static / Media Files** - use WhiteNoise

*   **Secrets Management** - use environment variables

*   **Nixpacks** - specify Python provider to be used

*   **Procfile** - specify commands to run after app build is completed

*   **Update Dependencies** - add relevant packages in above areas to requirements.txt

Once the repo has been prepared for deployment, we can upload it to GitHub and link to it
with Railway.

**************************
Install Extra Dependencies
**************************

=======
Secrets
=======

#.  Install **python-dotenv** from the command line:

    .. code-block:: console

        pip install python-dotenv

==========
Web Server
==========

To ensure the web app can receive requests and send responses,
a web server needs to be constantly running. In development,
the web server used was the Django development server.
In production, however, we need to use a production-robust web server.

Since we are using PaaS (Platform as a Service), however, we instead use **Gunicorn**,
which is a Python-based web server;
this is what will be used to handle the HTTP traffic of our deployed app.

#.  Install Gunicorn from the command line:

    .. code-block:: console

        pip install gunicorn

There are many web servers to choose from but Gunicorn is the one of the most popular.
Traditionally, if hosting with IaaS, the server would have web server software installed
\- such as Apache or Nginx - and it would be configured for the app.

========
Database
========

#.  Install **psycopg2** from the command line:

    .. code-block:: console

        pip install psycopg2-binary
    
    In development, the default database is SQLite.
    In production, however, we need to use a database provided by Railway.
    The best option is PostgreSQL as Django has more support for this database than any other.
    In order for Django's ORM to interact with a PostgreSQL database,
    the adapter ``psycopg2`` must be installed.
    Of course, we obtain the database credentials (name, password, port etc.)
    after we have created it on Railway.

#.  Install **dj-database-url** which allows us to parse a database URL
    into its various components. 

    .. code-block:: console

        pip install dj_database_url
    
    We will use these database credentials in our :file:`settings.py` file.

==================
Static/Media Files
==================

#.  Install **WhiteNoise** from the command line:

    .. code-block:: console

        pip install whitenoise

    In production, we want static and media files to be served efficiently with **WhiteNoise**
    (rather than having to be processed by **Gunicorn**).

************************
Listing Our Dependencies
************************

We always want to have a definitive list of the dependencies that our project has.

#.  In the **repo** directory, create a :file:`requirements.txt` file from the command line:

    .. code-block:: console

        pip freeze > requirements.txt

******************
Secrets Management
******************

Download the amended version of
:download:`settings.py <_static/deployment-to-railway/settings.py>`,
which has some changes that make our app "production-ready": mostly around secrets
management.

To store our project's secrets safely, we must ensure that they are defined outside
of our repo.

We will store these secrets as **environment variables**.

Railway offers this functionality which enables us to configure
important settings of our app, without having to edit the source code.
These environment variables are set from our Railway account in the browser.

Nevertheless, our source code needs to be set up to read these environment variables that
will be eventually defined. To accomplish this task, we can simply use the **os** package.
The **os** package is from the standard library and ensures that we are able to read
the environment variables.

The below code in :file:`settings.py` stores the environment variables in a dictionary.

.. code-block:: python

    secrets = dict(os.environ)

Our app will be able to read environment variables we will set. In production,
we have to set these environment variables separately. When we are developing
locally, however, it would be quite cumbersome to manually set all these individual
environment, especially if we have several different projects on our computer.

To organise these environmental variables, we can actually store them in a dedicated file
that ends with the **.env** extension.

We will create such a local file - called :file:`secrets-example.env` - with some content
that looks something like this:

.. code-block:: text

    SECRET_KEY=this-is-your-secret-key-123456790
    DEBUG=True
    REMOTE_DATABASE_URL=postgresql://username:password@host:port/db_name
    ALLOWED_HOSTS=localhost, 127.0.0.1, www.example.com, subdomain.example.com
    CSRF_TRUSTED_ORIGINS=https://subdomain.example.com, http://localhost:8000, http://127.0.0.1:8000

Obviously, we have just included some placeholder values above. If we haven't deployed
our project to Railway, we will not know what the URLs are (neither for the
database nor the app itself).

To include the values above as environment variables locally, we need to load them
in with the **python-dotenv** package, more specifically, using the ``load_dotenv``
function.
First, however, we need to define the path of our :file:`secrets-example.env` file,
which in our case is going to be a directory called **secrets** in the parent 
directory of the repo. Then, when we call ``load_dotenv``,  our specific file will be read:

    .. code-block:: python

        from dotenv import load_dotenv
            ...
        BASE_DIR = Path(__file__).resolve().parent.parent
        REPO_DIR = BASE_DIR.parent
        SECRETS_DIR = REPO_DIR.parent / 'secrets'
        SECRETS_PATH = SECRETS_DIR / 'secrets-example.env'
            ...
        load_dotenv(SECRETS_PATH)

We need to load our environment variables from our file **before** we create our 
``secrets`` dictionary as shown above. This ensures that the ``secrets`` dictionary
will contain the contents of our secrets file. If ``load_dotenv`` is unable to find
a valid file with the path supplied, it will **not** raise an error (it will just
return a value of ``False``). This behaviour is actually useful as it means an error
will not be raised in the absence of a **.env**, which is exactly the case in
production when we use **Railway**.

.. danger::

    It is important to realise that we would never include the **any** secrets
    (e.g. database credentials) **anywhere** in our source code as it will expose
    sensitive information.

    We should also keep our **.env** secret and only share it with authorised
    collaborators!

For the database credentials, we do a similar thing using **dj_database_url**:

.. code-block:: python

    DATABASES = {
        'default': dj_database_url.config(
            default=f'sqlite:///{BASE_DIR}/db.sqlite3'
        )
    }
    try:
        remote_db_url = secrets['REMOTE_DATABASE_URL']
    except KeyError:
        pass
    else:
        remote_db = {'remote': dj_database_url.parse(remote_db_url)}
        DATABASES.update(remote_db)


The ``dj_database_url.config`` function will look for an environment variable
called ``DATABASE_URL``. If it finds this environment variable - which it should
as we set it ourselves in production via Railway - it will take the database URL
string and convert it into a dictionary of its various components
(username, password etc.). If it does not find the ``DATABASE_URL`` environment
variable - i.e. when running locally - it will use the default URL specified with the
``default`` keyword argument - i.e. to our local SQLite database.

There are two environmental variables that represent a collection of strings.
These are ``ALLOWED_HOSTS`` and ``CSRF_TRUSTED_ORIGINS``.
Both of these variables can contain multiple values.

For example, ``ALLOWED_HOSTS`` could contain `www.example.com <#>`_ and 
`subdomain.example.com <#>`_.
But environment variables consist of only one string: they cannot contain lists.
Therefore, we need to parse out the environment variable string into a Python list
of "substrings".

The expected format used in our :file:`settings.py` is of comma separated values,
including a space between them. So if we wanted to have our ``ALLOWED_HOSTS``
to contain `www.example.com <#>`_ and `subdomain.example.com <#>`_, we would
set the environment variable as: **www.example.com, subdomain.example.com**.

We can see how such environment variables are parsed in :file:`settings.py`
to a list by using the split method:

.. code-block:: python

    ALLOWED_HOSTS = secrets['ALLOWED_HOSTS'].split(', ')
        ...
    CSRF_TRUSTED_ORIGINS = secrets['CSRF_TRUSTED_ORIGINS'].split(', ')


======================
Configuring WhiteNoise
======================

It is simple to configure **WhiteNoise** to serve static files for us.
We just need to add it to our list of middleware and (optionally) an
additional setting to enhance performance:

#.  Add the following line to ``MIDDLEWARE`` in :file:`settings.py`:

    .. code-block:: python

        MIDDLEWARE = [
            ...
            'whitenoise.middleware.WhiteNoiseMiddleware',
        ]

#.  Define a ``STATICFILES_STORAGE`` variable in :file:`settings.py`:

    .. code-block:: python

        STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

*************************************
Extra Configuration Files for Railway
*************************************

We need to create 2 configuration files that Railway expects.

*   **Procfile**
    
    *   The Procfile specifies commands to be executed once Railway
        has built our deployment. It resides in the top-level repo directory
        \- i.e. where :file:`requirements.txt` is.

*   **nixpacks.toml**

    *   Railway uses Nixpacks to build images, which are files that bundle our code
        and its environment together.

    *   We need to ensure that Nixpacks is configured to build an image for the Python
        environment. Doing so ensures that we have an environment where Python is
        installed and our dependencies are installed
        from :file:`requirements.txt`.


#.  Create a :file:`Procfile` file in the **repo** directory (note the lack of file extension)

    .. note::
        The content of the ``Procfile`` assumes that your repo structure mirrors that in
        this guide - a repo containing a project directory which in turn contains a base
        directory. If your tree structure differs, you may need to modify the contents
        of the file from what is stated below.

#.  Insert the following line in :file:`Procfile`:

    .. code-block:: text

        web: cd example && python manage.py migrate && python manage.py collectstatic && gunicorn example.wsgi

    There are 3 commands that we execute here:

    #.  Migrate

    #.  Collect static files

    #.  Run the web server - i.e. start Gunicorn


    *   The web prefix indicates that the these commands are a web process.

    *   The commands are for the Linux terminal, which is the OS our project operates in.

    *   Since we are in the repo directory, we change directory into the base directory.

    *   We then run the standard commands, with the final one starting the web server.
    
    *   Railway should automatically direct HTTP traffic to the Gunicorn web server.

#.  Create a :file:`nixpacks.toml` file in the **repo** directory

#.  Insert the following line in :file:`nixpacks.toml`:

    .. code-block:: text

        providers = ['python']


*******************************
Uploading the Project to GitHub
*******************************

For Railway to access our files, we can upload them to a GitHub account that we can create
for free.

#.  Create a `GitHub <https://github.com/join>`_ account.

#.  Create a new repo - call it **example-repo**.

#.  Upload our project files to it as explained
    `here <https://docs.github.com/en/repositories/
    working-with-files/managing-files/adding-a-file-to-a-repository
    ?platform=windows#adding-a-file-to-a-repository-on-github>`_.


******************
Setting Up Railway
******************

#.  Create a Railway account using your GitHub account.
    This is more convenient as our project will be linked directly to one of our repos.

    .. warning::
        If you recently created a new GitHub account, Railway may prevent you from accessing your
        repos if it flags your account as being questionable due to being a newly-created
        account.

#.  Create a project by navigating to the Railway dashboard and clicking the **New Project**
    button: give the project a suitable name.

#.  Create the following services:

    #.  a **deployment** service

        *   select the repo in your GitHub account

    #.  a **database** service

        *   choose PostgreSQL

    To find out how to create them, follow the steps on the official page.

*********************
Environment Variables
*********************

We need to configure the environment variables on Railway that our Django app expects.

There are 5 environment variables that we need to set on Railway:

#.   ``DEBUG``

#.   ``SECRET_KEY``

#.   ``ALLOWED_HOSTS``

#.   ``CSRF_TRUSTED_ORIGINS``

#.   ``DATABASE_URL`` `(this contains all necessary database credentials)`

Note that setting any of these variables incorrectly will result in an error.
Fortunately, whenever we create or edit any variables in Railway,
our app will automatically be redeployed - so we can modify our configuration
multiple times to get it right.

Notice how we did not have to set the PostgreSQL variables
(one of which is the ``DATABASE_URL``): they should be automatically added when
we create the database.

========================    =======================================  
Variable                    Value         
========================    =======================================  
``ALLOWED_HOSTS``           `your-demo-app-domain.app`
``CSRF_TRUSTED_ORIGINS``    `https://your-demo-app-domain.app <#>`_              
``DEBUG``                   `False`
``SECRET_KEY``              `your-secret-key-123`
``DATABASE_URL``            `postgresql://postgres` ... `railway`
========================    =======================================
 
For ``DEBUG``, the logic in :file:`settings.py` is such that,
unless the environment variable is set to `True`,
the ``DEBUG`` setting will be ``False``.

It is important to realise that environment variables are **strings**;
when they are loaded in with the ``os`` module, they are not evaluated to built-in Python
types (boolean, lists etc.). When loading from a JSON file, however, we are able to
get built-in Python types and can set these to our setting variables directly.
Both cases are handled in :file:`settings.py` - i.e. for development and production.

For ``CSRF_TRUSTED_ORIGINS``, you can find your app's URL in the **Settings**
tab of your deployment service under the **Environment** section listed next to
**Domains**.

*******
Caveats
*******

======================
Absent Deployment Stop
======================
There does not seem to be an actual feature to stop/pause the deployment.
The workaround is to **Remove** the currently-running deployment and then
**Rollback** to it from the Deployments history.


===============
Deployment Time
===============
It is inevitable that it takes a minute or two for our app to deploy.
This wait time is not specific to Railway, but in general to any PaaS
that has to build an image and install all the dependencies.
You will be able to see this activity in the build logs.

===============
Free Tier Limit
===============
Naturally, the free tier has monthly limits:
both in credit (i.e. dollars) and execution time (i.e. hours).
The execution time limit is more restrictive as you cannot run a
single project continuously for the entirety of each month.




















































