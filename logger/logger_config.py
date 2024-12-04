"""Config Logger module"""

import logging


class LoggerConfig:
    """
    Class with logger config parameters
    """

    LOG_NAME = "TestLogger"
    LOG_DIR_NAME = "logs"
    LOG_FILE_PREFIX = "test_log"
    LOG_FILE_EXTENSION = ".log"
    LOG_DATE_FORMAT = "%Y%m%d_%H%M%S"
    LOG_FORMAT = '[%(asctime)s:] %(module)s:%(lineno)d %(levelname)s - %(message)s'
    LOG_ENCODING = "utf-8"
    LOG_LEVEL = logging.DEBUG
