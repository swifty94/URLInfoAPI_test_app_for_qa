#!/usr/bin/env python
#
# GNU General Public License v3.0
# Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. 
# Copyright and license notices must be preserved. 
# Contributors provide an express grant of patent rights.
#
from flask import Flask, request, jsonify
from base import LoggerFactory
from dns_info import DNSInfo
from http_info import HTTPHeader
from waitress import serve as waitress_serve

#
#   instantiate Flask and use as decorator further
#   all Flask inherited instance methods will be deploed via WebApi instance _serve() method
#

app = Flask(__name__)
app.config["DEBUG"] = True
_appLogger = LoggerFactory.get_logger(str(Flask), log_level="DEBUG")

@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>')
def catch_all(u_path):
     return jsonify({
                "Response": f"Incorrect request to API: {u_path}",
                "Tip #1": "Please use URL like: http://localhost:5000/api/v1/url?info=https://megogo.net/ua/",
                "Tip #2": "You just need to put ANY url you wish after http://localhost:5000/api/v1/url?info="
            })

@app.route('/api/v1/url', methods=['GET'])
def checkPage():
    """Process any URL based on relevant class methods"""
    try:
        _appLogger.info('/api/v1/url')
        if 'info' in request.args:
            url = str(request.args['info'])
            if len(url) > 0:
                dns = DNSInfo(url).get()
                http = HTTPHeader(url).get()
                result = {
                    "DNS information": dns,
                    "HTTP header details": http
                }
                return jsonify(result)
            else:
                return jsonify({
                    "Response": "Error. URL cannot be > 0 length"
                })        
    except Exception as e:
        _appLogger.exception(f"Exception: {e} \n Full stack trace:", exc_info=2)        
        return jsonify({
            "Result": "FAIL. Please check url_info.log for details"
        })

class WebApi(object):
    """
    Class with web API methods
    """
    def __init__(self, app: Flask) -> None:
        self.self = __class__.__name__
        self.loggger = LoggerFactory.get_logger(self.self, log_level="INFO")
        self.app = app
        self.loggger.info("WebApi instance created")
    
    def _serve(self):
        try:
            print("*"*20+f"Starting WebApi object {self.app}, host='0.0.0.0', port='5000"+"*"*20)
            self.loggger.info(f"Starting WebApi object {self.app}, host='0.0.0.0', port='5000'")
            print("*"*20+f"Please try URL like http://localhost:5000/api/v1/ur?linfo=<YOUR_URL_HERE>"+"*"*20)
            self.loggger.info("Please try URL like http://localhost:5000/api/v1/ur?linfo=<YOUR_URL_HERE>")
            waitress_serve(self.app, host='0.0.0.0', port='5000')
        except Exception as e:
            self.loggger.error(f"ERROR: {e}", exc_info=2)
        finally:
            print("*"*20+"SERVER STOPPED"+20*"*")
            self.loggger.info("SERVER STOPPED")
