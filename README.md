# MyOwn
A social network developed using [Flask](http://flask.pocoo.org/), sqlite3 and [Materialize](https://materializecss.com/)

# Description

I tried to use MTV model, Model, Template and View, Flask to up the server and connect with jinja2, all the process to catch datas from database I used the sqlite3 native from Python, MyOwn is a social network based on material design, because of this I choose use the CSS framework Materialize.

# Install

First of all you have to install virtualenv in your machine

```sudo apt-get install virtualenv```

After you have to active the virtualenv using:

```source venv/bin/activate```

Now install the packages using pip:

```pip install -r requirements.txt```

# Run server

If you want the Debug mode in MyOwn, you have to do:

``` export FLASK_ENV=development ```

Run the server:

```FLASK_APP=run.py flask run```
