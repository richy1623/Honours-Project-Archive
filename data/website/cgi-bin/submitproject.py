#!/usr/bin/python3

# Import modules for CGI handling 

import cgi, cgitb 
import traceback
from util.pythonHTML import *
from util.projectmanager import submitmoderation

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
h('Adding file to Project')

if projectcode==None or year==None:
	printerror('Project not specified')

#Get file to upload
try:
	result=submitmoderation(year, projectcode)
	if result:
		p('Successfully submited project for moderation. An email will be sent after the project has been moderated informing you of the outcome.')
	else:
		p('Failed to submit for moderation')
except Exception as e:
	p(e)
close()
