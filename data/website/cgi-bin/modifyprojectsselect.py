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

if year!=None:
	h(year)
if projectcode!=None:
	h(projectcode)

try:
	table = []
	years=[]
	projects=[]
	students=[]
	path='../../data/projects/'
	for file in os.listdir(path):
		if file==year:
			years.append('<strong>'+file+'</strong>')
		else:
			years.append(file)
	if year!=None:
		path = path+year+'/'
		for file in os.listdir(path):
			if file==projectcode:
				projects.append('<strong>'+file+'</strong>')
			else:
				projects.append(file)
		if projectcode!=None:
			path = path+projectcode+'/'
			file = open(path+'students.txt')
			for line in file.readlines():
				students.append(line)
			file.close()
	table.append(years)
	table.append(projects)
	table.append(students)
	tablegen2(table)
except Exception as e:
	p(str(traceback.format_exc()))
close()

