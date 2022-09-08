
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
from util.projectmanager import createproject, addusertoproject

class test_createuser(unittest.TestCase):
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
		
		f = open(usrdir+counter+'.permissions.xml', 'r')
		permissionlines = f.readlines()
		f.close()
		self.assertEqual(permissionlines, [], "incorrect permissions")

class test_deleteuser(unittest.TestCase):
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

class test_getstudentid(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cleardl.clearusers()

	def test_normal_case(self):
		counter = createuser('PTRRIC011')
		self.assertNotEqual(counter, '', 'Failed to create user')
		
		self.assertEqual(getstudentid('PTRRIC011'), counter, 'Incorrect student ID returned')
		
	def test_user_doesnt_exist(self):
		self.assertEqual(getstudentid('NoSuchStudent'), '', 'Incorrect student ID returned')

class test_getstudentemail(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cleardl.clearusers()

	def test_normal_case(self):
		#code goes here
		counter = createuser('PTRRIC011')
		self.assertNotEqual(counter, '', 'Failed to create user')
		
		result = getstudentemail('PTRRIC011')
		self.assertEqual(result, 'PTRRIC011@myuct.ac.za', 'Incorrect student email returned')
		
	def test_user_doesnt_exist(self):
		self.assertEqual(getstudentemail('NoSuchStudent'), '', 'Incorrect student email returned')


class test_getstudentname(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cleardl.clearusers()

	def test_normal_case(self):
		counter = createuser('PTRRIC011')
		self.assertNotEqual(counter, '', 'Failed to create user')
		
		result = getstudentname(counter)
		self.assertEqual(result, 'PTRRIC011', 'Incorrect student name returned')
		
	def test_user_doesnt_exist(self):
		self.assertEqual(getstudentname('NoSuchStudent'), '', 'Incorrect student name returned')
		
class test_getallstudents(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cleardl.clearusers()

	def test_normal_case(self):
		counter = createuser('PTRRIC011')
		self.assertNotEqual(counter, '', 'Failed to create user')
		counter = createuser('LVZMON001')
		self.assertNotEqual(counter, '', 'Failed to create user')
		counter = createuser('NGLTAO001')
		self.assertNotEqual(counter, '', 'Failed to create user')
		
		result = getallstudents()
		if 'Admin' in result:
			result.remove('Admin')
		
		self.assertEqual(result, ['LVZMON001', 'NGLTAO001', 'PTRRIC011'], 'Incorrect student list returned')
		
		

class test_getYearAndProject(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cleardl.main()

	def test_normal_case(self):		
		project = createproject('PROJECTS', 'PROJECTS', '2022', ['PTRRIC011'])		
		self.assertTrue(project, 'Failed to create project')
		
		studentid = getstudentid('PTRRIC011')
		self.assertNotEqual(studentid, '', 'Unable to find student')
		
		(resultyear, resultproject) = getYearAndProject(studentid)
		self.assertEqual( resultyear, '2022' , 'Failed to return year given student ID')
		self.assertEqual( resultproject, 'PROJECTS', 'Failed to return project given student ID')

class test_getYearAndProject2(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		#setup any data structures for class
		True

	def test_normal_case(self):
		#code goes here
		self.assertTrue(True)
		
if oldsyspath!='':
	sys.path[0]=oldsyspath
