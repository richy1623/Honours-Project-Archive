
import unittest
from unittest.mock import patch, call

#set system path
import sys
oldsyspath=''
if sys.path[0].split('/')[-1]=='test':
	oldsyspath=sys.path[0]
	sys.path[0]='/'.join(sys.path[0].split('/')[:-1])
	print('set path to: '+sys.path[0])
	
import os
import shutil
import cgi

from test import cleardl, filldl
from util.usermanager import *
from util.projectmanager import *

testdata = '../../data/test_data/'
usrdir = '../../data/users/'
dbprjdir = '../../db/projects/'
dbprjdatadir = '../../db/project_data/'
pubhtmldir = '../'

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
		
		self.assertTrue(os.path.exists(usrdir+'../projects/2022/PROJECTS.txt'), 'Failed to create a project file for permissions') 
		
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
		os.mkdir(dbprjdir+'2022')
		shutil.copytree(testdata+'project/PROJECTS', dbprjdir+'2022/PROJECTS')
		
	def test_normal_case(self):
		display = displayprojectfiles('2022', 'PROJECTS', '')
		self.assertEquals(display, ([['PROJECTS'], ['index.html', 'testfile.txt', 'testfile2.txt', 'testfolder1', 'testfolder2']], [[True], [False, False, False, True, True]], [0]))
		
	def test_display_path_one(self):
		display = displayprojectfiles('2022', 'PROJECTS', ['testfolder1'])
		self.assertEquals(display, ([['PROJECTS'], ['index.html', 'testfile.txt', 'testfile2.txt', 'testfolder1', 'testfolder2'], ['testfile3.txt']], [[True], [False, False, False, True, True], [False]], [0, 3]))
		
	def test_invalid_project_name(self):
		display = displayprojectfiles('2022', 'NoSuchProject', '')
		self.assertEquals(display, ([['NoSuchProject']], [[True]], [0]))	
		
	def test_invalid_project_file(self):
		display = displayprojectfiles('2022', 'PROJECTS', ['NoSuchFolder'])
		self.assertEquals(display, ([['PROJECTS']], [[True]], [0]))
	
