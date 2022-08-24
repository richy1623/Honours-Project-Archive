#adds projects and users to the dl

import os
import shutil

#print(os.getcwd())
usrdir = '../../data/users/'
projdir = '../../data/projects/'
publicdir = '../../public_html/'
dbproj = '../../db/projects/'
dbprojdata = '../../db/project_data/'


def clearusers():
	for filename in os.listdir(usrdir):
		if filename.split('.')[0]!='1':
			os.remove(usrdir+filename)

	f = open(usrdir+'../../db/counter/users.counter', 'w')
	f.write('10')
	f.close()

def clearprojects():
	if os.path.exists(projdir):
		for filename in os.listdir(projdir):
			shutil.rmtree(projdir+filename) 
		
	if os.path.exists(dbprojdata):
		for filename in os.listdir(dbprojdata):
			shutil.rmtree(dbprojdata+filename) 

	if os.path.exists(dbproj):
		for filename in os.listdir(dbproj):
			shutil.rmtree(dbproj+filename)
			 
	if os.path.exists(publicdir+'collection/2020'):
		shutil.rmtree(publicdir+'collection/2020')
				 
	if os.path.exists(publicdir+'metadata/2020'):
		shutil.rmtree(publicdir+'metadata/2020')

	if os.path.exists(publicdir+'metadata/index.xml'):
		os.remove(publicdir+'metadata/index.xml')

def main():
	clearusers()
	clearprojects()

if __name__=='__main__':
	main()
