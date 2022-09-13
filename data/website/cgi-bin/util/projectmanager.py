import os
import traceback
import shutil

from util.pythonHTML import *
from util.usermanager import *
from util.emailmanager import sendemail

usrdir = '../../data/users/'
prjdir = '../../db/projects/'

def addusertoproject(studentnumber, studentid, year, project):
	"""adds a user to a project and updates the stored the details in XML files
	takes in the students number, the user ID, the year of the project and the project code
	returns true if it was successful and false if it failed"""
	try:
		studentnumber=''.join(filter(str.isalnum, studentnumber)) 
		year = str(year)
		
		if not os.path.exists(usrdir+'../projects/'+year+'/'+project+'.txt'):
			p('Project does not exist')
			return False
		if studentid=='':
			p('No student ID given for student '+ str(studentnumber))
			return False
			
		f = open(usrdir+'../projects/'+year+'/'+project+'.txt', 'r')
		for line in f.readlines():
			if line.strip()==studentnumber:
				return True
		f.close()
		
		f = open(usrdir+studentid+'.permissions.xml', 'w')
		f.write('<code>'+project+'</code>\n')
		f.write('<year>'+year+'</year>')
		f.close()
		
		f = open(usrdir+'../projects/'+year+'/'+project+'.txt', 'a')
		f.write(studentnumber+'\n')
		f.close()
		return True
	except:
		h('Failed to add student to project '+project)
		p(traceback.format_exc())
		return False
	
def createproject(projectname, projectcode, year, students):
	"""creates a project and create XML files to store the details
	takes in a the project name, project code, the year that the project belongs to 
	and a list of student numbers to add to the project
	returns true if it was successful and false if it failed"""
	try:
		projectcode=''.join(filter(str.isalnum, projectcode)) 
		if not os.path.exists(usrdir+'../projects/'):
			os.mkdir(usrdir+'../projects/')
		
		#f = open('../../data/spreadsheets/collections.csv', 'r')
		#f.readline()
		#
		#for line in f:
		#	if line.split(',')[0]==(projectcode+year):
		#		p('Project '+projectcode+' Already Exists')
		#		return False
		#f.close()
		#
		#if not os.path.exists('../../data/spreadsheets/'+year):
		#	os.mkdir('../../data/spreadsheets/'+year)
		
		if not os.path.exists('../../data/projects/'+year):
			os.mkdir('../../data/projects/'+year)
		if not os.path.exists(prjdir+year+'/'+projectcode):
			os.makedirs(prjdir+year+'/'+projectcode)
		if not os.path.exists(prjdir+'../project_data/'+year+'/'+projectcode):
			os.makedirs(prjdir+'../project_data/'+year+'/'+projectcode)
		
		f = open(usrdir+'../projects/'+year+'/'+projectcode+'.txt', 'x')
		f.close()
		
		#f= open('../../data/spreadsheets/collections.csv', 'a')
		#f.write(projectcode+str(year)+',\n')
		#f.close()
		
		for student in students:
			studentid = createuser(student)
			addusertoproject(student, studentid, year, projectcode)
			
		return True
	except IOError:
		h('Unable to find file:')
		p(traceback.format_exc())
		return False
		
def getdirarr(files, path):
	"""checks through a list of file names to see which files are directories
	takes in a list of files to check and a root path to check from
	returns a list of booleans for which file names are directories"""
	if not os.path.exists(path):
		return [False for i in files]
	dirfiles = []
	for f in files:
		dirfiles.append(os.path.isdir(path+'/'+ f))
	return dirfiles
	
def displayprojectfiles(year, project, openpath):
	"""parses through a group of file directories to fetch all of the files contained within them
	takes in the year of the project, the project code and a path listing all of the required directories to check
	returns 2D array of each of the directories and their files, a list of which of the given files were 
	directories and a list of all of the indexes for each of the wanted directories"""
	try:
		year=str(year)
		project=str(project)
		table = []
		dirs=[[True]]
		path='../../db/projects/'+year+'/'+project+'/'
		selected = []
		table.append([project])
		selected.append(0)
		if not os.path.exists(path):
			return (table, dirs, selected)
		
		#Handle path to the selected file
		for directory in range(len(openpath)):
			if not os.path.exists(path+'/'.join(openpath[:directory])):
				break
			if not os.path.isdir(path+'/'.join(openpath[:directory])):
				break
			col = sorted(os.listdir(path+'/'.join(openpath[:directory])))
			selected.append(col.index(openpath[directory]))
			table.append(col)
			dirs.append(getdirarr(col, path+'/'.join(openpath[:directory])))
		
		#Handle the last selected file
		if os.path.exists(path+'/'.join(openpath)):
			if os.path.isdir(path+'/'.join(openpath)):
				col = sorted(os.listdir(path+'/'.join(openpath)))
				table.append(col)
				dirs.append(getdirarr(col, path+'/'.join(openpath)))
		
		script('setyear('+year+')')
		return (table, dirs, selected)
	except:
		p(traceback.format_exc())
		return (table, dirs, selected)

