#!/usr/bin/python3

# Import modules for CGI handling 

import cgi, cgitb 
import traceback
from util.pythonHTML import *
from util.projectmanager import zipproject
from util.projectmanager import checkifdir

cgitb.enable()

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
year  = form.getvalue('year')
projectcode  = form.getvalue('projectcode')

#Helper functions
def printerror(error):
	p(error)
	close()
	exit()

#return html

header()
h('Adding file to Project')

if projectcode==None or year==None:
	printerror('File not specified')

#Get file to upload
try:
	if zipproject(year, projectcode):
		p('Successfully zipped project')
	else:
		p('Failed to zip project')
except Exception as e:
	p(e)
close()
