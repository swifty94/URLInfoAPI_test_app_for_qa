#!/usr/bin/env python
#
# GNU General Public License v3.0
# Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. 
# Copyright and license notices must be preserved. 
# Contributors provide an express grant of patent rights.
#

from setuptools import setup, Command
from distutils.command.build_py import build_py

with open('README.md') as infile:
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
      packages=['urlinfo'],
      provides=['urlinfo'],
      install_requires=[
        'dnspython==2.3.0',
        'Flask==2.2.2'],
      cmdclass={'build_py': build_py},
      classifiers=[
                   "Programming Language :: Python 3",
                   "GNU General Public License v3.0",
                  ],
     )
