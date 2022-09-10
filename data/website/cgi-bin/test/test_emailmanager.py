
import unittest

#set system path
import sys
oldsyspath=''
if sys.path[0].split('/')[-1]=='test':
	oldsyspath=sys.path[0]
	sys.path[0]='/'.join(sys.path[0].split('/')[:-1])
	print('set path to: '+sys.path[0])
	
from util.emailmanager import sendemail

class test_sendemail(unittest.TestCase):
	def test_normal_case(self):
		result = sendemail('PTRRIC011@myuct.ac.za', 'Unittest', 'Successfull sending of email')
		self.assertTrue(result)
		
	def test_list_of_recipients(self):
		result = sendemail(['PTRRIC011+1@myuct.ac.za','PTRRIC011+2@myuct.ac.za'], 'Unittest', 'Successfull sending of multiple emails')
		self.assertTrue(result)
		
	def test_no_recipients(self):
		result = sendemail([], 'Unittest', 'Successfull sending of email')
		self.assertFalse(result)

if oldsyspath!='':
	sys.path[0]=oldsyspath
