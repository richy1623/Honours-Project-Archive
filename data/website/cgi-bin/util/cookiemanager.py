import os
import traceback

from util.pythonHTML import *

def getcookies():
	cookies={}
	if 'HTTP_COOKIE' in os.environ:
		for cookie in environ['HTTP_COOKIE'].split('; '):
			(key, value) = cookie.split('=');
			cookies[key]=value
	return cookies
	
def getUserID():
	try:
		cookies=getcookies()
		if cookies!={}:
			return cookies['userID']
		else:
			return ''
	except:
		p(str(traceback.format_exc()))
		
def getUserID2():
	return '1'
