import logging

def set_logging_config(filename, filemode = 'w', format='%(asctime)s %(name)s %(threadName)s [%(levelname)s] %(message)s', level=logging.DEBUG, log_to_console = True):
    logging.basicConfig(filename = filename, filemode = filemode, format=format, level = level)

    tf_logger = logging.getLogger('tensorflow')
    for handler in tf_logger.handlers:
        handler.setFormatter(logging.Formatter(format))

    if log_to_console:
        console = logging.StreamHandler()
        console.setLevel(level)
        console.setFormatter(logging.Formatter(format))
        logging.getLogger().addHandler(console)

