#adds projects and users to the dl

import os
import shutil

#print(os.getcwd())


usrdir = '../users/'
projdir = '../projects/'
publicdir = '../../public_html/'
dbproj = '../../db/projects/'
dbprojdata = '../../db/project_data/'

if os.path.exists(usrdir):
	for filename in os.listdir(usrdir):
		if filename.split('.')[0]!='1':
			os.remove(usrdir+filename)
		
if os.path.exists(projdir):
	for filename in os.listdir(projdir):
		shutil.rmtree(projdir+filename)
	 
if os.path.exists(dbprojdata):
	for filename in os.listdir(dbprojdata):
		shutil.rmtree(dbprojdata+filename) 

if os.path.exists(dbproj):
	for filename in os.listdir(dbproj):
		shutil.rmtree(dbproj+filename)
for i in ['2020', '2021', '2022', '2023']: 
	if os.path.exists(publicdir+'collection/'+i):
		shutil.rmtree(publicdir+'collection/'+i)
				 
	if os.path.exists(publicdir+'metadata/'+i):
		shutil.rmtree(publicdir+'metadata/'+i)

if os.path.exists(publicdir+'metadata/index.xml'):
	os.remove(publicdir+'metadata/index.xml')

f = open(usrdir+'../../db/counter/users.counter', 'w')
f.write('10')
f.close()
