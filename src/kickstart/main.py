"""
Example Driver code
"""

from kickstart import PKG_NAME, __version__
from kickstart.logger import pkg_logger as pl

logger = pl.PackageLogger().get_logger()


def run() -> None:
    """
    Example function to execute through poetry scripts
    """
    logger.info('Testing for %s@%s', PKG_NAME, __version__)
    logger.debug('Testing for %s@%s', PKG_NAME, __version__)
    logger.warning('Testing for %s@%s', PKG_NAME, __version__)
    logger.error('Testing for %s@%s', PKG_NAME, __version__)
