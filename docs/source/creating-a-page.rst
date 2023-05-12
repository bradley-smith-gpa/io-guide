###############
Creating a Page
###############


*************************
Understanding the Process
*************************

Before we start creating our pages, we need to have an overview of what we need to
display our basic pages to the end user.

We need to consider 3 key concepts:

* **urls**

  * When the user visits a page, their URL will contain a **path** that is
    sent to our project and is handled by Django. This path is simply the part of the
    URL that indicates - in our case - what page they want to visit.
    For example, if they visit the about page the path may be ``/about/`` - i.e. it
    would appear as ``your-website.com/about/`` in the address bar. 

* **views**

  * Now that Django has identified the path the user has requested, it needs to map this path
    to a specific **view**. A view simply takes a request and returns a response. The term 
    "view" is short for "view function". Like most cases, the response we want to give to the
    user is an HTML template.

* **templates**

  * The HTML template is the page that will be displayed to the end user.
    We need to write it ourselves.

Before we proceed, we need to create a few of these files ourselves as shown below.

***************
Setting up URLs
***************

To map URLs to their views efficiently, we will create an :file:`urls.py` module in our 
`basics` app. Within this module, we will create the path to our homepage.
This :file:`urls.py` module in our app directory will be referenced
by the more general :file:`urls.py` in the "site" directory.

#.  Create a file called :file:`urls.py` in our app directory named `basics`

    .. image:: _static/creating-a-page/create-urls-module.png
      :width: 400
      :alt: Create new urls.py module in app directory

#.  In the :file:`urls.py` file we just created, add the following code:

    .. code-block:: python

      from django.urls import path
      from basics.views import HomeTemplate


      urlpatterns = [
          path('', HomeTemplate.as_view(), name='home-template'),
      ]

    The crux of this file is the `urlpatterns` list, which contains a collection
    of elements that match paths to their views.

    The ``path`` function used here has 3 key arguments:


    #.  The first one indicates the route which is the string pattern we want to match
        against. Since we want the home page to be displayed by default to the user,
        we will leave this as an empty string.

    #.  The second argument is our view function. We have not written it yet but will do
        soon.

    #.  The last keyword argument is the name we will give to this URL pattern. Here, we
        name it ``home-template`` as it relates to the template view of our homepage.


#.  Add the following to the ``urls.py`` in the "site" directory:

    .. code-block:: python
      :emphasize-lines: 2, 7

      from django.contrib import admin
      from django.urls import path, include


      urlpatterns = [
          path('admin/', admin.site.urls),
          path('', include('basics.urls')),
      ]

    Notice how we have modified the second import statement by adding the ``include``
    function. Also, we appended a new URL pattern to the ``urlpatterns`` list: this
    essentially forwards on "empty" paths to the :file:`urls.py` module in the basics app
    and handled there instead.


***************
Creating a View
***************

We will create a view to return a given template to the end user.

#.  Add the following code to :file:`views.py`

    .. code-block:: python

      from django.views.generic import TemplateView


      class HomeTemplate(TemplateView):
          template_name = 'basics/home-template/home-template.html'

    Notice that this code overwrites the pre-generated code that Django provides in this
    module. The ``template_name`` class attribute is a path to the template, which we will
    create soon.

.. note::

  There are two main ways to create views: function-based or class-based.
  
  In this guide, we will be using class-based views. Although function-based views
  are simpler, we eventually end up using class-based views and will have to confront the
  use of Python classes when we create models. Nevertheless, function-based views are useful
  to see the mechanics of how requests are taken and responses given: you will see them
  in many tutorials, such as at the start of the official Django one.


*********************
Creating the Template
*********************

Now we need to create the template that our view references.

#.  Create the folder structure `templates/basics/home-template`
    within the `basics` app directory:

    .. image:: _static/creating-a-page/templates-structure.png
      :width: 400
      :alt: Templates folder structure

    Notice that this code overwrites the pre-generated code that Django provides in this
    module. The ``template_name`` class attribute is a path to the template, which we will
    create soon.

#.  In the `home-template` directory we just created, include the this
    :download:`home-template.html <_static/creating-a-page/home-template-01.html>` file.

    .. image:: _static/creating-a-page/home-template.png
      :width: 400
      :alt: Templates folder structure

Although it might seem unnecessary, it is important to create the folder structure before hand.

* The first of these directories - `templates` - is the name required for Django so that it is 
  correctly identified as a directory containing our HTML files.

* The next subdirectory `basics` indicates the app - this allows us to specifically reference templates for the `basics` app
  (it avoids the possible ambiguity that two apps contain the a template with the same name).

