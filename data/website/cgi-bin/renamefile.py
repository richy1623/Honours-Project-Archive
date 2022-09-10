#!/usr/bin/python3

# Import modules for CGI handling 

import cgi, cgitb 
import traceback
from util.pythonHTML import *
from util.projectmanager import renamefile

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
year  = form.getvalue('year')
path  = form.getvalue('path')
oldfilename  = form.getvalue('oldfilename')
newfilename  = form.getvalue('newfilename')

#return html

header()
bannersmall()
h('Renaming File')

if oldfilename==None or year==None:
	h('File not specified')
	a('http://docs.simpledl.net/manageproject.py')
	close()
	exit()

#path is alowed to be an empty string
if path==None:
	path=''

if newfilename==None:
	createrenamefileform(year, path, oldfilename)
else:
	try:
		if renamefile(year, path, oldfilename, newfilename):
			p('Successfuly renamed '+strong(oldfilename)+' to '+strong(newfilename))
		else:
			p('Failed to rename '+oldfilename)
		closebutton()
	except:
		p(traceback.format_exc())
close()
