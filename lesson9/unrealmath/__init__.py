import logging.config

logging.getLogger(__name__).addHandler(logging.NullHandler())

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'default': {
            'format': '%(asctime)s - %(message)s'
        },
    },
    'handlers': {
        'addition': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'INFO',
            'formatter': 'default',
            'filename': 'addition.log',
            'maxBytes': 1024,
            'backupCount': 3
        },
        'subtraction': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'INFO',
            'formatter': 'default',
            'filename': 'subtraction.log',
            'maxBytes': 1024,
            'backupCount': 3
        }
    },
    'loggers': {
        'unrealmath.addition': {
            'handlers': ['addition'],
            'level': 'INFO',
            'propagate': False
        },
        'unrealmath.subtraction': {
            'handlers': ['subtraction'],
            'level': 'INFO',
            'propagate': False
        }
    }
}
