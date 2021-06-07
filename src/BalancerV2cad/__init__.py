"""
Package wide configurations
"""
from pathlib import PosixPath

__version__ = '0.1.0'

# This dumps the log file to the root directory of the project
BASE_DIR = PosixPath(__file__).resolve(strict=True).parent.parent.parent

# uncomment this line to dump the log file to ~/.config/__package__
#BASE_DIR = PosixPath().home() / '.config' / __package__

DEFAULT_LOGGER_NAME = 'dev'
LOGGING_FILE_NAME = f'{__package__}-{__version__}.log'

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "colored": {
            "()": "colorlog.ColoredFormatter",
            'format':
            "%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s"
        },
        "simple": {
            "format": "%(levelname)s - %(message)s"
        },
        "pedantic": {
            "format":
            "%(asctime)s - %(module)s - %(funcName)s - %(name)s - %(lineno)d - %(levelname)s - %(message)s"
        }
    },
    "handlers": {
        "console-color": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "colored",
            "stream": "ext://sys.stdout"
        },
        "file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "filename": "{0}".format(BASE_DIR / LOGGING_FILE_NAME),
            "formatter": "pedantic"
        }
    },
    "loggers": {
        # dev
        "{}".format(DEFAULT_LOGGER_NAME): {
            "handlers": [
                "console-color",
                "file_handler",
            ],
            "level": "DEBUG",
            "propagate": False
        },
        "production": {
            "handlers": [
                "file_handler",
            ],
            "level": "DEBUG",
            "propagate": False
        }
    },
    "root": {
        "handlers": ["file_handler"]
    }
}
