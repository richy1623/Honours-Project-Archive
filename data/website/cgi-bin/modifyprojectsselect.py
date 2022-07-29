#!/usr/bin/python3

# Import modules for CGI handling 
import cgi, cgitb 
import os
import traceback
from util.pythonHTML import *

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
year = form.getvalue('year')
projectcode  = form.getvalue('projectcode')

#return html

header()
h('Modify Projects')		

try:
	table = []
	years=[]
	projects=[]
	students=[]
	yearindex=-1
	projectindex=-1
	path='../../data/projects/'
	if not os.path.exists(path):
		os.mkdir(path)
	for index, file in enumerate(sorted(os.listdir(path))):
		if file==year:
			yearindex=index
		years.append(file)
	if year!=None:
		path = path+year+'/'
		for index, file in enumerate(sorted(os.listdir(path))):
			file=file.rpartition('.')[0]
			if file==projectcode:
				projectindex=index
			projects.append(file)
		if projectcode!=None:
			file = open(path+projectcode+'.txt')
			for line in sorted(file.readlines()):
				students.append(line)
			file.close()
	table.append(years)
	table.append(projects)
	table.append(students)
	tablegen2(table, yearindex, projectindex)
	invisrefresh()
	br()
	a('http://docs.simpledl.net')
except Exception as e:
	p(str(traceback.format_exc()))

close()
