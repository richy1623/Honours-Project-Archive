import smtplib
import traceback
from util.pythonHTML import *

def sendemail(recipient, subject, body):
	user = 'newhonoursarchive@gmail.com'
	recipient = recipient if isinstance(recipient, list) else [recipient]
	#TODO remove
	recipient = ['newhonoursarchive+'+i.split('@')[0]+'@gmail.com' for i in recipient]
	p('Sending emails to: '+', '.join(recipient))
	
	pwd='pnwuuewsvnmybvgd'
	
	# Prepare actual message
	message = """From: %s\nTo: %s\nSubject: %s\n\n%s
	""" % (user, ", ".join(recipient), subject, body)
	try:
		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.ehlo()
		server.starttls()
		server.login(user, pwd)
		server.sendmail(user, recipient, message)
		server.close()
		return True
	except:
		p(traceback.format_exc())
		return False

