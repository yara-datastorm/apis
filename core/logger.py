import logging


# setup loggers
def get_logger(name, level=logging.DEBUG) -> logging.Logger:
    # FORMAT = "[%(levelname)s  %(name)s %(module)s:%(lineno)s - %(funcName)s() - %(asctime)s]\t %(message)s \n"
    FORMAT = "[%(asctime)s.%(msecs)03dZ] %(name)s %(levelname)s %(message)s"
    TIME_FORMAT = "%d.%m.%Y %I:%M:%S %p"  # %Y-%m-%dT%H:%M:%S

    FILENAME = '/tmp/log.log'

    logging.basicConfig(format=FORMAT, datefmt=TIME_FORMAT, level=level,
    filename=FILENAME
    )

    logger = logging.getLogger(name)
    return logger

# [INFO  main main:69 - docs() - 08.08.2022 08:40:01 AM]
#          doc page