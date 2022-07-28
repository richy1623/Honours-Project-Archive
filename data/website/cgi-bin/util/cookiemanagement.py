import os

from util.pythonHTML import *

usrdir = '../../data/users/'
	
def getcookies();
	cookies={}
	if 'HTTP_COOKIE' in os.environ:
		for cookie in environ['HTTP_COOKIE'].split('; '):
			(key, value) = cookie.split('=');
			cookies[key]=value
	return cookies
	
def getUserID():
	cookies=getcookies()
	if cookies!={}:
		return cookies['userID']
	else:
		return ''
