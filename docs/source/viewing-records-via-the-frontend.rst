################################
Viewing Records via the Frontend
################################

Although the user can create records in the database, they need to be able to view them.
Fortunately, Django provides generic views to accomplish this and they are easier to
implement than the create (and update) views since they only revolve around GET requests.

====================
Adding a List View
====================

#.  In :file:`orders/views.py`, add the following lines:

    .. literalinclude:: _static/viewing-records-via-the-frontend/views-01.py
        :language: python
        :emphasize-lines: 14-17


===================
Adding the Template
===================

#.  Create a `customer-list` directory in our `templates/orders` directory within our
    `orders` app:

#.  Create the overall template for the view by adding :file:`customer-list.html` with
    the following content:

    .. literalinclude:: _static/viewing-records-via-the-frontend/customer-list-01.html
        :language: html


    *   We loop through each of the customers, displaying certain values within a card.
    
====================
Configuring the URLs
====================


#.  Add the following lines to the :file:`urls.py` module in our app:

    .. literalinclude:: _static/viewing-records-via-the-frontend/urls-01.py
        :language: python
        :emphasize-lines: 10-13

=========================
Adding an URL to our View
=========================

Like before, once we create a page we want the user to have a link so they can access it
(rather than navigating using the address bar).

#.  Add another ``li`` element with an URL tag in the :file:`basics/base/base.html`
    which links to our view:

    .. literalinclude:: _static/viewing-records-via-the-frontend/base-01.html
        :language: html
        :lines: 12-22
        :emphasize-lines: 8

This change is more of a quick fix; we will change how we access the create view in a more
clean way.