* Finally, the `home-template` directory ensures that all files related to the home template view
  are contained here. Although we only have one HTML file for this view, subsequent views may
  be more complex and have multiple files. 


**************************
Understanding the Template
**************************

Let us examine further the content of our HTML file as it contains some important details.

===========
Bootstrap 5
===========

As you know, an HTML file works in tandem with a CSS style sheet to provide our page with
some formatting. Also, we use JavaScript with our HTML file to provide more advanced
functionality to our page.

For our convenience, we use `Bootstrap 5 <https://getbootstrap.com/>`_ which is a frontend framework that provides us
with the CSS and JS already so we do not need to write it our self.

Including Bootstrap via CDN
---------------------------

We do not neccessarily have to download the Bootstrap files ourselves. We can use their
CDN which essentially allows us to load these files using an URL within our HTML.


We can see within :file:`home-template.html` where we have loaded the CSS from the Bootstrap 5
using the ``link`` element under within the ``head`` element of the template and also Bootstrap
icons:

.. literalinclude:: _static/creating-a-page/home-template-01.html
  :language: html
  :lines: 1-8
  :emphasize-lines: 7,8

Likewise, we can see within :file:`home-template.html` where we have loaded the JavaScript from the Bootstrap 5
using the ``script`` element just before the closing tag of the ``body`` element:

.. literalinclude:: _static/creating-a-page/home-template-01.html
  :language: html
  :lines: 36-
  :emphasize-lines: 1


Using Bootstrap
---------------

Once we have included these Bootstrap files in our template, we can freely use it with our
other elements. Although both important, we rely more on Bootstrap's CSS to provide styling
and are less focussed on the JavaScript.

For example, we can see our first ``div`` element having with a ``class`` attribute set to
``container``:

.. code-block:: html
  :emphasize-lines: 1

  <div class="container">
    ...
  </div>

This is a ``container`` class provided by Bootstrap automatically sets margins, padding,
maximum width etc. for our specified element. To find out more about this class, you
can visit the official Bootstrap documentation page on
`containers <https://getbootstrap.com/docs/5.3/layout/containers/>`_.


Another more interesting example are classes that appear for the ``header`` element:

.. code-block:: html
  :emphasize-lines: 2

   <div class="container">
        <header class="d-flex flex-wrap justify-content-between py-3 mb-4 border-bottom">
          ...
        </header>
    </div>
  
Each of the classes are briefly explained but it is always worth looking at their official
documentation:

* **d-flex**

  * sets element as a flexbox container and direct children elements as flex items
  * this allows us to easily change the layout behaviour of our elements

* **flex-wrap**

  * force flex items onto a new line
  * if the viewport - i.e. screen - becomes smaller, the elements in the header
    will move on to a new line
  * this is the same concept as wrapping text in say Microsoft Word

* **justify-content-between**

  * align flex items centrally along the main axis
  * this means that the first child element will be on the far left of
    our ``div`` and the last child element on the far right
    (any middle elements will be spaced evenly)

* **py-3**

  * vertical padding (i.e. in the y-axis) of 3

* **mb-4**

  * bottom margin of 4

* **border-bottom**

  * add border to bottom of element

Bootstrap has many versions with the latest major version being 5.
It is important to use documentation from this latest version: previous versions
have different class names that may not work with newest version.

========================
Django Template Language
========================

To make pages dynamic, Django provides its own template language. This turns our regular
HTML file into a template, where certain parts of it can change.

The two key concepts are:

#.  **Variables**

    * insert an arbitrary value we can provide via Python
    * denoted by double opening and closing curly brackets: **{{** **}}**

#.  **Tags**

    * perform arbitrary logic within our template
    * these can be thought of as like functions
    * denoted by curly bracket and percent sign: **{%** **%}**


For now, we will focus on the latter concept of tags as only they make an appearance
in our template as shown below:

.. literalinclude:: _static/creating-a-page/home-template-01.html
  :language: html
  :lines: 11-22
  :emphasize-lines: 3, 7

This special ``url`` tag allows us to insert an URL in our HTML simply by referencing
the name of our URL pattern. Recall that in our app's ``urls.py`` module, we named the
home template's URL pattern as ``home-template``. This means that, when the either of the
two relevant elements in the snippet above are clicked, they will navigate the user to the
home page.

Of course, it is entirely possible to manually type in the home page URL as the `href`
value. Such an idea, however, would be unwise as we want to refer to the URL pattern name
instead: the path a page is associated with may change in the future. If that
were to happen, then we would have to manually change all the `href` values in our HTML
files.


****************
Viewing our Page
****************

#.  Start the server (if it is not already running)

#.  Navigate to `localhost:8000 <http://localhost:8000/>`_
