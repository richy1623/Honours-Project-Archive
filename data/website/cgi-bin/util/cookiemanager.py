import os
import traceback

from util.pythonHTML import *

def getcookies():
	"""fetches the cookies from the evnironmnet
	returns a dictionary with the cookies keys and values"""
	cookies={}
	if 'HTTP_COOKIE' in os.environ:
		for cookie in os.environ['HTTP_COOKIE'].split('; '):
			(key, value) = cookie.split('=')
			cookies[key]=value
	return cookies
	
def getUserID():
	"""fetches the userID from the cookie
	returns an empty string if there is no userID in the cookie"""
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
	"""fetches if the user is an admin from the cookie
	returns an empty string if there is no admin in the cookie"""
	try:
		cookies=getcookies()
		if cookies!={}:
			return cookies['admin']=='1'
		else:
			return False
	except:
		p(str(traceback.format_exc()))
		return False

def getusername():
	"""fetches the user name from the cookie
	returns an empty string if there is no userID in the user name"""
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
