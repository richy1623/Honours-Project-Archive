#!/usr/bin/python3

# Import modules for CGI handling 

import cgi, cgitb 
import traceback
import os
from util.pythonHTML import *
from util.projectmanager import viewmetadata
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
bannersmall()
h('Displaying Metadata of Project')

if projectcode==None or year==None:
	printerror('Project not specified')

if not os.path.exists('../../db/project_data/'+year+'/'+projectcode+'/metadata.xml'):
	printerrorcode('No Metadata added for project')

#Get file to upload
try:
	metadata = viewmetadata(year, projectcode)
	if not metadata:
		p('Failed to display metadata for project')
	else:
		printmetadata(metadata)
except Exception as e:
	p(e)
close()
