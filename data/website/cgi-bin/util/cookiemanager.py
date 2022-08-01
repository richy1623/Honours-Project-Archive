import os
import traceback

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
			uid = cookies['userID']
			verify = cookies['verify']
			return cookies['userID']
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
		
def getUserID2():
	return '1'
