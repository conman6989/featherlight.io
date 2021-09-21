# lightfeather.io Code Challenge

Notification Form
======

A basic Notification Form app built in Python with Flask.

This app was built using the flaskr template as bones to build on quickly.

I also added a second Notifications Form written in Vanilla Javascript.
Both can be found at the top of the index page in the navagation bar.
the side bar has links to login / logout / register pages.
in that same bar I have added a link to my site github pages site. there you can find some other projects I have worked on reciently.

I currently Host 3 webapps from my home with Docker and Nginx with Certbot.
I would be more than happy to send you the demo logins for any of my sites.

 - https://brainasium.app/projects
 - https://www.iaai.io/ - requires demo login
 - https://elliott-wellman.app/ - requires demo login

## Install
-------

**Be sure to use the same version of the code as the version of the docs
you're reading.** You probably want the latest tagged version, but the
default Git version is the main branch. ::

    # clone the repository
    $ git clone https://github.com/conman6989/lightfeather.io.git

Create a virtualenv and activate it::

    $ python3 -m venv venv
    $ . venv/bin/activate

Or on Windows cmd::

    $ py -3 -m venv venv
    $ venv\Scripts\activate.bat

Install Requirements:

    pip install -e .

## Run
----

    $ export FLASK_APP=notification_form
    $ export FLASK_ENV=development
    $ flask init-db
    $ flask run

Or on Windows cmd::

    > set FLASK_APP=notification_form
    > set FLASK_ENV=development
    > flask init-db
    > flask run

I have included a small .bat file i use for convience as well.

Open http://127.0.0.1:5000 in a browser.

## Test
----

    $ pip install '.[test]'
    $ pytest

Run with coverage report:

    $ coverage run -m pytest
    $ coverage report
    $ coverage html  # open htmlcov/index.html in a browser
