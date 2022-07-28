#adds projects and users to the dl

import os
import shutil

#print(os.getcwd())


usrdir = '../users/'
projdir = '../projects/'
dbproj = '../../db/projects/'

for filename in os.listdir(usrdir):
	if filename.split('.')[0]!='1':
		os.remove(usrdir+filename)

for filename in os.listdir(projdir):
	shutil.rmtree(projdir+filename) 

if os.path.exists(dbproj):
	for filename in os.listdir(dbproj):
		shutil.rmtree(dbproj+filename) 

f = open(usrdir+'../../db/counter/users.counter', 'w')
f.write('10')
f.close()
