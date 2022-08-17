#!/usr/bin/python3

# Import modules for CGI handling 
import cgi, cgitb 
import os
import traceback
from util.cookiemanager import *
from util.pythonHTML import *
from util.projectmanager import approveproject, denyproject, getpendingprojects

#Helper functions
def printerror(error):
	p(error)
	close()
	exit()

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
projectapprove = form.getvalue('projectapprove')
projectdeny = form.getvalue('projectdeny')
reason = form.getvalue('reason')
year = form.getvalue('year')

#return output
header()
banner()
setuser(getusername2())
h('Manage Projects')		
br()

if projectapprove==None and projectdeny==None:
	displayprojectapprovalpage(getpendingprojects())
else:
	if year==None:
		printerror('Year is missing. Please try again')
	if projectapprove!=None:
		result = approveproject(year, projectapprove)
		if result:
			p('Successfully Approved Project '+strong(projectapprove))
		else:
			p('Failed to Approve Project '+strong(projectapprove))
	else:
		result = denyproject(year, projectdeny, reason)
		if result:
			p('Successfully Rejected Project '+strong(projectdeny))
		else:
			p('Failed to Reject Project '+strong(projectdeny))
	

close()
