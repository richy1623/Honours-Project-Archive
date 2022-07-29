#!/usr/bin/python3

# Import modules for CGI handling 
import cgi, cgitb 
from util.pythonHTML import *
from util.projectmanager import *
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
students = []
for i in range(4):
	student = form.getvalue('student'+str(i))
	if student!=None:
		students.append(student)

#return html

header()
h('Attempting to create project...')		

if projectname==None or projectcode==None or year==None:
	h('Please fill in all project fields')
	a('http://docs.simpledl.net/createprojects.html')
	close()
	exit()

success = createproject(projectname, projectcode, year, students)
if success:
	p('Project: ' + projectname + ' has been added successfully.')
else:
	p('Project: ' + projectname + ' was unable to be added.')

a('http://docs.simpledl.net/')

close()

