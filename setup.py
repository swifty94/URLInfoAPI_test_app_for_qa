#!/usr/bin/env python
#
# GNU General Public License v3.0
# Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. 
# Copyright and license notices must be preserved. 
# Contributors provide an express grant of patent rights.
#

from setuptools import setup, Command
from distutils.command.build_py import build_py

with open('README.rst') as infile:
    long_description = infile.read()

from urlinfo import __version__

setup(name='urlinfo',
      version=__version__,
      description='UrlInfoAPI',
      long_description=long_description,
      url='https://github.com/swifty94/URLInfoAPI_test_app_for_qa',
      license='GNU General Public License v3.0',
      author='Kirill Rudenko',
      author_email='developer1swifty@gmail.com',
      packages=['urllib'],
      provides=['urllib'],
      install_requires=[
        'certifi==2022.12.7',
        'charset-normalizer==3.0.1',
        'click==8.1.3',
        'colorama==0.4.6',
        'dnspython==2.3.0',
        'Flask==2.2.2',
        'idna==3.4',
        'importlib-metadata==6.0.0',
        'itsdangerous==2.1.2',
        'Jinja2==3.1.2',
        'MarkupSafe==2.1.2',
        'requests==2.28.2',
        'tld==0.12.6',
        'urllib3==1.26.14',
        'Werkzeug==2.2.2',
        'zipp==3.11.0'],
      cmdclass={'build_py': build_py},
      classifiers=[
                   "Programming Language :: Python 3",
                   "GNU General Public License v3.0",
                  ],
     )
