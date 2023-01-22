|Build Status| 

.. |Build Status| image:: https://app.travis-ci.com/github/swifty94/URLInfoAPI_test_app_for_qa.svg?branch=master
   :target: https://app.travis-ci.com/github/swifty94/URLInfoAPI_test_app_for_qa

About
=====

Simple program with CMD / Web API.
Allows to parse any URL into the valid FQDN and get:
- DNS information
- HTTP header information

GNU General Public License v3.0
Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. 
Copyright and license notices must be preserved. 
Contributors provide an express grant of patent rights.

Requirements
============

-  Python 3.X
-  Compatible with Linux/OSX/ Windows (Python must be installed on Windows additionally, as it is not comming out of box)

Installation
============
<pre>
C:\Users\kiril\Documents\LenovoData\urlinfolib>python setup.py install

/// long output of installation goes here...

C:\Users\kiril\Documents\LenovoData\urlinfolib>ls -l
total 68
-rw-rw-rw-   1 user     group         265 Jan 22 21:46 CHANGES.md
-rw-rw-rw-   1 user     group       35149 Jan 19 23:28 LICENSE
-rw-rw-rw-   1 user     group          99 Jan 19 23:52 MANIFEST.in
-rw-rw-rw-   1 user     group        5562 Jan 22 22:04 README.md
drwxrwxrwx   1 user     group           0 Jan 22 22:10 build
drwxrwxrwx   1 user     group           0 Jan 22 22:10 dist
-rw-rw-rw-   1 user     group         281 Jan 19 23:47 requirements.txt
-rw-rw-rw-   1 user     group        1618 Jan 22 22:07 setup.py
drwxrwxrwx   1 user     group           0 Jan 22 22:08 tests
-rw-rw-rw-   1 user     group       22087 Jan 22 21:42 url_info.log
drwxrwxrwx   1 user     group           0 Jan 22 22:08 urlinfo
drwxrwxrwx   1 user     group           0 Jan 22 22:10 urlinfo.egg-info
drwxrwxrwx   1 user     group           0 Jan 22 22:08 venv

C:\Users\kiril\Documents\LenovoData\urlinfolib>
</pre>
Usage
=====

<pre>
C:\Users\admin\UrlInfoAPI>python urlinfo

Usage:

python urlinfo $param1 $param2*

    - $param1 - String | mode to use the program.

        - cmd -> using in terminal. You'll receive result to STDOUT in your terminal.
        - web -> using via web browser using API endpoint. Use "python urlinfo web help" for more details.
    - $param2* - String | !Mandatory for ONLY for 'cmd' mode!
        - Basically any URL from your web-browser you wanna check. Just copy and paste as an argumet to CMD.


C:\Users\admin\UrlInfoAPI>
</pre>

Basics
------
- using CMD interface

<pre>
C:\Users\admin\Desktop>cd UrlInfoAPI

C:\Users\admin\Desktop\UrlInfoAPI>python urlinfo cmd https://app.travis-ci.com
********************DNS INFORMATION********************

