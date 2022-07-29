import os
import traceback

from util.pythonHTML import *
from util.usermanager import *

usrdir = '../../data/users/'

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
		if not os.path.exists('../../db/projects/'+year+'/'+projectcode):
			os.makedirs('../../db/projects/'+year+'/'+projectcode)
		
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
		p(str(traceback.format_exc()))
		return False



def displayprojectfiles(projectyear, openpath):
	try:
		table = []
		path='../../db/projects/'+projectyear[1]+'/'+projectyear[0]+'/'
		selected = []
		
		for directory in range(len(openpath)):
			col = sorted(os.listdir(path+'/'.join(openpath[:directory])))
			selected.append(col.find(openpath[directory]))
			table.append(col)
	except Exception as e:
		p(str(traceback.format_exc()))
