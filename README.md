# MyOwn
A social network developed using [Flask](http://flask.pocoo.org/), sqlite3 and [Materialize](https://materializecss.com/)

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
