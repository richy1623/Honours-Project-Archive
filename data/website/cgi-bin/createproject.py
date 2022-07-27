#!/usr/bin/python3

# Import modules for CGI handling 
import cgi, cgitb 
from util.pythonHTML import *
import os
import traceback

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
#Project Data
projectname = form.getvalue('projectname')
projectcode  = form.getvalue('projectcode')
year = form.getvalue('projectyear')
#Student Data
student1 = form.getvalue('student1')
student2 = form.getvalue('student2')
student3 = form.getvalue('student3')
student4 = form.getvalue('student4')

#return html

header()
h('Attempting to create project...')

def createuser(studentnumber, project):
	try:
		f = open('../../db/counter/users.counter', 'r+')
		counter = str(int(f.readline())+1)
		f.seek(0)
		f.write(counter)
		f.truncate()
		f.close()
		if os.path.exists('../../data/users/'+counter+'.email.xml'):
			h('user already exists for this counter')
			return
		try:
			f = open('../../data/users/'+counter+'.email.xml', 'w')
			f.write('<email>'+studentnumber+'@myuct.ac.za</email>')
			f.close()
			
			f = open('../../data/users/'+counter+'.profile.xml', 'w')
			f.write('<profile></profile>')
			f.close()
			
			f = open('../../data/users/'+counter+'.name.xml', 'w')
			f.write('<name>'+studentnumber+'</name>')
			f.close()
			
			f = open('../../data/users/'+counter+'.permissions.xml', 'w')
			f.write('<permissions>'+project+'</permissions>')
			f.close()
			
			p('User: ' + studentnumber + ' has been added successfully.')
		except IOError:
			h('unable to create user files')
	except BaseException as err:
		h('Unable to find counter file')
		

if projectname==None or projectcode==None or year==None:
	h('Please fill in all project fields')
	a('http://docs.simpledl.net/createprojects.html')
	close()
	exit()

try:
	file = open('../../data/spreadsheets/collections.csv', 'r')
	file.readline()

	for line in file:
		if line.split(',')[0]==(projectcode+year):
			h('Project Already Exists')
			close()
			file.close()
			exit()
	file.close()
	
	file = open('../../data/spreadsheets/collections.csv', 'a')
	#TODO Propper info
	file.write(projectcode+year+','+'\n')
	file.close()
	if not os.path.exists('../../data/spreadsheets/'+year):
		os.mkdir('../../data/spreadsheets/'+year)
	
	createuser(student1, projectcode)
	if not student2==None:
		createuser(student2, projectcode)
		if not student3==None:
			createuser(student3, projectcode)
			if not student4==None:
				createuser(student4, projectcode)
	p('Project: ' + projectname + ' has been added successfully.')
except IOError:
	h('Unable to find file')
finally:
	close()

