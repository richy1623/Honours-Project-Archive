#!/usr/bin/python3

# Import modules for CGI handling 
import cgi, cgitb 
import os
import traceback
from util.pythonHTML import *
from util.cookiemanager import *
from util.usermanager import *
from util.projectmanager import *

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
opendirs=[]
depth=1
try:
	while True:
		value = form.getvalue('d'+str(depth))
		if value!=None:
			opendirs.append(value)
			depth+=1
		else:
			break
except:
	p(str(traceback.format_exc()))
#get project from cookies
uid = getUserID2()
projectyear=getProjectYear(uid)

#return html

header()
h('Manage Projects')		

displayprojectfiles(projectyear, opendirs)

close()
