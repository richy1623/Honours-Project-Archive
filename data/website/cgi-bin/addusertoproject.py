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
bannersmall()
if student==None:
	s('User not specified')
	a('http://docs.simpledl.net/modifyprojectsselect.py')
	close()
	exit()
else:
	h('Adding '+student+' to '+str(project))
	
if year==None or project==None:
	h('Project not specified')
	a('http://docs.simpledl.net/modifyprojectsselect.py')
	close()
	exit()
	
try:
	studentid=getstudentid(student)
	if studentid=='':
		createuser(student)
	if addusertoproject(student, studentid, year, project):
		p('Successfuly added '+student)
	else:
		p('Failed to add '+student)
except Exception as e:
	p(str(traceback.format_exc()))
close()
