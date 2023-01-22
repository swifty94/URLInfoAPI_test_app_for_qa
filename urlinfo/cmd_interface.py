#!/usr/bin/env python
#
# GNU General Public License v3.0
# Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. 
# Copyright and license notices must be preserved. 
# Contributors provide an express grant of patent rights.
#
from base import LoggerFactory
from dns_info import DNSInfo, dumps
from http_info import HTTPHeader
from sys import argv
from web_api import app, WebApi

class CMDOPTS(object):
    def __str__(self) -> str:
        return """
Usage:\n
python urlinfo $param1 $param2*\n
    - $param1 - String | mode to use the program.\n
        - cmd -> using in terminal. You'll receive result to STDOUT in your terminal.
        - web -> using via web browser using API endpoint. Use "python urlinfo web help" for more details.
    - $param2* - String | !Mandatory for ONLY for 'cmd' mode!
        - Basically any URL from your web-browser you wanna check. Just copy and paste as an argumet to CMD.
        """

class WEBHelper(object):
    def __str__(self) -> str:
        return """
Usage:\n
python web
    - once it is done, the URL you need to use in order to reach API will be printed to STDOUT
    - open your web browser and paste this url, but don't press Enter yet.
    - in order to pass the desired URL for check simply add the following to the very end of endpoint:\n
        ?url="<paste your URL here>"\n
    - example:\n
        http://127.0.0.1:5000/api/urlinfo?url="https://packaging.python.org/en/latest/tutorials"
        """

class CMDInterface:
    """
    Class with basic API to set/get info to STDIN/STDOUT
    """
    def __init__(self) -> None:
        self.log = LoggerFactory.get_logger(__class__.__name__, log_level="INFO")
        self.log.info("CMDInterface instance created")

    def toSTDOUT(self) -> str:
        try:
            self.log.info("'cmd' mode enabled")
            url = argv[2]
            dns = DNSInfo(url)
            http = HTTPHeader(url)
            dnsInfo = dns.get() 
            httpInfo = http.get()          
            print('*'*20+"DNS INFORMATION"+'*'*20+"\n")
            print(dumps(dnsInfo, indent=4))
            print('*'*20+"HTTP HEADER INFORMATION"+'*'*20+"\n")
            print(dumps(httpInfo, indent=4))
            exit(0)
        except IndexError:
            self.log.error("Missing URL parameter! 'cmd' mode disabled")
            print("Missing URL parameter!")
            print(CMDOPTS())
            exit(1)

    def runWeb(self) -> None:
        try:
            self.log.info("'web' mode enabled")
            web = WebApi(app)
            web._serve() 
        except Exception as e:
            self.log.error(f"Exception: {e}", exc_info=1)
            self.log.info("'web' mode diabled")
            exit(1)

    def scan(self) -> None:
        try:
            cli_arg = argv[1]
            if cli_arg == 'web':
                self.runWeb()
            elif cli_arg == 'cmd':
                self.toSTDOUT()
            elif argv[2] == 'help':
                print(WEBHelper())
        except IndexError:
            self.log.error("No arguments provided!")
            print(CMDOPTS())
            exit(1)
        finally:
            self.log.info("CMDInterface instance destroyed")
