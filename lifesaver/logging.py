import logging


def setup_logging(time_formatting='%Y-%m-%d %H:%M', hush=None):
    """
    Sets up logging.

    The root logger's level is set to logging.DEBUG.
    The ``websockets`` and ``discord`` root loggers are set to ``logging.INFO``.

    :param time_formatting: Sets the time formatting.
    :param hush: A list of additional logger names to set to ``logging.INFO``.
    """
    # Set the root logger's info to INFO.
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)

    # formatters
    fmt = logging.Formatter('[{asctime}] [{levelname: <7}] {name}: {message}', time_formatting, style='{')

    # enable debug logging for us, but not for discord
    default_hush = ['websockets', 'discord']
    for log in (hush + default_hush if hush else default_hush):
        logging.getLogger(log).setLevel(logging.INFO)

    stream = logging.StreamHandler()
    stream.setFormatter(fmt)

    root_logger.addHandler(stream)
