# MyOwn
A social network developed using [Flask](http://flask.pocoo.org/), sqlite3 and [Materialize](https://materializecss.com/)

# Description

I tried to use MTV, Model, Template and View, Flask to up the server and connect with jinja2, all the process to catch datas from database I used the sqlite3 native from Python, MyOwn is a social network based on material design, because of this I choose use the CSS framework Materialize.

# Install

Packages:

```
asn1crypto==0.24.0
backports.functools-lru-cache==1.5
cryptography==2.1.4
cycler==0.10.0
enum34==1.1.6
idna==2.6
ipaddress==1.0.17
keyring==10.6.0
keyrings.alt==3.0
kiwisolver==1.0.1
matplotlib==2.2.3
numpy==1.15.3
pycrypto==2.6.1
pygobject==3.26.1
pyparsing==2.3.0
python-dateutil==2.7.5
pytz==2018.7
pyxdg==0.25
SecretStorage==2.3.1
six==1.11.0
subprocess32==3.5.3 

```

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

# Description dirs

## codesForDatabase

In this dir we have all functions that go pass the variables to database

## database

Here we have the database of project ```

## model

In model we have the function that will go create the database and tables

## static

Here is the dir that have style and scripts from CSS and JS

## templates

All the web layout

## venv

Here is our virtual environment

## view

Here we connect the routes with codesForDatabase to catch values to pass