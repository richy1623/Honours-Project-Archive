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
bannersmall()
h('Create Project')		
p('Enter each Project and add the students in the project team')

if projectname==None or projectcode==None or year==None:
	if not (projectname==None and projectcode==None and year==None):
		h('Please fill in all project fields', level=2)
	createprojectform()
	close()
	exit()

success = createproject(projectname, projectcode, year, students)
if success:
	p('Project: ' + projectname + ' has been added successfully.')
else:
	p('Project: ' + projectname + ' was unable to be added.')

closebutton()

close()

