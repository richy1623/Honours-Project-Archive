#adds projects and users to the dl

import os

#print(os.getcwd())


usrdir = '../users/'

f = open(usrdir+'../../db/counter/users.counter', 'r')
usercount=f.readline()
f.close()

projectcount=0
year=2020

for y in range(3):
	year=y+2020
	if not os.path.exists(usrdir+'../projects/'+str(year)):
		os.mkdir(usrdir+'../projects/'+str(year))
	if not os.path.exists(usrdir+'../spreadsheets/'+str(year)):
		os.mkdir(usrdir+'../spreadsheets/'+str(year))
	x=0
	for i in range(1,21):
		if i%20 in [1,2,4,7,11,12,14,17]:
			projectcount+=1
		i=i+20*y
		i=str(i)
		f = open(usrdir+usercount+'.email.xml', 'w')
		f.write('<email>user'+i+'@myuct.ac.za</email>')
		f.close()
		
		f = open(usrdir+usercount+'.profile.xml', 'w')
		f.write('<profile></profile>')
		f.close()
		
		f = open(usrdir+usercount+'.name.xml', 'w')
		f.write('<name>user'+i+'</name>')
		f.close()
		
		f = open(usrdir+usercount+'.permissions.xml', 'w')
		f.write('<permissions>project'+str(projectcount)+'</permissions>')
		f.close()
		
		f = open(usrdir+'../projects/'+str(year)+'/project'+str(projectcount)+'.txt', 'a')
		f.write('user'+i+'\n')
		f.close()
		
		usercount=str(int(usercount)+1)
		print('User: ' + 'user'+i + ' has been added to project '+str(projectcount)+' successfully.')

f = open(usrdir+'../../db/counter/users.counter', 'w')
f.write(usercount)
f.close()
