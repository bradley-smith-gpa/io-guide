#################
Adding More Pages
#################


********************
Template Inheritance
********************

Before we dive in and start creating more pages, we need to revamp our current template
setup.

At the moment, we simply have one file that is directly served by our one-and-only
view. But if we were to naively create one template for each view, we would end up with
a lot of duplicate content. For example, our ``head`` element containing the link to the
Bootstrap style sheet would be repeated in each of our templates. So if we were to upgrade
to a newer version of Bootstrap, we would have to make these changes in multiple HTML files.

To avoid this situation, we can use template inheritance using Django's template language
to minimise the amount of HTML we need to write.

#.  Create a `base` subdirectory in our app's `templates` directory
    (besides our `home-template` directory)

#.  Add the :download:`base.html <_static/base.html>` into this subdirectory.

    .. literalinclude:: _static/base.html
      :language: html
      :emphasize-lines: 23, 24

    Notice the ``block`` tags which indicate where a chunk of HTML
    \- referenced under the name ``content`` - should be inserted
    (we will define this ``content`` in the next step).


#.  Edit the :download:`home-template.html <_static/adding-more-pages/home-template.html>` to only include
    the distinct block of content and removing the HTML already in :file:`base.html`.

    .. literalinclude:: _static/adding-more-pages/home-template.html
      :language: html
      :emphasize-lines: 1, 3, 17

    The ``extends`` tag indicates Django to use the :file:`base.html` file we created as
    the basis for this home template. Crucially, the following ``block`` tags surround
    the HTML that should be inserted into the identified :file:`base.html` file.

    Overall, this leads to the exact same result as we had before and should work fine.
    The only difference is that we have managed to separate the boilerplate HTML from the
    HTML we expect to vary between our different views.

*******************
Creating More Views
*******************

Now let's add two extra templates: these will be for our about page and contact page.

#.  Create the following subdirectories within the `templates/basics` directory of the
    `basics` app:

    * about-template
    * contact-template

    .. image:: _static/adding-more-pages/updated-templates-structure.png
      :width: 400
      :alt: Template directory with contact and about subdirectories

#.  Add each of the two HTML files to their respective directory:

    * :download:`about-template.html <_static/adding-more-pages/about-template.html>`
    * :download:`contact-template.html <_static/adding-more-pages/contact-template.html>`

    .. image:: _static/adding-more-pages/home-and-about-templates.png
      :width: 400
      :alt: Template directory with contact and about subdirectories

#.  In :file:`views.py` of our app, add in the two views:

    .. literalinclude:: _static/adding-more-pages/views.py
      :language: python
      :emphasize-lines: 8-13 

#.  In :file:`urls.py` of our app, add in the URL patterns:

    .. literalinclude:: _static/adding-more-pages/urls.py
      :language: python
      :emphasize-lines: 7-8 

************************
Adding URLs to Our Views
************************

By completing the previous steps, we should be able to navigate to both pages.
The only way to reach them, however, is by linking to them directly 
\- i.e. `localhost:8000/about/ <http://localhost:8000/about/>`_ and 
`localhost:8000/contact/ <http://localhost:8000/contact/>`_.
Of course, we do not want the user to rely on typing in the address bar to find
our pages.

All we need to do is to insert their URLs in our header in :file:`base.html` so that
we can navigate to them by clicking their respective links.

#.  In :file:`base.html`, use the ``url`` template tag like before to set the ``href``
    attribute values:

    .. literalinclude:: _static/adding-more-pages/base.html
      :language: html
      :lines: 11-22
      :emphasize-lines: 8-9
