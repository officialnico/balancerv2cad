# A preconfigured python package

> All dev dependencies are installed, for testing, and logging, as well as static anaylsis tools like mypy.

## This project is built and managed with python poetry

[Read the Docs](https://python-poetry.org/docs/cli/)

``` bash
# After poetry is installed and your virtual environment is activated, install all the project dependencies
poetry install

# If you want to want to add a new python package
poetry add python-dotenv

# If you want to add a new python package only for development (dev dependency)
poetry add mypy -D
```

## Using dotenv

> kickstart uses a .env file to showcase how to access dev environment variables similar
> to proccess.env in javascript. src/kickstart/main.py showcases the usage. for it to work
> create the a .env file in the project root with the following contents

```bash
CAPTAIN_ONE=Picard
CAPTAIN_TWO=Sisco
```

## Simple tests are already set up, with an example conftest.py

> the pyproject.toml offers a way to define scripts in a similar fashion to an npm
> package.json

``` bash
# use poetry python scripts to run the example tests
$ poetry run tests

# use poetry python scripts to run the example driver program
$ poetry run drive

# when drive is ran it will dump a log file in the project root, to change the
# the destination of this file, change the value of BASE_DIR in src/kickstart/__init__.py

# python __init__.py files have the same function as javascript index.js files
# the __version__ variable and logging config are defined in src/kickstart/__init__.py
```

## A logger utilizing colorlog and colorama are already set up

``` python
# The default logging config dictionary is also defined in the root __init__.py
# simple import it into your new module as so...

from kickstart.logger import package_logger as pl
logger = pl.PackageLogger().get_logger()
```

