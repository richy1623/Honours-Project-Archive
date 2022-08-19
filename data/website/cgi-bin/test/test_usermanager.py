
import unittest

#set system path
import sys
if sys.path[0].split('/')[-1]=='test':
	sys.path[0]='/'.join(sys.path[0].split('/')[:-1])
	print('set path to: '+sys.path[0])
	
from test import cleardl, filldl


def test_createuser(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		#setup any data structures for class
		True

	def test_normal_case(self):
		#code goes here


def test_deleteuser(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		#setup any data structures for class
		True

	def test_normal_case(self):
		#code goes here


def test_getstudentid(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		#setup any data structures for class
		True

	def test_normal_case(self):
		#code goes here


def test_getstudentemail(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		#setup any data structures for class
		True

	def test_normal_case(self):
		#code goes here


def test_getstudentname(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		#setup any data structures for class
		True

	def test_normal_case(self):
		#code goes here


def test_getallstudents(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		#setup any data structures for class
		True

	def test_normal_case(self):
		#code goes here


def test_getYearAndProject(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		#setup any data structures for class
		True

	def test_normal_case(self):
		#code goes here


def test_getYearAndProject2(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		#setup any data structures for class
		True

	def test_normal_case(self):
		#code goes here
