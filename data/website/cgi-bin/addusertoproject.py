#!/usr/bin/python3

# Import modules for CGI handling 
import cgi, cgitb 
import os
import traceback
from util.pythonHTML import *
from util.projectmanager import addusertoproject
from util.usermanager import *

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
year  = form.getvalue('year')
project  = form.getvalue('project')
student = form.getvalue('student')

#return html

header()
if student== None:
	h('Adding user to '+str(project))
else:
	h('Adding '+student+' to '+str(project))
	
if year==None or project==None:
	h('Project not specified')
	a('http://docs.simpledl.net/modifyprojectsselect.py')
	close()
	exit()
	
try:
	if student==None:
		formlist(getallstudents(), 'addusertoproject.py', hidden=[['year',year],['project',project]])
	else:
		studentid=getstudentid(student)
		if studentid!='':
			if addusertoproject(student, studentid, year, project):
				p('Successfuly added '+student)
			else:
				p('Failed to add '+student)
		else:
			p('Invalid student number')
except Exception as e:
	p(str(traceback.format_exc()))
close()
