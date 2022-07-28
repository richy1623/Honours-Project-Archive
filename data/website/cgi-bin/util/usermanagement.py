import os

from util.pythonHTML import *

usrdir = '../../data/users/'

def createuser(studentnumber, project, year):
	try:
		f = open('../../db/counter/users.counter', 'r+')
		counter = str(int(f.readline())+1)
		f.seek(0)
		f.write(counter)
		f.truncate()
		f.close()
		if os.path.exists(usrdir+counter+'.email.xml'):
			h('user already exists for this counter')
			return
		try:
			f = open(usrdir+counter+'.email.xml', 'w')
			f.write('<email>'+studentnumber+'@myuct.ac.za</email>')
			f.close()
			
			f = open(usrdir+counter+'.profile.xml', 'w')
			f.write('<profile></profile>')
			f.close()
			
			f = open(usrdir+counter+'.name.xml', 'w')
			f.write('<name>'+studentnumber+'</name>')
			f.close()
			
			f = open(usrdir+counter+'.permissions.xml', 'w')
			f.write('<permissions>'+project+'</permissions>')
			f.close()
			
			f = open(usrdir+'../projects/'+year+'/'+project+'.txt', 'a')
			f.write(studentnumber+'\n')
			f.close()
			
			p('User: ' + studentnumber + ' has been added successfully.')
		except IOError as err:
			h('unable to create user files: '+str(err))
	except BaseException as err:
		h('Unable to find counter file'+str(err))

def deleteuser(studentnumber, year, project):
	studentnumbermod = '<name>'+studentnumber+'</name>'
	if not os.path.exists(usrdir):
		return False
	userid = -1
	for filename in os.listdir(usrdir):
		if filename.split('.')[1]=='name':
			try:
				f = open(usrdir+filename, 'r')
				if f.readline()==studentnumbermod:
					f.close()
					userid=filename.split('.')[0]
					break
				f.close()
			except Exception as e:
				print(e)
				continue
	try:
		f = open(usrdir+'../projects/'+year+'/'+project+'.txt', 'r')
		students = f.readlines()
		f.close()
		f = open(usrdir+'../projects/'+year+'/'+project+'.txt', 'w')
		for student in students:
			student=student.strip()
			if student!=studentnumber:
				f.write(student+'\n')
		f.close()
	except Exception as e:
		print(e)
		return False
	if userid==-1:
		return True
	for filename in ['.name.xml', '.email.xml', '.password.xml', '.permissions.xml', 'profile.xml', '.token.txt']:
		if os.path.exists(usrdir+userid+filename):
			os.remove(usrdir+userid+filename)
	return True
	
def getProject(userid):
	if userid=='':
		return ''
	try:
		f = open(usrdir+userid+'.permissions.xml', 'r')
		project=f.readline()
		f.close()
		return project[13:-14]
	except:
		p('Cannot find user permission file')
		return ''
