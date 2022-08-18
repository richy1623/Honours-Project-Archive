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
bannersmall()
smallh('Adding projects with CSV upload')



#Get file to upload
try:
	if 'uploadfile' not in form or form['uploadfile'].filename=='':
		smallp('Please upload a file below')
		createuploadformcsv(year)
	elif year==None:
		smallp('Please enter the year')
		createuploadformcsv(year)
	else:
		uploadfile = form['uploadfile']
		smallp('Recieved file: '+strong(uploadfile.filename))
		try:
			result = createprojectscsv(uploadfile, year)
			if result:
				smallp('Upload Successful')
			else:
				smallp('Upload Failed')
		except:
			smallp(traceback.format_exc())
except Exception as e:
	smallp(e)
close()
