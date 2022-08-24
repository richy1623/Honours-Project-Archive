#!/usr/bin/python3

# Import modules for CGI handling 

import cgi, cgitb 
import traceback
from util.pythonHTML import *
from util.projectmanager import deletefile

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
year  = form.getvalue('year')
path  = form.getvalue('path')
filename  = form.getvalue('filename')

#return html

header()
bannersmall()
h('Deleting File from Project')

if filename==None or year==None:
	h('File not specified')
	close()
	exit()

#path is alowed to be an empty string
if path==None:
	p('Unable to delete root file directory')
else:
	try:
		if deletefile(year, path, filename):
			p('Successfuly deleted '+filename)
		else:
			p('Failed to delete '+filename)
	except:
		p(traceback.format_exc())
close()
