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
			
			f = open(userdir+'../projects/'+year+'/'+project, 'a')
			f.write(studentnumber)
			f.close()
			
			p('User: ' + studentnumber + ' has been added successfully.')
		except IOError:
			h('unable to create user files')
	except BaseException as err:
		h('Unable to find counter file')

def deleteuser(studentnumber):
	studentnumber = '<name>'+studentnumber+'</name>'
	if not os.path.exists(usrdir):
		return False
	userid = -1
	for filename in os.listdir(usrdir):
		#print(filename, filename.split('.')[1]=='name')
		if filename.split('.')[1]=='name':
			try:
				f = open(usrdir+filename, 'r')
				#print(filename, f.readline(),studentnumber)
				if f.readline()==studentnumber:
					f.close()
					userid=filename.split('.')[0]
					break
				f.close()
			except Exception as e:
				print(e)
				continue
	try:
		f = open(userdir+'../projects/'+year+'/'+project, 'r')
		students = f.readlines()
		f.close()
		
		f = open(userdir+'../projects/'+year+'/'+project, 'w')
		for student in students:
			if student!=studentnumber:
				f.write(student+'/n')
		f.close()
	except Exception as e:
		print(e)
		return False
	if userid==-1:
		return True
	for filename in ['.name.xml', '.email.xml', '.password.xml', '.permissions.xml', '.token.txt']:
		if os.path.exists(usrdir+userid+filename):
			os.remove(usrdir+userid+filename)
	return True
			
