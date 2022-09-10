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

#return html

header()
banner()
h('Manage Projects')

#get project from cookies
uid = getUserID()
if uid=='':
	p('Please login to your account to access your project folder')
else:
	(year, project)=getYearAndProject(uid)
	if year=='' or project=='':
		p('User has not been assigned to a project. Please contact the administrator to add you to your assigned project')
	else:
		setuser(getstudentname(uid))
		p('Please click on your project name then select '+strong('Add File')+' to add a zip file containing your project\'s website. Afterwards you will be able to view your uploaded files\' structure and the current view of the website.')	
		p('Once your project has been uploaded, you will need to fill in your project\'s details in the metadata tab.')	
		br()
		p('When you are satisfied with your project upload you will be able to submit it for moderation.')
		br()
		h('Files', 2)
		script('setproject("'+project+'")')
		(table, dirs, selected) = displayprojectfiles(year, project, opendirs)
		tablegen3(table, dirs, selected)
		projectmenu()
		br()
		br()

close()
