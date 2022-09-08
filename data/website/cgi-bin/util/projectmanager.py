import os
import traceback
import shutil

from util.pythonHTML import *
from util.usermanager import *
from util.misc import sendemail

usrdir = '../../data/users/'
prjdir = '../../db/projects/'

def addusertoproject(studentnumber, studentid, year, project):
	try:
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
	try:
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
		
#checks through a list of file names to see which files are directories
#returns a list of booleans for which file names are directories
def getdirarr(files, path):
	if not os.path.exists(path):
		return [False for i in files]
	dirfiles = []
	for f in files:
		dirfiles.append(os.path.isdir(path+'/'+ f))
	return dirfiles
	
def displayprojectfiles(year, project, openpath):
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
				#TODO is file
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
	return os.path.exists(prjdir+year+'/'+path+'/'+filename) and os.path.isdir(prjdir+year+'/'+path+'/'+filename)

def unzipfile(path, filename):
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
	if os.path.exists(prjdir+year+'/'+path+'/'+oldfilename):
		os.rename(prjdir+year+'/'+path+'/'+oldfilename, prjdir+year+'/'+path+'/'+newfilename)
		return True
	else:
		p('Path '+strong(prjdir+year+'/'+path+'/'+oldfilename)+' does not exist')
		return False
		
def createprojectscsv(uploadfile, year):
	try:
		projectsdict={}
		for line in uploadfile.file.readlines():
			(project, student) = line.decode("utf-8").strip().split(',')
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
	try:
		path = prjdir+'../project_data/'+year+'/'+projectcode
		if not os.path.exists(path):
			os.makedirs(path)
		shutil.make_archive(path+'/'+projectcode, 'zip', prjdir+year+'/'+projectcode)
		return True
	except:
		p(traceback.format_exc())
		return False		
	
#fetches all of the projects awaitng moderation
#returns a 3D list in the form [[year, [projects for year]]]
#if there are no projects returns an empty list []
def getpendingprojects():
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
	emails = getusersemailsinproject(year, projectname)
	if os.path.exists(prjdir+'../project_data/'+year+'/'+projectname+'/pendingreview.txt'):
		os.remove(prjdir+'../project_data/'+year+'/'+projectname+'/pendingreview.txt')
	if reason==None:
		reason = 'No Reason Provided'
	result = sendemail(emails, 'Request to add '+projectname+' - DECLINED', 'Your project has been rejected from the archive.\nReason provided: '+reason)
	return result

def getnamefield(line):
	name = line[line.index('<')+1:line.index('>')]
	field = line[line.index('>')+1:line.rindex('<')]
	return [name, field]

def viewmetadata(year, projectcode):
	try:
		fields = ['title', 'description', 'date', 'student', 'student', 'student', 'student', 'supervisor']
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
		
