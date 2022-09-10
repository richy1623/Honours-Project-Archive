
import unittest

#set system path
import sys
oldsyspath=''
if sys.path[0].split('/')[-1]=='test':
	oldsyspath=sys.path[0]
	sys.path[0]='/'.join(sys.path[0].split('/')[:-1])
	print('set path to: '+sys.path[0])
	
from test import cleardl, filldl
from util.usermanager import *
from util.cookiemanager import *

import os

class test_getcookies(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cleardl.clearusers()
		counter = createuser('PTRRIC011')
		os.environ['HTTP_COOKIE'] = 'userID='+counter+'; admin=1; username=PTRRIC011; verify=66714227792424116092'

	def test_normal_case(self):
		cookies = getcookies()
		self.assertEqual(cookies['userID'], getstudentid('PTRRIC011'))
		self.assertEqual(cookies['admin'], '1')
		self.assertEqual(cookies['username'], 'PTRRIC011')

class test_getUserID(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cleardl.clearusers()
		counter = createuser('PTRRIC011')
		os.environ['HTTP_COOKIE'] = 'userID='+counter+'; admin=1; username=PTRRIC011; verify=66714227792424116092'

	def test_normal_case(self):
		result = getUserID()
		self.assertEqual(result, getstudentid('PTRRIC011'))

class test_isadmin(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cleardl.clearusers()
		os.environ['HTTP_COOKIE'] = 'userID=11; admin=1; username=PTRRIC011; verify=66714227792424116092'

	def test_normal_case(self):
		result = isadmin()
		self.assertEqual(result, True)

class test_getusername(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cleardl.clearusers()
		os.environ['HTTP_COOKIE'] = 'userID=11; admin=1; username=PTRRIC011; verify=66714227792424116092'

	def test_normal_case(self):
		result = getusername()
		self.assertEqual(result, 'PTRRIC011')

if oldsyspath!='':
	sys.path[0]=oldsyspath
