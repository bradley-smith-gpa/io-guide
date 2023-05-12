#################################
Creating Records via the Frontend
#################################

Of course, we want the user to create records themselves instead of using the ORM which
they will not have access to.

To do so, we need to add a view to create a record that incorporates a form so that the user
can submit data.

====================
Adding a Create View
====================

#.  In :file:`orders/views.py`, add the following:

    .. literalinclude:: _static/creating-records-via-the-frontend/views-01.py
        :language: python

    *   **template_name**
    
        *   This is the same class attribute we saw before with our basic pages
            and will create the template it refers to later.
    
    *   **model**

        *   This is the model class our view is referring to: ``Customer``.
    
    *   **form_class**

        *   This is the form class our view will use. We have set it to
            ``CustomerCreateForm`` which we will create later.

        *   The form will provide the validation for the data that is submitted by the user.

        *   Also, it provides the input fields in the template.
    
    *   **success_url**

        *   This is the URL the user will be redirected to if their data is successfully
            submitted and a customer record has been created.

        *   We use the ``reverse_lazy`` function around the URL pattern name, which 
            will do a "lookup" and return the relevant URL, which in this case is the
            homepage.
        
        *   ``reverse_lazy`` is used instead of the regular ``reverse`` so that this function
            does not get called when Django server starts up, which is an issue to avoid when
            using class-based views.

=============
Adding a Form
=============

#.  Create a :file:`forms.py` module in our `orders` app with the content below:

    .. literalinclude:: _static/creating-records-via-the-frontend/forms-01.py
        :language: python

    *   **__init__**
    
        *   We override the ``__init__`` method to customise the look our fields when they
            are rendered as HTML.

    *   **Meta.model**
    
        *   This is the model class our form is referring to: ``Customer``.

    *   **Meta.fields**
    
        *   The list of fields our form will contain from the ``Customer`` model.

        *   Alternatively, you can set this attribute to the string ``__all__`` instead of a
            list, which will automatically add all fields to this model. Ensure, however, that
            you genuinely want to add all of a model's fields to the form; if a new field is
            added to the model, this will automatically appear on the frontend, whether you
            intend the user to see it or not.

    *   **template_name**
    
        *   This is the template that the form will use when it is rendered as HTML.
        *   We will create this template later.


====================
Adding the Templates
====================

#.  Create a `customer-create` directory in our `templates/orders` directory within our
    `orders` app:

#.  Create the overall template for the view by adding :file:`customer-create.html` with
    the following content:

    .. literalinclude:: _static/creating-records-via-the-frontend/customer-create-01.html
        :language: html


    *   The important part here is the ``form`` element
    
        *   We set the ``method`` attribute to ``post`` as we will be submitting data.
        *   We include ``novalidate`` to disable default browser validation: we are already
            providing our own.
        *   We include a **csrf_token** tag which is mandatory. It provides us with a hidden
            field containing a token, which prevents threat actors from submitting bogus
            POST requests on the user's behalf.
        *   The **form** variable will display our form according to the form template we
            will define next. The **form** variable is an instance of the form class 
            set under the ``form_class`` attribute in our view earlier on.

#.  Create the form template for the form by adding :file:`form.html` with
    the following content:

    .. literalinclude:: _static/creating-records-via-the-frontend/form-01.html
        :language: html


    *   We iterate over each field in our form. First, we display any errors from a previous
        invalid attempt if possible. Then, we loop through each field: rendering its label tag
        before the actual input element itself.
    *   At the end, we provide a button for the user to press which will submit the form.

====================
Configuring the URLs
====================

#.  Add an URL pattern to our site :file:`urls.py` module:

    .. literalinclude:: _static/creating-records-via-the-frontend/site-urls-01.py
        :language: python
        :emphasize-lines: 7

#.  Like before, create an :file:`urls.py` module in our app - in this case `orders` - 
    with the following content:

    .. literalinclude:: _static/creating-records-via-the-frontend/urls-01.py
        :language: python

=========================
Adding an URL to our View
=========================

Like before, once we create a page we want the user to have a link so they can access it
(rather than navigating using the address bar).

#.  Add another ``li`` element with an URL tag in the :file:`basics/base/base.html`
    which links to our view:

    .. literalinclude:: _static/creating-records-via-the-frontend/base-01.html
        :language: html
        :lines: 12-22
        :emphasize-lines: 7

This change is more of a quick fix; we will change how we access the create view in a more
clean way.


======================
Summary of the Process
======================

Let's review what we have done in the context of a user making requests to our customer
create view.

We can think of two ways the user interacts:
    #.  when they view the page with a GET request
    #.  when they submit data with a POST request

Viewing the Page
----------------

#.  The user sends a GET request to a specific URL in their browser.
#.  This URL is processed by the :file:`urls.py` module in the site directory
#.  Upon matching the route in the URL pattern, Django then forwards on the remainder
    of the path to the appropriate app - in this case `orders`.
#.  The remainder of this path is looked-up against the URL patterns in the
    :file:`urls.py` module of our `orders` app.
#.  Upon matching the route in the URL pattern, Django then calls the view function we
    linked to that route - in this case `CustomerCreateView`.
#.  An instance of this view is configured using the related model, form and template.
#.  Upon seeing that this is a GET request, the view simply builds an HTML file is
    from the overall view template, within which the form-specific template is rendered.
#.  This HTML is sent back to the user containing the form, along with the standard elements
    of the page - e.g. the header.

Submitting Data
----------------

#.  The user fills out the form and clicks the button to submit it.

#.  This creates a POST request to the **same** page they are already
    on - i.e. ``orders/customer/create``.

#.  Upon matching the route in the URL pattern, Django then forwards on the remainder
    of the path to the appropriate app - in this case `orders`.

#.  The remainder of this path is looked-up against the URL patterns in the
    :file:`urls.py` module of our `orders` app.

#.  Upon matching the route in the URL pattern, Django then calls the view function we
    linked to that route - in this case ``CustomerCreateView``.

#.  An instance of this view is configured using the related model, form and template.

#.  Upon seeing that this is a POST request, the view will collect the data submitted and
    enter it into our form class, which is ``CustomerCreateForm``. 

*   If the form is valid...

    *   the record is attempted to be created using the model ``Customer``.

    *   provided the data submitted does not violate any database constraints, the record is
        created in the database.

    *   the user is redirected to the ``success_url`` specified.

*   If the form is invalid...

    *   the user will be redirected back to the same page ``orders/customer/create``.

    *   the form, however, will still contain data from fields that were deemed valid
        (it means the user does not neeed to re-fill these fields).

    *   the user will also see such errors given the way we've written our template.

    *   the user will have to repeat the process if they continue to submit invalid data

