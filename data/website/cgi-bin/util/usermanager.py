import os

from util.pythonHTML import *

usrdir = '../../data/users/'

def createuser(studentnumber):
	"""creates a user and puts stores the details in XML files
	returns the created users ID if it was successful and an empty string if it failed"""
	try:
		studentnumber=''.join(filter(str.isalnum, studentnumber)) 
		f = open('../../db/counter/users.counter', 'r+')
		counter = str(int(f.readline())+1)
		f.seek(0)
		f.write(counter)
		f.truncate()
		f.close()
		if os.path.exists(usrdir+counter+'.email.xml'):
			h('user already exists for this counter')
			return ''
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
			
			f = open(usrdir+counter+'.permissions.xml', 'a')
			f.close()
			
			p('User: ' + studentnumber + ' has been created successfully.')
			return counter
		except IOError as err:
			h('unable to create user files: '+str(err))
			return ''
	except BaseException as err:
		h('Unable to find counter file'+str(err))
		return ''

def deleteuser(studentnumber, year, project):
	"""deletes a user and deletes the stored the details in XML files
	returns true if it was successful and false if it failed"""
	studentnumber=''.join(filter(str.isalnum, studentnumber)) 
	studentnumbermod = '<name>'+studentnumber+'</name>'
	if not os.path.exists(usrdir):
		return False
	userid = -1
	for filename in os.listdir(usrdir):
		if filename.split('.')[1]=='name':
			try:
				f = open(usrdir+filename, 'r')
				if f.readline().strip()==studentnumbermod:
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
	for filename in ['.name.xml', '.email.xml', '.password.xml', '.permissions.xml', '.profile.xml', '.token.txt']:
		if os.path.exists(usrdir+userid+filename):
			os.remove(usrdir+userid+filename)
	return True

def getstudentid(studentnumber):
	"""fetches a user's ID from their student number
	returns the ID if it was successful and an empty string if it failed"""
	studentnumbermod = '<name>'+studentnumber+'</name>'
	if not os.path.exists(usrdir):
		return ''
	for filename in os.listdir(usrdir):
		if filename.split('.')[1]=='name':
			try:
				f = open(usrdir+filename, 'r')
				if f.readline().strip()==studentnumbermod:
					f.close()
					return filename.split('.')[0]
				f.close()
			except Exception as e:
				print(e)
				continue
	return ''
	
def getstudentemail(studentnumber):
	"""fetches a user's email address from their student number
	returns the email address if it was successful and an empty string if it failed"""
	sid = getstudentid(studentnumber)
	if sid=='':
		return ''
	if os.path.exists(usrdir+sid+'.email.xml'):
		try:
			f = open(usrdir+sid+'.email.xml', 'r')
			email = f.readline()[7:-8]
			f.close()
			return email
		except Exception as e:
			print(e)
	return ''
		
def getstudentname(userid):
	"""fetches a user's name from their user id
	returns the user's name if it was successful and an empty string if it failed"""
	if userid == '':
		return ''
	if os.path.exists(usrdir+userid+'.name.xml'):
		try:
			f = open(usrdir+userid+'.name.xml', 'r')
			name = f.readline().strip()[6:-7]
			f.close()
			return name
		except Exception as e:
			print(e)
	return ''

def getallstudents():
	"""fetches a sorted list of all users in the system
	returns the sorted list if it was successful and an empty list there are no users"""
	students=[]
	if not os.path.exists(usrdir):
		return students
	for filename in os.listdir(usrdir):
		if filename.split('.')[1]=='name':
			try:
				f = open(usrdir+filename, 'r')
				students.append(f.readline().strip()[6:-7])
				f.close()
			except Exception as e:
				print(e)
				continue
	return sorted(students)

def getYearAndProject(userid):
	"""fetches a the year and project code that a specific user is assigned to
	returns the year and project code if it was successful and two empty strings if the user does not exist or the user has no permissions"""
	if userid=='':
		p('No user ID provided')
		return ('','')
	try:
		if not os.path.exists(usrdir+userid+'.permissions.xml'):
			return ('','')
		f = open(usrdir+userid+'.permissions.xml', 'r')
		project=f.readline().strip()
		year=f.readline().strip()
		f.close()
		return (year[6:-7], project[6:-7])
	except:
		return ('','')
