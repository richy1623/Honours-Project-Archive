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
path  = form.getvalue('path')
filename  = form.getvalue('filename')
title  = form.getvalue('title')
supervisor  = form.getvalue('supervisor')
students=[]
for i in range(1,5):
	s = form.getvalue('student'+str(i))
	if s!=None:
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
h('Adding file to Project')

if year==None:
	printerror('Year not specified')

projectcode=''
if path==None:
	path=''
	if filename!=None:
		projectcode=filename
else:
	projectcode=path.split('/')[0]
	filename=''

if projectcode=='':
	printerror('Project not specified')

if not checkifdir(year, '', projectcode):
	printerror('Not a valid direcotry')

p('Adding Metadata to project '+strong(projectcode))

#Get file to upload
try:
	if title==None or supervisor==None or students==[]:
		if not (title==None and supervisor==None and students==[]):
			p('Title, Supervisor and one or more students are required')
		createmetadataform(projectcode, year, path, filename)
	else:
		if addmetadata(year, projectcode, title, students, supervisor):
			p('Metadata added Successfuly')
		else:
			p('Failed to add Metadata')
except Exception as e:
	p(e)
close()