def deletefile(year, path, filename):
	"""deletes a file from a project
	takes in the project year, the path to the file (including the project name), and the file to be deleted
	returns true if it was deleted or if it never existed and false if it failed to delete the file"""
	year = str(year)
	filename = str(filename)
	try:
		if os.path.exists(prjdir+year+'/'+path+'/'+filename):
			if os.path.isdir(prjdir+year+'/'+path+'/'+filename):
				shutil.rmtree(prjdir+year+'/'+path+'/'+filename)
			else:
				os.remove(prjdir+year+'/'+path+'/'+filename)
			return True
		else:
			p('File does not exist: '+year+'/'+path+'/'+filename)
			return False
	except:
		p(traceback.format_exc())
		return False

def checkifdir(year, path, filename):
	"""checks if a given file is a directory
	takes in the project year, the path to the file (including the project name), and the file to be checked
	returns true if it is a directory and false if it not"""
	return os.path.exists(prjdir+year+'/'+path+'/'+filename) and os.path.isdir(prjdir+year+'/'+path+'/'+filename)

def unzipfile(path, filename):
	"""unzips a file from a project
	takes in the path to the file (including the project name and year), and the file to be unzipped
	returns true if it was unzipped and false if it failed to unzipped the file"""
	try:
		if len(filename.split('.',1))>1 and filename.split('.',1)[1] in ['tar.bz2', 'tbz2', 'tar.gz', 'tgz', 'tar', 'tar.xz', 'txz', 'zip']:
			shutil.unpack_archive(path+filename, path)
			os.remove(path+filename)
			p('File unzipped successfully')
			return True
		else:
			p('Unable to unzip file')
			return False
	except:
		p('Unable to unzip file')
		p(traceback.format_exc())
		return False
		
def addfiletoproject(year, path, targetlocation, uploadfile, unzip):
	"""adds a file to a project
	takes in the project year, the path to the file (including the project name), the directory to add the file to, the file to add 
	and a boolean stating whether to unzip the file
	returns true if it was added and false if it failed to add the file"""
	try:
		fn = os.path.basename(uploadfile.filename)
		f = open(prjdir+year+'/'+path+'/'+targetlocation+'/'+fn, 'wb')
		f.write(uploadfile.file.read())
		f.close()
		if unzip :
			unzipfile(prjdir+year+'/'+path+'/'+targetlocation+'/', fn)
		return True
	except:
		p(traceback.format_exc())
		return False
		
def renamefile(year, path, oldfilename, newfilename):
	"""renames a file from a project
	takes in the project year, the path to the file (including the project name), the old file's name, and the new name for the file
	returns true if it was renamed and false if it failed to rename the file"""
	if path=='':
		p('Unable to rename root directory')
		return False
	if os.path.exists(prjdir+year+'/'+path+'/'+oldfilename):
		os.rename(prjdir+year+'/'+path+'/'+oldfilename, prjdir+year+'/'+path+'/'+newfilename)
		return True
	else:
		p('Path '+strong(prjdir+year+'/'+path+'/'+oldfilename)+' does not exist')
		return False
		
def createprojectscsv(uploadfile, year):
	"""creates one or more projects based off a csv file
	takes in a file and the year to create all the projects for
	the file should contain PROJECTCODE,STUDENTNUMBER on each line
	returns true if it created the projects and false if it faileds"""
	try:
		projectsdict={}
		for line in uploadfile.file.readlines():
			(project, student) = line.decode("utf-8").strip().split(',')
			project = project.strip()
			student=student.strip()
			if project not in projectsdict.keys():
				projectsdict[project]=[]
			projectsdict[project].append(student)
		for key in projectsdict:
			createproject(key, key, year, projectsdict[key])
		return True
	except:
		p(traceback.format_exc())
		return False
		