class test_deletefile(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cleardl.main()

	def test_normal_case(self):
		os.mkdir(dbprjdir+'2022')
		shutil.copytree(testdata+'project/PROJECTS', dbprjdir+'2022/PROJECTS')
		result = deletefile('2022', 'PROJECTS', 'index.html')
		self.assertTrue(result, 'Self reported fail for deleting')
		
		self.assertFalse(os.path.exists(dbprjdir+'2022/PROJECTS/index.html'), 'Failed to delete a given project file')

class test_checkifdir(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cleardl.main()
		os.mkdir(dbprjdir+'2022')
		shutil.copytree(testdata+'project/PROJECTS', dbprjdir+'2022/PROJECTS')
		
	def test_file_is_dir(self):
		result = checkifdir('2022', 'PROJECTS', 'testfolder1')
		self.assertTrue(result)
		
	def test_file_is_not_dir(self):
		result = checkifdir('2022', 'PROJECTS', 'index.html')
		self.assertFalse(result)

class test_unzipfile(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cleardl.main()
		os.mkdir(dbprjdir+'2022')
		os.mkdir(dbprjdir+'2022/PROJECTS')
		shutil.copyfile(testdata+'testzip.zip', dbprjdir+'2022/PROJECTS/testzip.zip')

	def test_normal_case(self):
		result = unzipfile(dbprjdir+'2022/PROJECTS/', 'testzip.zip')
		self.assertTrue(result)
		self.assertFalse(os.path.exists(dbprjdir+'2022/PROJECTS/testzip.zip'), 'Failed to delete a zip file after deletion')
		self.assertTrue(os.path.exists(dbprjdir+'2022/PROJECTS/testzip'), 'Failed to unzip file')
		self.assertTrue(os.path.exists(dbprjdir+'2022/PROJECTS/testzip/zippedfile1.txt'), 'Failed to unzip file 1')
		self.assertTrue(os.path.exists(dbprjdir+'2022/PROJECTS/testzip/zippedfile2.txt'), 'Failed to unzip file 2')
	
	def test_file_not_exist(self):
		result = unzipfile('2022/PROJECTS', 'testzip2.zip')
		self.assertFalse(result)

class test_addfiletoproject(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cleardl.main()
		os.mkdir(dbprjdir+'2022')
		shutil.copytree(testdata+'project/PROJECTS', dbprjdir+'2022/PROJECTS')
		
	def test_normal_case(self):
		uploadfile = cgi.FieldStorage()
		uploadfile.file = open(testdata+'newfile.txt', 'rb')
		uploadfile.filename = 'newfile.txt'
		result  = addfiletoproject('2022', 'PROJECTS', '', uploadfile, False)
		self.assertTrue(result, 'Self reported fail to add file to project')
		self.assertTrue(os.path.exists(dbprjdir+'2022/PROJECTS/newfile.txt'), 'Failed to add file')
	
	def test_upload_with_unzip(self):
		uploadfile = cgi.FieldStorage()
		uploadfile.file = open(testdata+'testzip.zip', 'rb')
		uploadfile.filename = 'testzip.zip'
		result  = addfiletoproject('2022', 'PROJECTS', '', uploadfile, True)
		self.assertTrue(result, 'Self reported fail to add file to project')
		self.assertTrue(os.path.exists(dbprjdir+'2022/PROJECTS/testzip'), 'Failed to unzip file')
		self.assertTrue(os.path.exists(dbprjdir+'2022/PROJECTS/testzip/zippedfile1.txt'), 'Failed to unzip file 1')
		self.assertTrue(os.path.exists(dbprjdir+'2022/PROJECTS/testzip/zippedfile2.txt'), 'Failed to unzip file 2')

class test_renamefile(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cleardl.main()
		os.mkdir(dbprjdir+'2022')
		shutil.copytree(testdata+'project/PROJECTS', dbprjdir+'2022/PROJECTS')

	def test_normal_case(self):
		result = renamefile('2022', 'PROJECTS', 'index.html', 'newindex.html')
		self.assertTrue(result, 'Self reported fail to rename file')
		self.assertTrue(os.path.exists(dbprjdir+'2022/PROJECTS/newindex.html'), 'Failed to add new file')
		self.assertFalse(os.path.exists(dbprjdir+'2022/PROJECTS/index.html'), 'Failed to delete old file')

class test_createprojectscsv(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cleardl.main()

	def test_normal_case(self):
		uploadfile = cgi.FieldStorage()
		uploadfile.file = open(testdata+'2023Projects.csv', 'rb')
		uploadfile.filename = '2023Projects.csv'
		result = createprojectscsv(uploadfile, '2023')
		
		self.assertTrue(result, 'Self reported fail to create project')
		self.assertTrue(os.path.exists(usrdir+'../projects/'), 'Failed to create project folder')
		
		for projectname in ['DemoProject', 'DiceSimulator', 'NewGame']:
			self.assertTrue(os.path.exists(usrdir+'../projects/2023/'+projectname+'.txt'), 'Failed to create a project file for permissions') 
			self.assertTrue(os.path.exists(dbprjdir+'2023'+'/'+projectname), 'Failed to create a project folder inside a particular year folder') 
			self.assertTrue(os.path.exists(dbprjdir+'../project_data/'+'2023'+'/'+projectname), 'Failed to create a project folder inside the project data folder') 
			
		students = getallstudents()
		if 'Admin' in students:
			students.remove('Admin')
		self.assertEqual(students, [' BSSETH002', ' DMZCAT001', ' HTHSAM007', ' PTRRIC011'], 'Incorrect list of students created')

class test_addmetadata(unittest.TestCase):
	def setUp(self):
		cleardl.main()
		createproject('PROJECTS', 'PROJECTS', '2022', [])

	def test_normal_case(self):
		image = cgi.FieldStorage()
		image.file = open(testdata+'testimage.jpg', 'rb')
		image.filename = 'testimage.jpg'
		result = addmetadata('2022', 'PROJECTS', 'New Honours Archive', ['PTRRIC011', 'MNZSIM001'], 'Hussein', 'A very captivating description', image)
		self.assertTrue(result, 'Self reported fail to add metadata')
		f = open(prjdir+'../project_data/2022/PROJECTS/metadata.xml', 'r')
		fexpected = open(testdata+'metadata.xml', 'r')
		self.assertEquals(f.readlines(), fexpected.readlines())
		self.assertTrue(os.path.exists(prjdir+'../project_data/2022/PROJECTS/PROJECTS.jpg'))

	def test_no_image(self):
		result = addmetadata('2022', 'PROJECTS', 'New Honours Archive', ['PTRRIC011', 'MNZSIM001'], 'Hussein', 'A very captivating description', None)
		self.assertTrue(result, 'Self reported fail to add metadata')
		f = open(prjdir+'../project_data/2022/PROJECTS/metadata.xml', 'r')
		fexpected = open(testdata+'metadata.xml', 'r')
		self.assertEquals(f.readlines(), fexpected.readlines())
		self.assertTrue(os.path.exists(prjdir+'../project_data/2022/PROJECTS/PROJECTS.jpg'))

class test_zipproject(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cleardl.main()
		os.mkdir(dbprjdir+'2022')
		shutil.copytree(testdata+'project/PROJECTS', dbprjdir+'2022/PROJECTS')

	def test_normal_case(self):
		result = zipproject('2022', 'PROJECTS')
		self.assertTrue(result, 'Self reported fail to zip project')
		self.assertTrue(os.path.exists(dbprjdatadir+'2022/PROJECTS/PROJECTS.zip'))
		
class test_getpendingprojects(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cleardl.main()

	def test_normal_case(self):
		filldl.main()
		for i in range(1, 9):
			f = open(dbprjdatadir+'2020/project'+str(i)+'/pendingreview.txt', 'x')
			f.close()
		result = getpendingprojects()
		self.assertEquals(len(result), 1)
		self.assertEquals(result, [['2020', ['project'+str(i) for i in range(1, 9)]]])
	
	def test_no_projects(self):
		cleardl.main()
		result = getpendingprojects()
		self.assertEquals(len(result), 0)
		self.assertEquals(result, [])

class test_getusersemailsinproject(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cleardl.main()
		filldl.main()

	def test_normal_case(self):
		result = getusersemailsinproject('2020', 'project2')
		self.assertEquals(result, ['user2@myuct.ac.za', 'user3@myuct.ac.za'])
		
	def test_no_such_project(self):
		result = getusersemailsinproject('2020', 'NoSuchProject')
		self.assertEquals(result, [])

class test_submitmoderation(unittest.TestCase):
	def setUp(self):
		cleardl.main()
		os.mkdir(dbprjdir+'2022')
		os.mkdir(dbprjdatadir+'2022')
		os.mkdir(dbprjdatadir+'2022/PROJECTS')

	def test_normal_case(self):
		shutil.copytree(testdata+'project/PROJECTS', dbprjdir+'2022/PROJECTS')
		shutil.copyfile(testdata+'metadata.xml', dbprjdatadir+'2022/PROJECTS/metadata.xml')
		
		result = submitmoderation('2022', 'PROJECTS')
		self.assertTrue(result, 'Self reported fail to submit project')
		self.assertTrue(os.path.exists(dbprjdatadir+'2022/PROJECTS/PROJECTS.zip'))
		self.assertTrue(os.path.exists(dbprjdatadir+'2022/PROJECTS/pendingreview.txt'))
		
	def test_valid_project_no_metadata(self):
		shutil.copytree(testdata+'project/PROJECTS', dbprjdir+'2022/PROJECTS')
		
		result = submitmoderation('2022', 'PROJECTS')
		self.assertFalse(result, 'Self reported fail to submit project')
		self.assertFalse(os.path.exists(dbprjdatadir+'2022/PROJECTS/PROJECTS.zip'))
		self.assertFalse(os.path.exists(dbprjdatadir+'2022/PROJECTS/pendingreview.txt'))
		
	def test_valid_project_no_metadata(self):
		result = submitmoderation('2022', 'NoSuchProject')
		self.assertFalse(result, 'Self reported fail to submit project')
		self.assertFalse(os.path.exists(dbprjdatadir+'2022/NoSuchProject/NoSuchProject.zip'))
		self.assertFalse(os.path.exists(dbprjdatadir+'2022/NoSuchProject/pendingreview.txt'))
		
class test_approveproject(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cleardl.main()

	def test_normal_case(self):
		#create project to deny
		project = createproject('PROJECTS', 'PROJECTS', '2022', ['PTRRIC011'])
		self.assertTrue(project, 'Self reported fail to create project')
		shutil.rmtree(dbprjdir+'2022/PROJECTS')
		shutil.copytree(testdata+'project/PROJECTS', dbprjdir+'2022/PROJECTS')
		metadata = addmetadata('2022', 'PROJECTS', 'New Honours Archive', ['PTRRIC011', 'MNZSIM001'], 'Hussein', 'A very captivating description', None)
		self.assertTrue(metadata, 'Self reported fail to add metadata')
		#submit project for moderation
		submit = submitmoderation('2022', 'PROJECTS')
		self.assertTrue(submit, 'Self reported fail to submit project')
		
		result = approveproject('2022', 'PROJECTS')
		self.assertTrue(result, 'Self reported fail to accept project')
		self.assertFalse(os.path.exists(dbprjdatadir+'2022/NoSuchProject/pendingreview.txt'))
		
		#check year in collection
		path = pubhtmldir+'metadata/index.xml'
		self.assertTrue(os.path.exists(path), path+' not created')
		f = open(path, 'r')
		text = f.read()
		f.close()
		self.assertIn('<item type="collection">2022</item>', text)
		
		#check project in year
		path = pubhtmldir+'metadata/2022/index.xml'
		self.assertTrue(os.path.exists(path), path+' not created')
		f = open(path, 'r')
		text = f.read()
		f.close()
		self.assertIn('<item type="item">PROJECTS</item>', text)
		
		#check project in year
		path = pubhtmldir+'metadata/2022/PROJECTS/index.xml'
		self.assertTrue(os.path.exists(path), path+' not created')
		f = open(path, 'r')
		text = f.read()
		f.close()
		self.assertEquals('<collection>\n   <level>3</level>\n   <type>item</type>\n</collection>', text)
		
		#check metadata in project
		self.assertTrue(os.path.exists(pubhtmldir+'metadata/2022/PROJECTS/metadata.xml'))
		
		#check project files in collection
		self.assertTrue(os.path.exists(pubhtmldir+'collection/2022/PROJECTS/PROJECTS.jpg'))
		self.assertTrue(os.path.exists(pubhtmldir+'collection/2022/PROJECTS/PROJECTS.zip'))

class test_denyproject(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cleardl.main()

	def test_normal_case(self):
		#create project to deny
		project = createproject('PROJECTS', 'PROJECTS', '2022', ['PTRRIC011'])
		self.assertTrue(project, 'Self reported fail to create project')
		shutil.rmtree(dbprjdir+'2022/PROJECTS')
		shutil.copytree(testdata+'project/PROJECTS', dbprjdir+'2022/PROJECTS')
		metadata = addmetadata('2022', 'PROJECTS', 'New Honours Archive', ['PTRRIC011', 'MNZSIM001'], 'Hussein', 'A very captivating description', None)
		self.assertTrue(metadata, 'Self reported fail to add metadata')
		#submit project for moderation
		submit = submitmoderation('2022', 'PROJECTS')
		self.assertTrue(submit, 'Self reported fail to submit project')
		
		#test denial
		result = denyproject('2022', 'PROJECTS', 'Reason to deny')
		self.assertTrue(result, 'Self reported fail to deny project')
		self.assertFalse(os.path.exists(dbprjdatadir+'2022/NoSuchProject/pendingreview.txt'))

class test_viewmetadata(unittest.TestCase):
	def setUp(self):
		cleardl.main()
		os.mkdir(dbprjdatadir+'2022')
		os.mkdir(dbprjdatadir+'2022/PROJECTS')

	def test_normal_case(self):
		shutil.copyfile(testdata+'metadata.xml', dbprjdatadir+'2022/PROJECTS/metadata.xml')
		result = viewmetadata('2022', 'PROJECTS')
		self.assertEquals(result, [['title', 'New Honours Archive'], ['description', 'A very captivating description'], ['date', '2022'], 
			['student', 'PTRRIC011'], ['student', 'MNZSIM001'], ['supervisor', 'Hussein']])
	
	def test_no_such_project(self):
		result = viewmetadata('2022', 'NoSuchProject')
		self.assertFalse(result)

if oldsyspath!='':
	sys.path[0]=oldsyspath
	print('reverting sys path')
		
