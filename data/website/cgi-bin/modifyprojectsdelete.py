#!/usr/bin/python3

# Import modules for CGI handling 
import cgi, cgitb 
import os
import traceback
from util.pythonHTML import *
from util.usermanager import deleteuser

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
student  = form.getvalue('student')
year  = form.getvalue('year')
project  = form.getvalue('project')

#return html

header()
bannersmall()
h('Deleting User '+str(student))
	
if student==None or year==None or project==None:
	h('Student not specified')
	a('http://docs.simpledl.net/modifyprojectsselect.py')
	close()
	exit()
	
try:
	if deleteuser(student, year, project):
		p('Successfuly deleted '+student)
	else:
		p('Failed to delete '+student)
except Exception as e:
	p(traceback.format_exc())
close()