def addmetadata(year, projectcode, title, students, supervisor, description, image):
	"""adds metadata to a project and an thumbnail
	takes in the project year, the project name, the title of the project, a list of students in the project, 
	a description for the project and a thubnail for the project
	if no image is provided, a default image will be used
	returns true if it was added successfully and false if it failed"""
	try:
		if not os.path.exists(prjdir+'../project_data/'+year+'/'+projectcode):
			os.makedirs(prjdir+'../project_data/'+year+'/'+projectcode)
		
		f = open(prjdir+'../project_data/'+year+'/'+projectcode+'/metadata.xml', 'w')
		
		f.write('<item>\n')
		f.write('   <levelOfDescription>item</levelOfDescription>\n')
		f.write('   <title>'+title+'</title>\n')
		f.write('   <description>'+description+'</description>\n')
		f.write('   <date>'+year+'</date>\n')
		for i in students: 
			f.write('   <student>'+i+'</student>\n')
		f.write('   <supervisor>'+supervisor+'</supervisor>\n')
		
		f.write('   <digitalObjectURI>'+year+'/'+projectcode+'/'+projectcode+'.zip</digitalObjectURI>\n')
		f.write('   <uniqueIdentifier>'+year+projectcode+'</uniqueIdentifier>\n')
		
		f.write('  <view>\n')
		f.write('      <title>'+title+'</title>\n')
		if image==None:
			try:
				shutil.copy(usrdir+'../res/uct-logo.jpg', prjdir+'../project_data/'+year+'/'+projectcode)
				os.rename(prjdir+'../project_data/'+year+'/'+projectcode+'/uct-logo.jpg', prjdir+'../project_data/'+year+'/'+projectcode+'/'+projectcode+'.jpg')
			except:
				p(traceback.format_exc())
			f.write('      <file>'+year+'/'+projectcode+'/'+projectcode+'.jpg'+'</file>\n')
		else:	
			try:
				fn = os.path.basename(image.filename)
				imagefile = open(prjdir+'../project_data/'+year+'/'+projectcode+'/'+projectcode+'.jpg', 'wb')
				imagefile.write(image.file.read())
				imagefile.close()
				f.write('      <file>'+year+'/'+projectcode+'/'+projectcode+'.jpg'+'</file>\n')
			except:
				p(traceback.format_exc())
			
		f.write('   </view>\n')
		
		f.write('</item>')
			
		f.close()
		return True
	except:
		p(traceback.format_exc())
		return False
		
def zipproject(year, projectcode):
	"""zips a project and saves the zip to the project_data directory
	takes in the project year, and the project code
	returns true if it was zipped and false if it failed to zip the project"""
	try:
		path = prjdir+'../project_data/'+year+'/'+projectcode
		if not os.path.exists(path):
			os.makedirs(path)
		shutil.make_archive(path+'/'+projectcode, 'zip', prjdir+year+'/'+projectcode)
		return True
	except:
		p(traceback.format_exc())
		return False		
	
def getpendingprojects():
	"""fetches all of the projects awaitng moderation
	returns a 3D list in the form [[year, [projects for year]]]
	if there are no projects returns an empty list []"""
	years=[]
	if not os.path.exists(prjdir+'../project_data/'):
		return []
	for year in os.listdir(prjdir+'../project_data/'):
		projects=[]
		for project in os.listdir(prjdir+'../project_data/'+year):
			if os.path.exists(prjdir+'../project_data/'+year+'/'+project+'/pendingreview.txt'):
				projects.append(project)
		if len(projects)>0:
			years.append([year, sorted(projects)])
	return sorted(years)

def getusersemailsinproject(year, project):
	"""fetches all of the users email adresses for a project
	takes in the project year and the project code
	returns a list of all of the emails of the students in the project and an empty list if the project does not exist"""
	if os.path.exists(usrdir+'../projects/'+year+'/'+project+'.txt'):
		try:
			emails=[]
			f = open(usrdir+'../projects/'+year+'/'+project+'.txt', 'r')
			for line in f.readlines():
				emails.append(getstudentemail(line.strip()))
			f.close()
			return emails
		except:
			p(traceback.format_exc())
			return []
	else:
		return []
		
def submitmoderation(year, projectcode):
	"""submits a project for moderation
	takes in the project year and the project code
	returns true if it was added to the moderation queue and false if it failed"""
	try:
		if os.path.exists(prjdir+'../project_data/'+year+'/'+projectcode):
			if os.path.exists(prjdir+'../project_data/'+year+'/'+projectcode+'/metadata.xml'):
				zipproject(year, projectcode)
				f = open(prjdir+'../project_data/'+year+'/'+projectcode+'/pendingreview.txt', 'a')
				f.close()
				return True
			else:
				p('Metadata for project not found. Please upload metadata then try again.')
		else:
			p('No such project code exists')
		return False
	except:
		return False
		
