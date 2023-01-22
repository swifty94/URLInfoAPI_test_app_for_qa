#!/usr/bin/env python
#
# GNU General Public License v3.0
# Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. 
# Copyright and license notices must be preserved. 
# Contributors provide an express grant of patent rights.
#
import logging
import logging.config
from os import path

class LoggerFactory:
    """
    Basic logger\n
    """
    logging.config.fileConfig(path.join(path.dirname(path.abspath(__file__)), 'logging.ini'))
    _LOG = None

    @staticmethod
    def __create_logger(cls_name,  log_level):
        """
        A private method that interacts with the python
        logging module
        """
        # get the logging format
        # Initialize the class variable with logger object
        
        LoggerFactory._LOG = logging.getLogger(cls_name)
        # set the logging level based on selection
        if log_level == "INFO":
            LoggerFactory._LOG.setLevel(logging.INFO)
        elif log_level == "ERROR":
            LoggerFactory._LOG.setLevel(logging.ERROR)
        elif log_level == "DEBUG":
            LoggerFactory._LOG.setLevel(logging.DEBUG)
        return LoggerFactory._LOG

    @staticmethod
    def get_logger(cls_name, log_level):
        """
        A static method called by other modules to initialize logger in separate class
        """
        logger = LoggerFactory.__create_logger(cls_name, log_level)
        return logger