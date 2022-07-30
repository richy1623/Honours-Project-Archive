#!/usr/bin/python3

# Import modules for CGI handling 

import cgi, cgitb 
import traceback
#import sys
#sys.path.append('cgi-bin')
#from util.pythonHTML import *
#from util.projectmanager import deletefile

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
year  = form.getvalue('year')
path  = form.getvalue('path')
filename  = form.getvalue('filename')

#return html

header()
h('Deleting Project... '+str(filename))
	
if filename==None or year==None or path==None:
	h('Project not specified')
	a('http://docs.simpledl.net/manageproject.py')
	close()
	exit()
	
try:
	#if deletefile(year, path, filename):
	#	p('Successfuly deleted '+filename)
	#else:
	#	p('Failed to delete '+filename)
	print('hello')
except Exception as e:
	p(str(traceback.format_exc()))
close()

