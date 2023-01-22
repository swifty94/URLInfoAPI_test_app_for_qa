#!/usr/bin/env python
#
# GNU General Public License v3.0
# Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. 
# Copyright and license notices must be preserved. 
# Contributors provide an express grant of patent rights.
#

from base import LoggerFactory
from cmd_interface import CMDInterface

if __name__ == "__main__":
    try:
        logger = LoggerFactory.get_logger(__name__, log_level="INFO")
        logger.info("Program entry point __main__ start")
        cmd = CMDInterface()
        cmd.scan()
    except Exception as e:
        logger.error(f"Exception: {e}", exc_info=1)
    finally:
        logger.info("Program entry point __main__ end")