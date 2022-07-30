import os
import traceback
import shutil

from util.pythonHTML import *
from util.usermanager import *

usrdir = '../../data/users/'
prjdir = '../../db/projects/'

def addusertoproject(studentnumber, studentid, year, project):
	try:
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
		p(str(traceback.format_exc()))
		return False
	
def createproject(projectname, projectcode, year, students):
	try:
		if not os.path.exists(usrdir+'../projects/'):
			os.mkdir(usrdir+'../projects/')
		
		f = open('../../data/spreadsheets/collections.csv', 'r')
		f.readline()

		for line in f:
			if line.split(',')[0]==(projectcode+year):
				h('Project Already Exists')
				return False
		f.close()
		
		if not os.path.exists('../../data/spreadsheets/'+year):
			os.mkdir('../../data/spreadsheets/'+year)
		if not os.path.exists('../../data/projects/'+year):
			os.mkdir('../../data/projects/'+year)
		if not os.path.exists(prjdir+year+'/'+projectcode):
			os.makedirs(prjdir+year+'/'+projectcode)
		
		f = open(usrdir+'../projects/'+year+'/'+projectcode+'.txt', 'x')
		f.close()
		
		f= open('../../data/spreadsheets/collections.csv', 'a')
		f.write(projectcode+str(year)+',\n')
		f.close()
		
		for student in students:
			studentid = createuser(student)
			addusertoproject(student, studentid, year, projectcode)
			
		return True
	except IOError:
		h('Unable to find file:')
		p(traceback.format_exc())
		return False



def displayprojectfiles(year, project, openpath):
	try:
		table = []
		path='../../db/projects/'+year+'/'+project+'/'
		selected = []
		table.append([project])
		selected.append(0)
		
		#Handle path to the selected file
		for directory in range(len(openpath)):
			if not os.path.isdir(path+'/'.join(openpath[:directory])):
				#TODO is file
				break
			col = sorted(os.listdir(path+'/'.join(openpath[:directory])))
			selected.append(col.index(openpath[directory]))
			table.append(col)
		
		#Handle the last selected file
		if not os.path.isdir(path+'/'.join(openpath)):
				#TODO is file
				p('Building')
		else:
			col = sorted(os.listdir(path+'/'.join(openpath)))
			table.append(col)
		
		script('setyear('+year+')')
		tablegen3(table, selected)
	except:
		p(traceback.format_exc())

def deletefile(year, path, filename):
	try:
		if os.path.exists(prjdir+year+'/'+path+'/'+filename):
			if os.path.isdir(prjdir+year+'/'+path+'/'+filename):
				shutil.rmtree('path')
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
		shutil.unpack_archive(path+filename, path)
		os.remove(path+filename)
		p('File unzipped successfully')
		return True
	except:
		p('Unable to unzip file')
		p(traceback.format_exc())
		return False
		
def addfiletoproject(year, path, filename, uploadfile, unzip):
	try:
		fn = os.path.basename(uploadfile.filename)
		f = open(prjdir+year+'/'+path+'/'+filename+'/'+fn, 'wb')
		f.write(uploadfile.file.read())
		f.close()
		if unzip and fn.split('.',1)[1] in ['tar.bz2', 'tbz2', 'tar.gz', 'tgz', 'tar', 'tar.xz', 'txz', 'zip']:
			unzipfile(prjdir+year+'/'+path+'/'+filename+'/', fn)
		return True
	except:
		p(traceback.format_exc())
		return False
