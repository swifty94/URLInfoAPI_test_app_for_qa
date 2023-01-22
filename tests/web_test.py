#!/usr/bin/env python
#
# GNU General Public License v3.0
# Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. 
# Copyright and license notices must be preserved. 
# Contributors provide an express grant of patent rights.
#
from urlinfo import mainStr
import unittest

class TestCase(unittest.TestCase):
    
    def testMain(self):
        self.assertEqual(mainStr(), "HelloFromMyLib")

if __name__ == '__main__':
    unittest.main()