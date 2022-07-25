#!/usr/bin/python3

# Import modules for CGI handling 
import cgi, cgitb 
from util.pythonHTML import *
import os

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
#Project Data
projectname = form.getvalue('projectname')
projectcode  = form.getvalue('projectcode')
year = form.getvalue('projectyear')
#Student Data
student1 = form.getvalue('student1')
student2 = form.getvalue('student2')
student3 = form.getvalue('student3')
student4 = form.getvalue('student4')

#return html

header()
h('tryung')

if projectname==None or projectcode==None or year==None:
	h('Please fill in all project fields')
	a('http://docs.simpledl.net/createprojects.html')
	close()
	exit()

try:
	file = open('../../data/spreadsheets/collections.csv', 'r')
	file.readline()

	for line in file:
		if line.split(',')[0]==(projectcode+year):
			h('Project Already Exists')
			close()
			file.close()
			exit()
	file.close()
	
	file = open('../../data/spreadsheets/collections.csv', 'a')
	file.write(projectcode+year+','+'\n')
	file.close()
	file = open('../../data/spreadsheets/students.csv', 'a')
	file.write(student1+','+projectcode+'\n')
	if not student2==None:
		file.write(student2+','+projectcode+'\n')
		if not student3==None:
			file.write(student3+','+projectcode+'\n')
			if not student4==None:
				file.write(student4+','+projectcode+'\n')
	file.close()
	
	h('All good')
except IOError:
	h('Unable to find file')
finally:
	close()

