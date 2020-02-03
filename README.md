# heroku-bank-api
This is a demo project using DRF which includes two API end-point i.e. Search API and Autocomplete API. It is hosted on Heroku.
e.g.
```sh
curl -v https://pure-ravine-81384.herokuapp.com/api/branches/?q=bangalore&limit=3&offset=0
curl -v https://pure-ravine-81384.herokuapp.com/api/branches/autocomplete/?q=bangalore&limit=5&offset=1
```


## Running Locally

Make sure you have Python 3.8 [installed locally](http://install.python-guide.org). To push to Heroku, you'll need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), as well as [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).
Note: Database need to create manually. [Check this out](https://github.com/snarayanank2/indian_banks)

```sh
$ git clone https://github.com/skdehuri/heroku-bank-api.git
$ cd heroku-bank-api

$ python3 -m venv env
$ pip install -r requirements.txt

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
