############################
Adding More Models and Views
############################

We can add in more models and views.

=============
Adding Models
=============

#.  In :file:`orders/models.py`, add the following lines:

    .. literalinclude:: _static/adding-more-models-and-views/models.py
        :language: python
        :emphasize-lines: 1, 3, 18-46


===================
Adding Create Views
===================

#.  In :file:`orders/views.py`, add the following lines:

    .. literalinclude:: _static/adding-more-models-and-views/views.py
        :language: python
        :emphasize-lines: 3-4, 20-31

================
Adding the Forms
================

#.  In :file:`forms.py` of our orders app, add the following lines:

    .. literalinclude:: _static/adding-more-models-and-views/forms.py
        :language: python
        :emphasize-lines: 2, 24-

====================
Adding the Templates
====================

#.  Create a `product-create` and `order-create` directory in our `templates/orders` directory within our
    `orders` app:

#.  Create the overall template for the view by adding :file:`product-create.html` and :file:`form.html` with
    the following content:

    .. literalinclude:: _static/adding-more-models-and-views/product-create/product-create.html
        :language: html

    .. literalinclude:: _static/adding-more-models-and-views/product-create/form.html
        :language: html

#.  Create the overall template for the view by adding :file:`order-create.html` and :file:`form.html` with
    the following content:

    .. literalinclude:: _static/adding-more-models-and-views/order-create/order-create.html
        :language: html

    .. literalinclude:: _static/adding-more-models-and-views/order-create/form.html
        :language: html


====================
Configuring the URLs
====================


#.  Add the following lines to the :file:`urls.py` module in our app:

    .. literalinclude:: _static/adding-more-models-and-views/urls.py
        :language: python
        :emphasize-lines: 2-4, 16-23

=========================
Adding an URL to our View
=========================

Like before, once we create a page we want the user to have a link so they can access it
(rather than navigating using the address bar).

#.  Add more ``li`` elements with an URL tag in the :file:`basics/base/base.html`
    which links to our view:

    .. literalinclude:: _static/adding-more-models-and-views/base.html
        :language: html
        :emphasize-lines: 20-21

This change is more of a quick fix; we will change how we access the create view in a more
clean way.


