import os
import traceback

from util.pythonHTML import *

def getcookies():
	cookies={}
	if 'HTTP_COOKIE' in os.environ:
		for cookie in os.environ['HTTP_COOKIE'].split('; '):
			(key, value) = cookie.split('=')
			cookies[key]=value
	return cookies
	
def getUserID():
	try:
		cookies=getcookies()
		if cookies!={}:
			uid = cookies['userID']
			return uid
		else:
			return ''
	except:
		p(str(traceback.format_exc()))
		return ''
		
def isadmin():
	try:
		cookies=getcookies()
		if cookies!={}:
			return cookies['admin']==1
		else:
			return False
	except:
		p(str(traceback.format_exc()))
		return False

def getusername():
	try:
		cookies=getcookies()
		if cookies!={}:
			name = cookies['username']
			return name
		else:
			return ''
	except:
		p(str(traceback.format_exc()))
		return ''
