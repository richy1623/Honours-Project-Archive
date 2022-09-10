#!/usr/bin/python3

# Import modules for CGI handling 

import cgi, cgitb 
import traceback
from util.pythonHTML import *
from util.projectmanager import addfiletoproject
from util.projectmanager import checkifdir

cgitb.enable()

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
year  = form.getvalue('year')
path  = form.getvalue('path')
filename  = form.getvalue('filename')

#Helper functions
def printerror(error):
	smallp(error)
	close()
	exit()

#return html

header()
bannersmall()
smallh('Adding file to Project')

if filename==None or year==None:
	printerror('File not specified')

#path is alowed to be an empty string
if path==None:
	path=''
	
if not checkifdir(year, path, filename):
	printerror('Not a valid directory')

p('Inserting file into directory: '+strong(path+'/'+filename))

#Get file to upload
try:
	if 'uploadfile' not in form or form['uploadfile'].filename=='':
		smallp('Please upload a file below')
		createuploadform(['year', 'path', 'filename'],[year, path, filename])
	else:
		uploadfile = form['uploadfile']
		smallp('Recieved file: '+strong(uploadfile.filename))
		unzip  = form.getvalue('unzip')
		try:
			if addfiletoproject(year, path, filename, uploadfile, unzip!=None):
				smallp('Upload Successful')
			else:
				smallp('Upload Failed')
			closebutton()
		except:
			smallp(traceback.format_exc())
except Exception as e:
	smallp(e)
close()
