##################
Using the Database
##################


*********************
Models and Migrations
*********************

It is important to know how we are able to interact with the database.
So far, we have produced static pages - i.e. they are always the same - and 
critically have no interaction with the database.

Of course, we want users to interact with the database by submitting data via forms
or having data displayed to them on the page.

We use models to provide this functionality for us. A model is a representation of our data.
Typically, one model represents one table in our database. These models are written in Python
and are defined in the :file:`models.py` module within each app.

We need a mechanism to alter the database whenever we make changes to any of our models.
This is the role of migrations. A migration is a file that represents one or more
changes to the database. These files are also Python modules, although they are not very
often viewed or edited manually.

*******************************
Getting Started with Migrations
*******************************

To see the migrations in action, we can run certain commands from the command line.

#.  Show migrations by running the following from the command line:

    .. code-block:: console

        python manage.py showmigrations
    
    You should get an output like so:

    .. code-block:: console

        admin
        [ ] 0001_initial
        [ ] 0002_logentry_remove_auto_add
        [ ] 0003_logentry_add_action_flag_choices
        auth
        [ ] 0001_initial
        [ ] 0002_alter_permission_name_max_length
        [ ] 0003_alter_user_email_max_length
        [ ] 0004_alter_user_username_opts
        [ ] 0005_alter_user_last_login_null
        [ ] 0006_require_contenttypes_0002
        [ ] 0007_alter_validators_add_error_messages
        [ ] 0008_alter_user_username_max_length
        [ ] 0009_alter_user_last_name_max_length
        [ ] 0010_alter_group_name_max_length
        [ ] 0011_update_proxy_permissions
        [ ] 0012_alter_user_first_name_max_length
        basics
        (no migrations)
        contenttypes
        [ ] 0001_initial
        [ ] 0002_remove_content_type_name
        sessions
        [ ] 0001_initial
    
    This is a list of the migrations Django has detected. You may be wondering where these
    came from: they actually were created automatically by Django when we setup our project.
    The migrations shown are derived from the "built-in" apps of Django. For example, the
    admin app has 3 migrations.

    As expected, our `basics` app is listed here and more importantly does not have any
    migrations: of course it doesn't since we never made any ourselves.

#.  To implement these default migrations into our database, run the following command:

    .. code-block:: console

        python manage.py migrate

    You should get the following output:

    .. code-block:: console

        Operations to perform:
        Apply all migrations: admin, auth, contenttypes, sessions
        Running migrations:
        Applying contenttypes.0001_initial... OK
        Applying auth.0001_initial... OK
        Applying admin.0001_initial... OK
        Applying admin.0002_logentry_remove_auto_add... OK
        Applying admin.0003_logentry_add_action_flag_choices... OK
        Applying contenttypes.0002_remove_content_type_name... OK
        Applying auth.0002_alter_permission_name_max_length... OK
        Applying auth.0003_alter_user_email_max_length... OK
        Applying auth.0004_alter_user_username_opts... OK
        Applying auth.0005_alter_user_last_login_null... OK
        Applying auth.0006_require_contenttypes_0002... OK
        Applying auth.0007_alter_validators_add_error_messages... OK
        Applying auth.0008_alter_user_username_max_length... OK
        Applying auth.0009_alter_user_last_name_max_length... OK
        Applying auth.0010_alter_group_name_max_length... OK
        Applying auth.0011_update_proxy_permissions... OK
        Applying auth.0012_alter_user_first_name_max_length... OK
        Applying sessions.0001_initial... OK


#.  Verify that the migrations have indeed been applied:

    .. code-block:: console

        python manage.py showmigrations
    
    You should get the following output:

    .. code-block:: console

        admin
        [X] 0001_initial
        [X] 0002_logentry_remove_auto_add
        [X] 0003_logentry_add_action_flag_choices
        auth
        [X] 0001_initial
        [X] 0002_alter_permission_name_max_length
        [X] 0003_alter_user_email_max_length
        [X] 0004_alter_user_username_opts
        [X] 0005_alter_user_last_login_null
        [X] 0006_require_contenttypes_0002
        [X] 0007_alter_validators_add_error_messages
        [X] 0008_alter_user_username_max_length
        [X] 0009_alter_user_last_name_max_length
        [X] 0010_alter_group_name_max_length
        [X] 0011_update_proxy_permissions
        [X] 0012_alter_user_first_name_max_length
        basics
        (no migrations)
        contenttypes
        [X] 0001_initial
        [X] 0002_remove_content_type_name
        sessions
        [X] 0001_initial
    
    As you can see, the **X** mark next to each migration indicates that it has been
    applied.
            
*******************************
Viewing the Database in VS Code
*******************************

We can view the tables of our SQLite database by installing an extension

#.  Go to the Extensions pane and search for `sqlite`
#.  Install the SQLite Viewer extension
#.  In the Explorer pane, click on the database and you should be able to see the tables

    .. image:: _static/using-the-database/sqlite-viewer.png
        :width: 800
        :alt: Display tables of SQLite database within VS Code


***************************
Creating an App with Models
***************************

Let's create an app called **orders**. This will contain data on imaginary orders that are
sold as part of our project. Specifically, it will contain 2 models - one to contain customer
data and the other for the product data itself.

#.  In the command line, start a new app called **orders**:

    .. code-block:: console

        python manage.py startapp orders

#.  Register our app in :file:`settings.py`:

    .. code-block:: python
        :emphasize-lines: 9

        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'basics',
            'orders',
        ]

