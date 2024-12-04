import logging
import os
from datetime import datetime
from typing import Union

from logger.logger_config import LoggerConfig


class Logger:
    """Logger class"""
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    log_dir = os.path.join(root_dir, LoggerConfig.LOG_DIR_NAME)

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    timestamp = datetime.now().strftime(LoggerConfig.LOG_DATE_FORMAT)
    log_file = os.path.join(log_dir, f"{LoggerConfig.LOG_FILE_PREFIX}_"
                                     f"{timestamp}{LoggerConfig.LOG_FILE_EXTENSION}")

    logger = logging.getLogger(LoggerConfig.LOG_NAME)
    logger.setLevel(LoggerConfig.LOG_LEVEL)

    file_handler = logging.FileHandler(log_file, encoding=LoggerConfig.LOG_ENCODING)
    file_handler.setLevel(LoggerConfig.LOG_LEVEL)

    formatter = logging.Formatter(LoggerConfig.LOG_FORMAT)
    file_handler.setFormatter(formatter)

    if not logger.hasHandlers():
        logger.addHandler(file_handler)

    @staticmethod
    def set_level(level: Union[str, int]) -> None:
        """
        Method set level
        :param level: Union[str, int]
        :return: None
        """

        Logger.logger.setLevel(level)

    @staticmethod
    def info(message: str) -> None:
        """
        Method info
        :param message: str
        :return: None
        """
        Logger.logger.info(msg=message)

    @staticmethod
    def debug(message: str) -> None:
        """
        Method debug
        :param message: str
        :return: None
        """
        Logger.logger.debug(msg=message)

    @staticmethod
    def warning(message: str) -> None:
        """
        Method warning
        :param message: str
        :return: None
        """
        Logger.logger.warning(msg=message)

    @staticmethod
    def error(message: str) -> None:
        """
        Method error
        :param message: str
        :return: None
        """
        Logger.logger.error(msg=message)
