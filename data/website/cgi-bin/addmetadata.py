#!/usr/bin/python3

# Import modules for CGI handling 

import cgi, cgitb 
import traceback
from util.pythonHTML import *
from util.projectmanager import addmetadata
from util.projectmanager import checkifdir

cgitb.enable()

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
year  = form.getvalue('year')
projectcode  = form.getvalue('projectcode')
filename  = form.getvalue('filename')
title  = form.getvalue('title')
supervisor  = form.getvalue('supervisor')
description  = form.getvalue('description')
students=[]
for i in range(1,5):
	s = form.getvalue('student'+str(i))
	if s!=None and s!='':
		students.append(s)
	else:
		break

#Helper functions
def printerror(error):
	p(error)
	close()
	exit()

#return html

header()
h('Adding Metadata to Project')

if year==None:
	printerror('Year not specified')

if projectcode==None:
	printerror('Project not specified')

if not checkifdir(year, '', projectcode):
	printerror('Not a valid direcotry')

if 'image' not in form or form['image'].filename=='':
	image=None
else:
	image = form['image']
	
p('Adding Metadata to project '+strong(projectcode))

#Get file to upload
try:
	if title==None or supervisor==None or students==[] or description==None:
		if not (title==None and supervisor==None and students==[] and description==None):
			p('Title, Supervisor, a description and one or more students are required')
		createmetadataform(projectcode, year)
	else:
		if addmetadata(year, projectcode, title, students, supervisor, description, image):
			p('Metadata added Successfuly')
		else:
			p('Failed to add Metadata')
except:
	p(traceback.format_exc())
close()
