import os
#util/projectmanager.py
#set system path
import sys
if sys.path[0].split('/')[-1]=='test':
	sys.path[0]='/'.join(sys.path[0].split('/')[:-1])
	print('set path to: '+sys.path[0])
if os.getcwd().split('/')[-1]=='test':
	os.chdir('..')
	
filename = input('Enter a filename: ')

if not os.path.exists(filename):
	print('file does not exist')
	print(os.listdir())
	exit()
	
filetotest = open(filename, 'r')
print('reading file '+filename)

testfile = open('test/test_'+filename.split('/')[-1], 'w')
print('creating file '+testfile.name)
testfile.write('''
import unittest

#set system path
import sys
if sys.path[0].split('/')[-1]=='test':
	sys.path[0]='/'.join(sys.path[0].split('/')[:-1])
	print('set path to: '+sys.path[0])
	
from test import cleardl, filldl
''')

for line in filetotest:
	if line[:3]=='def':
		print('\tcreating method for '+line[4:line.index('(')])
		testfile.write('\n\ndef test_'+line[4:line.index('(')]+'(unittest.TestCase):\n')
		testfile.write('\t@classmethod\n')
		testfile.write('\tdef setUpClass(cls):\n')
		testfile.write('\t\t#setup any data structures for class\n\t\tTrue\n\n')
		
		testfile.write('\tdef test_normal_case(self):\n')
		testfile.write('\t\t#code goes here\n')

print('finished writing to file '+testfile.name)
filetotest.close()
testfile.close()
