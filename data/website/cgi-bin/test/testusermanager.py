import unittest
import os

#set system path
import sys
if sys.path[0].split('/')[-1]=='test':
	sys.path[0]='/'.join(sys.path[0].split('/')[:-1])
	print('set path to: '+sys.path[0])
	
from test import cleardl, filldl
	
from util.usermanager import *
from util.projectmanager import *

usrdir = '../../data/users/'

class testCreateUser(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cleardl.main()
		
	def test_normal_case(self):
		counter = '11'
		
		result = createuser('PTRRIC011')
		self.assertEqual(result, '11', 'Creating user reports a fail')
		
		f = open(usrdir+counter+'.email.xml', 'r')
		email = f.readline()
		f.close()
		self.assertEqual(email, '<email>PTRRIC011@myuct.ac.za</email>', "incorrect email address")
		
		f = open(usrdir+counter+'.profile.xml', 'r')
		profile = f.readline()
		f.close()
		self.assertEqual(profile, '<profile></profile>', "incorrect profile")
		
		f = open(usrdir+counter+'.name.xml', 'r')
		name = f.readline()
		f.close()
		self.assertEqual(name, '<name>PTRRIC011</name>', "incorrect name")

class testDeleteUser(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cleardl.main()
		
	def test_normal_case(self):
		for filename in ['11.name.xml', '11.email.xml', '11.password.xml', '11.permissions.xml', '11.profile.xml', '11.token.txt']:
			f = open(usrdir+filename, 'a')
			f.write('')
			f.close()
			
		f = open(usrdir+'11.name.xml', 'w')
		f.write('<name>PTRRIC011</name>')
		f.close()
		
		os.makedirs(usrdir+'../projects/2022/')
		f = open(usrdir+'../projects/2022/PROJECTS.txt', 'w')
		f.write('PTRRIC011')
		f.close()
		
		result = deleteuser('PTRRIC011', '2022', 'PROJECTS')
		self.assertTrue(result, 'Deleting user reports a fail')
		
		for filename in ['11.name.xml', '11.email.xml', '11.password.xml', '11.permissions.xml', '11.profile.xml', '11.token.txt']:
			self.assertFalse(os.path.exists(usrdir+filename), filename+' not deleted')
		f = open(usrdir+'../projects/2022/PROJECTS.txt', 'r')
		self.assertFalse('PTRRIC011' in f.readlines(), 'Student permissions were not removed')
		f.close()
	
	def test_user_doesnt_exist(self):
		result = deleteuser('PTRRIC011', '2022', 'PROJECTS')
		self.assertTrue(result, 'Deleting user reports a fail')
			
if __name__ == '__main__':
	unittest.main()
