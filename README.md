# A preconfigured python package

> All dev dependencies are installed, for testing, and logging, as well as static anaylsis tools like mypy.

## This project is built and managed with python poetry

[Read the Docs](https://python-poetry.org/docs/cli/)

``` bash
# After poetry is installed and your virtual environment is activated, install all the project dependencies
poetry install

# If you want to want to add a new python package

poetry add requests

# If you want to add a new python package only for development (dev dependency)
poetry add mypy -D
```

## Simple tests are already set up, with an example conftest.py


``` bash
# run the tests
pytest

# the __version__ and pkg_name variables are defined in the root __init__.py
src/kickstart/__init__.py
```

## A logger utilizing colorlog and colorama are already set up

``` python
# The default logging config dictionary is also defined in the root __init__.py
# simple import it into your new module as so...

from kickstart.logger import package_logger as pl
logger = pl.PackageLogger().get_logger()
```

