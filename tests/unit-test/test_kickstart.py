"""
Showcasing two different ways to properly test your code

1. By importing the kickstart package in directly.
2. By passing in a function fixture defined in conftest.py
"""
from kickstart import __version__


def test_version():
    """
    testing version from importing it
    """
    assert __version__ == '0.1.0'


def test_version_using_fixture(version_test):
    """
    testing version from passing the module
    in as a fixture
    """
    assert version_test.__version__ == '0.1.0'


def test_pkgname_using_fixture(version_test):
    """
    testing pkgname from passing the module
    in as a fixture
    """
    assert version_test.PKG_NAME == 'kickstart'
