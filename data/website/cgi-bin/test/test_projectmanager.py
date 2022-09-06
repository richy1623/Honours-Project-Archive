
import unittest

#set system path
import sys
if sys.path[0].split('/')[-1]=='test':
	sys.path[0]='/'.join(sys.path[0].split('/')[:-1])
	print('set path to: '+sys.path[0])
	
import os
import shutil

from test import cleardl, filldl
from util.usermanager import *
from util.projectmanager import *

testdata = '../../data/test_data/'
usrdir = '../../data/users/'
dbprjdir = '../../db/projects/'
dbprjdatadir = '../../db/project_data/'

class test_addusertoproject(unittest.TestCase):
	def setUp(self):
		cleardl.main()

	def test_normal_case(self):
	
		#adding an existing user to a project
		counter = createuser('PTRRIC011')
		self.assertNotEqual(counter, '', 'Failed to create user')
		
		project = createproject('PROJECTS', 'PROJECTS', '2022', ['STDTES001, STDTES002'])		
		self.assertTrue(project, 'Failed to create project')
	
		result1 = addusertoproject("PTRRIC011", counter,  '2022', 'PROJECTS')
		self.assertTrue(result1, 'Self reported failed to add user to a project')
		
		self.assertTrue(os.path.exists(usrdir+counter+'.permissions.xml'), 'Permissions file not created')
		f = open(usrdir+counter+'.permissions.xml', 'r')
		permissions = f.read()
		f.close()
		self.assertEquals(permissions, '<code>PROJECTS</code>\n<year>2022</year>', 'Incorrect permissions file')
		
		f = open(usrdir+'../projects/2022/PROJECTS.txt', 'r')
		users = f.readlines()
		f.close()
		
		self.assertIn('PTRRIC011\n', users, 'Incorrect permission file for project')
	
	def test_project_not_exist(self):
		#adding a user to a non-existing project 
		counter = createuser('PTRRIC011')
		self.assertNotEqual(counter, '', 'Failed to create user')
		
		result = addusertoproject("PTRRIC011", counter,  '2022', 'PROJECTS')
		self.assertFalse(result, 'Failed to stop adding a user to a non-existing project')

class test_createproject(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cleardl.main()

	def test_normal_case(self):
		
		project = createproject('PROJECTS', 'PROJECTS', '2022', ['STDTES001, STDTES002'])		
		self.assertTrue(project, 'Self reported fail to create project')
		
		self.assertTrue(os.path.exists(usrdir+'../projects/'), 'Failed to create project folder')
		
		self.assertTrue(os.path.exists(dbprjdir+'2022'+'/'+'PROJECTS'), 'Failed to create a project folder inside a particular year folder') 
		
		self.assertTrue(os.path.exists(dbprjdir+'../project_data/'+'2022'+'/'+'PROJECTS'), 'Failed to create a project folder inside the project data folder') 
		
		students = getallstudents()
		
		if 'Admin' in students:
			students.remove('Admin')
		
		self.assertEqual(students, ['STDTES001, STDTES002'], 'Incorrect student list returned')
		

class test_getdirarr(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cleardl.main()

	def test_normal_case(self):
		os.mkdir(dbprjdir+'2022')
		shutil.copytree(testdata+'project/PROJECTS', dbprjdir+'2022/PROJECTS')
		files = ['index.html', 'testfile.txt', 'testfolder2', 'testfolder1', 'testfile2.txt']
		result = getdirarr(files, dbprjdir+'2022/PROJECTS')
		self.assertEquals(result, [False, False, True, True, False], 'Incorrect boolean for a folder given')

class test_displayprojectfiles(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cleardl.main()

	def test_normal_case(self):
		project = createproject('PROJECTS', 'PROJECTS', '2022', ['STDTES001, STDTES002'])		
		self.assertTrue(project, 'Failed to create project')
		
		#TODO
		
class test_deletefile(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cleardl.main()

	def test_normal_case(self):
		
		os.mkdir(dbprjdir+'2022')
		shutil.copytree(testdata+'project/PROJECTS', dbprjdir+'2022/PROJECTS')
		result = deletefile('2022', 'PROJECTS', 'index.html')
		
		
		self.assertFalse(os.path.exists(dbprjdir+'2022/PROJECTS/index.html'), 'Failed to delete a given project file')

class test_checkifdir(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cleardl.main()
		s
	def test_normal_case(self):
		#code goes here
		self.assertTrue(True)

class test_unzipfile(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		#setup any data structures for class
		True

	def test_normal_case(self):
		#code goes here
		self.assertTrue(True)

class test_addfiletoproject(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		#setup any data structures for class
		True

	def test_normal_case(self):
		#code goes here
		self.assertTrue(True)

class test_renamefile(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		#setup any data structures for class
		True

	def test_normal_case(self):
		#code goes here
		self.assertTrue(True)

class test_createprojectscsv(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		#setup any data structures for class
		True

	def test_normal_case(self):
		#code goes here
		self.assertTrue(True)

class test_addmetadata(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		#setup any data structures for class
		True

	def test_normal_case(self):
		#code goes here
		self.assertTrue(True)

class test_zipproject(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		#setup any data structures for class
		True

	def test_normal_case(self):
		#code goes here
		self.assertTrue(True)

class test_getpendingprojects(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		#setup any data structures for class
		True

	def test_normal_case(self):
		#code goes here
		self.assertTrue(True)

class test_getusersemailsinproject(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		#setup any data structures for class
		True

	def test_normal_case(self):
		#code goes here
		self.assertTrue(True)

class test_submitmoderation(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		#setup any data structures for class
		True

	def test_normal_case(self):
		#code goes here
		self.assertTrue(True)

class test_approveproject(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		#setup any data structures for class
		True

	def test_normal_case(self):
		#code goes here
		self.assertTrue(True)

class test_denyproject(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		#setup any data structures for class
		True

	def test_normal_case(self):
		#code goes here
		self.assertTrue(True)

class test_viewmetadata(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		#setup any data structures for class
		True

	def test_normal_case(self):
		#code goes here
		self.assertTrue(True)