{
    "FQDN": "travis-ci.com",
    "DNS records": {
        "A-1": "104.26.7.20",
        "A-2": "104.26.6.20",
        "A-3": "172.67.75.36",
        "AAAA-1": "2606:4700:20::ac43:4b24",
        "AAAA-2": "2606:4700:20::681a:714",
        "AAAA-3": "2606:4700:20::681a:614",
        "NS-1": "lee.ns.cloudflare.com.",
        "NS-2": "sandy.ns.cloudflare.com.",
        "MX-1": "10 aspmx2.googlemail.com.",
        "MX-2": "5 alt2.aspmx.l.google.com.",
        "MX-3": "1 aspmx.l.google.com.",
        "MX-4": "5 alt1.aspmx.l.google.com.",
        "MX-5": "10 aspmx3.googlemail.com.",
        "TXT-1": "\"pardot845883=ec1455733e354154d29e95536bb3ada7f816a0ea11e317bf96c8d3b7bd6aeb61\"",
        "TXT-2": "\"knowbe4-site-verification=c2601f709fa62bce1f741c2c778107e7\"",
        "TXT-3": "\"google-site-verification=h4ZSCqpTKMv94Hm_49xE5xvmww-cngOcXqcUqwnKf3o\"",
        "TXT-4": "\"globalsign-domain-verification=K9ZBZYNiNsNNOiaY2Tbjn-Bfe0dWwAwpstKoOOVJWO\"",
        "TXT-5": "\"google-site-verification=fX5II5Zm361C7EFqPVDFRvClFZqAs8M2PpdQ6DR5GD8\"",
        "TXT-6": "\"v=spf1 a mx include:helpscoutemail.com include:spf.mandrillapp.com include:stspg-customer.com include:mail.zendesk.com include:aspmx.pardot.com ~all\"",
        "TXT-7": "\"status-page-domain-verification=pnpcptp8xh9k\"",
        "TXT-8": "\"keybase-site-verification=OyuCesVNzPfge5X9BozBqMphd-I_RaCUK0ALkV0OyYA\"",
        "TXT-9": "\"_globalsign-domain-verification=95YZs-Lq6mpDrrS5bnsvxSp8Llz8ZsgkwBGGx8RQVh\"",
        "TXT-10": "\"google-site-verification=bWl85QvPMsRO4akiMIAWeDRba2ZcLjSheaZ-3yceM-Q\"",
        "TXT-11": "\"2231c2e1908a4f28a87da07bda9aeaa3\"",
        "SOA-1": "lee.ns.cloudflare.com. dns.cloudflare.com. 2295297193 10000 2400 604800 3600"
    }
}
********************HTTP HEADER INFORMATION********************

{
    "date": "Sun, 22 Jan 2023 19:21:46 GMT",
    "content-type": "text/html",
    "transfer-encoding": "chunked",
    "connection": "keep-alive",
    "strict-transport-security": "max-age=15724800; includeSubDomains, max-age=31536000",
    "cache-control": "public, must-revalidate, max-age=0",
    "content-location": "/",
    "last-modified": "Mon, 16 Jan 2023 07:31:15 GMT",
    "expires": "0",
    "vary": "Accept,Accept-Encoding",
    "etag": "74881b8d6f46edd07c428fab905c349b",
    "x-frame-options": "SAMEORIGIN",
    "x-xss-protection": "1; mode=block",
    "x-content-type-options": "nosniff",
    "content-encoding": "gzip"
}

C:\Users\kiril\Desktop\UrlInfoAPI>
</pre>

- using Web API interface

<pre>
C:\Users\admin\Desktop>cd UrlInfoAPI

C:\Users\admin\Desktop\UrlInfoAPI>python urlinfo web                          
********************Starting WebApi object <Flask 'web_api'>, host='0.0.0.0', port='5000********************
********************Please try URL like http://localhost:5000/api/v1/ur?linfo=<YOUR_URL_HERE>********************
</pre>

Then open and your browser and do something like below 

![](https://github.com/swifty94/URLInfoAPI_test_app_for_qa/blob/master/urlinfo/sample_1.png)

![](https://github.com/swifty94/URLInfoAPI_test_app_for_qa/blob/master/urlinfo/sample_2.png)

Once you done, just do "CTRL+C" in you terminal and you'll see something like below:

<pre>
C:\Users\admin\Desktop\UrlInfoAPI>python urlinfo web
********************Starting WebApi object <Flask 'web_api'>, host='0.0.0.0', port='5000********************
********************Please try URL like http://localhost:5000/api/v1/ur?linfo=<YOUR_URL_HERE>********************
********************SERVER STOPPED********************

C:\Users\admin\Desktop\UrlInfoAPI>
</pre>

Running tests::
=============

    C:\URLInfoAPI_test_app_for_qa>python urlinfo\tests\run_all.py

Reporting issues
================

Please report any issues in the issue tracker `<https://github.com/swifty94/URLInfoAPI_test_app_for_qa/issues/new>`.

