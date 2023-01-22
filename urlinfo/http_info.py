import requests
from base import LoggerFactory
from json import dumps
logger = LoggerFactory.get_logger(__name__, log_level="INFO")

class HTTPHeader():
    def __init__(self, url) -> None:
        self.url = url
        self.logger = LoggerFactory.get_logger(__class__.__name__, log_level="INFO")
    
    def get(self):
        try:        
            response = requests.get(self.url)
            header = dict(response.headers)
            header = {k.lower(): v for k, v in header.items()}
            if len(header) == 0:
                header["Response"] = "No data found"
                return header
            return header
        except Exception as e:
            self.logger.exception(f"Exception: {e} \n Full stack trace:", exc_info=2)
        finally:
            self.logger.info('Finished processing URL: ' + self.url)