#.  In the :file:`orders/models.py` module, we will create a model that represents
    our customer data:

    .. literalinclude:: _static/using-the-database/models-customer-01.py
        :language: python
        :emphasize-lines: 4-10
    
    There are several important concepts to note here:

    *   We are defining a class that inherits from Django's ``Model`` class.
        It means that we are able to build-off Django's "barebones" model functionality.
    *   We should always name our class as a singular - i.e. Customer not Customers. Tables
        should be named after the record they represent.
    *   We should always used pascal case for our classes (not just for Django but Python
        in general).
    *   We define fields as class attributes: 3 character fields (that store strings) and an email field.
        This email field helpfully validates whether the string entered is in the format of a valid email address.
    *   Within each of these fields, we pass in various arguments that modify their behaviour:

        *   The first positional argument for each field is the verbose name of that field
            
            *   For example, the first field of ``first_name`` will be displayed with the
                label of ``First Name``, which we specified ourselves.
            
            *   It is not strictly necessary to provide the verbose name since Django will
                automatically create one for us. Nevertheless, it is recommended to set it
                explicitly as Django's generated verbose name is not always what we want.

        *   The ``max_length`` kwarg for each ``CharField`` specifies the maximum number of
            characteres the user can enter. If the submitted number of characters surpasses
            the given integer (in our case 40), then the database will reject the creation of
            the record.

        *   The ``null`` and ``blank`` keyword arugments (for the ``middle_name`` field)
            indicate whether this field can have a value of null in the database or can be left
            blank when filling out forms on the front end. By default, these keyword arguments are
            ``False`` - i.e. the field is mandatory. If we set both kwargs to `True`, this means
            that such a field is optional - i.e. the user does not necessarily have to fill in 
            their middle name.

#.  To apply our model changes to the database - i.e. create the customer table - 
    run the following command:

    .. code-block:: console

        python manage.py makemigrations
    
    You should get the following output:

    .. code-block:: console

        Migrations for 'orders':
        orders/migrations/0001_initial.py
            - Create model Customer

    Also, you should be able to see a migration file appear in `orders/migrations`.


#.  To further verify the migration has been created, run the following command:

    .. code-block:: console

        python manage.py showmigrations orders
    
    You should get the following output:

    .. code-block:: console

        orders
        [ ] 0001_initial
    
    As you can see, Django has picked up on the migration file as it is tracking the
    contents of the migrations directory. We can see, however, that it is missing an
    **X** - i.e. it has not been applied yet to the database.

    .. tip::

        In the command above, we specified the app name ``orders`` as an argument in the
        ``showmigrations`` command. This is useful as it will only perform this action
        for the specified app. If we did not provide an app label, it will display all
        app migrations, which can clutter our screen up. The same principle applies for
        the ``makemigrations`` command - we can selectively create migration files for 
        a given app.

#.  To migrate our changes, run the following command:

    .. code-block:: console

        python manage.py migrate orders

    You should get the following output:
  
    .. code-block:: console

        Operations to perform:
        Apply all migrations: orders
        Running migrations:
        Applying orders.0001_initial... OK

#.  Verify that the table has been created by viewing it in VS Code:

    Notice how our table has its name prefixed by our app label automatically - i.e.
    it is ``orders_customer`` rather than just ``customer``. This is done deliberately
    by Django to ensure no name conflicts occur if two different apps have a model with 
    the same name.

***********************
Introduction to the ORM
***********************

Django allows us to interact with the database with Python (instead of SQL) as it has
an in-built ORM (object relational mapper) that connects to our database.

We can experiment with the ORM from the command line. It is important to get a feel for
how it works as this is the mechanism that the views will use to query, create, update and
delete data on behalf of the user.

#.  In the command line, run the following command that will provide a shell setup by
    Django:

    .. code-block:: console

        python manage.py shell

#.  In the Python shell, import our ``Customer`` model from our `orders` app:

    .. code-block:: python

        >>> from orders.models import Customer

#.  Query the ``Customer`` model to retrieve all records (although the table is empty):

    .. code-block:: python

        >>> Customer.objects.all()
        <QuerySet []>
    
    This will return an empty queryset as we have no records in our table.

#.  Create a ``Customer`` record:

    .. code-block:: python

        >>> Customer.objects.create(first_name='Darth', last_name='Vader', email='darth@thesith.com')
        <Customer: Customer object (1)>

#.  Re-run the query command to show that indeed we now have a record:

    .. code-block:: python

        >>> Customer.objects.all()
        <QuerySet [<Customer: Customer object (1)>]>
    
    You can also view it in VS Code - although you may need to refresh the tab displaying
    your database.

#.  Query records on a specific field:

    .. code-block:: python

        >>> Customer.objects.filter(last_name='Vader')
        <QuerySet [<Customer: Customer object (1)>]>

    .. code-block:: python

        >>> Customer.objects.filter(first_name='Luke')
        <QuerySet []>

#.  Exit the shell with :kbd:`Ctrl+Z` or by typing ``exit()``

****************************
Record String Representation
****************************

As seen above, the string representation displayed to us is not too helpful - i.e. it
is not at all clear what the record ``<QuerySet [<Customer: Customer object (1)>]>`` entails.

To fix this, we can change how the record in a model is displayed to increase readability.

#.  In :file:`orders/models.py`, define the following method:

    .. literalinclude:: _static/using-the-database/models-customer-02.py
        :language: python
        :emphasize-lines: 12-13

    This will return the first name followed by the last name of any given record.
    In the context of a model, ``self`` represents a record.
    We can use the class attributes to access the value of a specific field on our model.

    It should be noted that, although we've made a change to our model, no migrations are
    created from this: we are simply changing the cosmetic appearance at the application
    level instead of the database.

#.  Verify in the shell that this change has been implemented:

    .. code-block:: console

        python manage.py shell

        >>> from orders.models import Customer
        >>> Customer.objects.all()
        <QuerySet [<Customer: Darth Vader>]>
        