def approveproject(year, projectname):
	"""approve a project and adds it to the digital library
	takes in the project year and the project code
	sends emails to all of the students in the project to inform them of the outcome
	returns true if it was added to the digital library and false if it failed"""
	emails = getusersemailsinproject(year, projectname)
	if not os.path.exists('../metadata/'+year):
		try:
			os.mkdir('../metadata/'+year)
			f = open('../metadata/'+year+'/index.xml', 'w')
			f.write('<collection>\n   <level>2</level>\n</collection>')
			f.close()
			if not os.path.exists('../metadata/index.xml'):
				f = open('../metadata/index.xml', 'w')
				f.write('<collection>\n   <level>1</level>\n</collection>')
				f.close()
			f = open('../metadata/index.xml', 'r')
			lines = f.readlines()
			f.close()
			f = open('../metadata/index.xml', 'w')
			f.write(lines[0])
			f.write('   <item type="collection">'+year+'</item>\n')
			for line in lines[1:]:
				f.write(line)
			f.close()
		except:
			p(traceback.format_exc())
			return False
	
	if not os.path.exists('../metadata/'+year+'/'+projectname):
		try:
			os.mkdir('../metadata/'+year+'/'+projectname)
			f = open('../metadata/'+year+'/'+projectname+'/index.xml', 'w')
			f.write('<collection>\n   <level>3</level>\n   <type>item</type>\n</collection>')
			f.close()
			
			f = open('../metadata/'+year+'/index.xml', 'r')
			lines = f.readlines()
			f.close()
			f = open('../metadata/'+year+'/index.xml', 'w')
			f.write(lines[0])
			f.write('   <item type="item">'+projectname+'</item>\n')
			for line in lines[1:]:
				f.write(line)
			f.close()
		except:
			p(traceback.format_exc())
			return False
			
	
	if os.path.exists(prjdir+'../project_data/'+year+'/'+projectname+'/metadata.xml'):
		try:
			shutil.copy(prjdir+'../project_data/'+year+'/'+projectname+'/metadata.xml', '../metadata/'+year+'/'+projectname)
		except:
			p(traceback.format_exc())
			return False
	else:
		return False

	#Handle File Moving
	if not os.path.exists('../collection/'+year):
		os.mkdir('../collection/'+year)
	
	if not os.path.exists('../collection/'+year+'/'+projectname):
		os.mkdir('../collection/'+year+'/'+projectname)
	
	try:
		shutil.copy(prjdir+'../project_data/'+year+'/'+projectname+'/'+projectname+'.jpg', '../collection/'+year+'/'+projectname)
		shutil.copy(prjdir+'../project_data/'+year+'/'+projectname+'/'+projectname+'.zip', '../collection/'+year+'/'+projectname)
	except:
		p(traceback.format_exc())
		return False
	
	try:
		os.system('../../simpledl/bin/generate.pl > /dev/null 2>&1 ')
		os.system('../../simpledl/bin/generate.pl --thumbs > /dev/null ')
	except:
		p(traceback.format_exc())
		return False
		
	if os.path.exists(prjdir+'../project_data/'+year+'/'+projectname+'/pendingreview.txt'):
		os.remove(prjdir+'../project_data/'+year+'/'+projectname+'/pendingreview.txt')
	result = sendemail(emails, 'Request to add '+projectname+' - APPROVED', 'Your project has been added to the archive.')
	return result		
	
def denyproject(year, projectname, reason):
	"""deny a project and removes it from the moderation queue
	takes in the project year, the project code, and the reason for the denial
	sends emails to all of the students in the project to inform them of the outcome
	returns true if it removed from the moderation queue and false if it failed"""
	emails = getusersemailsinproject(year, projectname)
	if os.path.exists(prjdir+'../project_data/'+year+'/'+projectname+'/pendingreview.txt'):
		os.remove(prjdir+'../project_data/'+year+'/'+projectname+'/pendingreview.txt')
	if reason==None:
		reason = 'No Reason Provided'
	result = sendemail(emails, 'Request to add '+projectname+' - DECLINED', 'Your project has been rejected from the archive.\nReason provided: '+reason)
	return result

def getnamefield(line):
	"""get the key and value in a line of XML
	takes in a line of xml in the form <key>value</key>"""
	name = line[line.index('<')+1:line.index('>')]
	field = line[line.index('>')+1:line.rindex('<')]
	return [name, field]

def viewmetadata(year, projectcode, fields = ['title', 'description', 'date', 'student', 'student', 'student', 'student', 'supervisor']):
	"""view the metadata of a project
	takes in the project year, the project code, and an optional list of metadata fields
	returns a list contaitning all of the relevant metadata fields"""
	try:
		if not os.path.exists('../../db/project_data/'+year+'/'+projectcode+'/metadata.xml'):
			return False
		f = open('../../db/project_data/'+year+'/'+projectcode+'/metadata.xml', 'r')
		metadatalines = f.readlines()
		f.close()
		metadata=[]
		for line in metadatalines:
			namefield = getnamefield(line)
			if namefield[0] in fields:
				fields.remove(namefield[0])
				metadata.append(namefield)
		return metadata
	except:
		p(traceback.format_exc())
		return False
		
