#!/usr/bin/python3

# Import modules for CGI handling 

import cgi, cgitb 
import traceback
from util.pythonHTML import *
from util.projectmanager import createprojectscsv

cgitb.enable()

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
year  = form.getvalue('year')

#Helper functions
def printerror(error):
	p(error)
	close()
	exit()

#return html

header()
h('Adding projects with CSV upload')



#Get file to upload
try:
	if 'uploadfile' not in form or form['uploadfile'].filename=='':
		p('Please upload a file below')
		createuploadformcsv(year)
	elif year==None:
		p('Please enter the year')
		createuploadformcsv(year)
	else:
		uploadfile = form['uploadfile']
		p('Recieved file: '+strong(uploadfile.filename))
		try:
			result = createprojectscsv(uploadfile, year)
			if result:
				p('Upload Successful')
			else:
				p('Upload Failed')
		except:
			p(traceback.format_exc())
except Exception as e:
	p(e)
close()
