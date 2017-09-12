import logging.config


def setup_logging():
    DEFAULT_LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
            },
            'colored': {
                '()': 'colorlog.ColoredFormatter',
                'format': "%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s"
            }
        },
        'handlers': {
            'default': {
                'level': 'DEBUG',
                'formatter': 'colored',
                'class': 'logging.StreamHandler',
            },
        },
        'loggers': {
            '': {
                'level': 'DEBUG',
            },
            'sn_agent': {
                'level': 'DEBUG',
            },
        },
        'root': {
            'handlers': ['default'],
            'level': 'DEBUG',
        },
    }
    logging.config.dictConfig(DEFAULT_LOGGING)
