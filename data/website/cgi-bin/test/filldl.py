#adds projects and users to the dl

import os

#print(os.getcwd())


usrdir = '../../data/users/'

def main():
	f = open(usrdir+'../../db/counter/users.counter', 'r')
	usercount=f.readline()
	f.close()

	projectcount=0
	year=2020

	if not os.path.exists(usrdir+'../projects/'):
		os.mkdir(usrdir+'../projects/')
	if not os.path.exists('../../db/projects/'):
					os.makedirs('../../db/projects/')
	if not os.path.exists('../../db/project_data/'):
					os.makedirs('../../db/project_data/')
		
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
				if not os.path.exists('../../db/projects/'+str(year)+'/project'+str(projectcount)):
					os.makedirs('../../db/projects/'+str(year)+'/project'+str(projectcount))
				if not os.path.exists('../../db/project_data/'+str(year)+'/project'+str(projectcount)):
					os.makedirs('../../db/project_data/'+str(year)+'/project'+str(projectcount))
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
			f.write('<code>project'+str(projectcount)+'</code>\n')
			f.write('<year>'+str(year)+'</year>')
			f.close()
			
			f = open(usrdir+'../projects/'+str(year)+'/project'+str(projectcount)+'.txt', 'a')
			f.write('user'+i+'\n')
			f.close()
			
			usercount=str(int(usercount)+1)
			print('User: ' + 'user'+i + ' has been added to project '+str(projectcount)+' successfully.')

	f = open(usrdir+'../../db/counter/users.counter', 'w')
	f.write(usercount)
	f.close()

if __name__=='__main__':
	main()
