import sys
import smtplib
import optparse
from email import Encoders
from email.MIMEBase import MIMEBase
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart

def send_email_text (user, pwd, to, subject, text):
	msg = MIMEText(text)
	msg['FROM'] = user
	msg['To'] = to
	msg['Subject'] = subject
	try:
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.ehlo()
		server.starttls()
		server.login(user, pwd)
		server.sendmail(user, to, msg.as_string())
		server.close()
	except:
		print("failed")

def send_email(user, pwd, to, subject, text, attachment):
	if (attachment == "None"):
		msg = MIMEText(text)
	else:
		msg = MIMEMultipart(text)
		part = MIMEBase('application', "octet-stream")
		part.set_payload(open(attachment, "rb").read())
		Encoders.encode_base64(part)
		part.add_header('Content-Disposition', 'attachment; filename=' + attachment)
		msg.attach(part)

	msg['FROM'] = user
	msg['To'] = to
	msg['Subject'] = subject

	try:
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.ehlo()
		server.starttls()
		server.login(user, pwd)
		server.sendmail(user, to, msg.as_string())
		server.close()
		print("done")
	except:
		print("failed")

#		MAIN METHOD
if __name__ == '__main__':

	argList = sys.argv
	argList.pop(0)

	if (argList==[]):
		print("To:")
		to = raw_input()
		print "Text:"
		text = raw_input()
		print "Subject:"	
		subject = raw_input()
		print "File to attach:"
		attachment = raw_input()			
	elif len(argList)==1:
		if (argList == ["-h"]):
			print ("usage: sender <address> <text> <subject> <attachment>")
			sys.exit()
		else:
			to = argList[0]
			text = ''
			subject = 'from xerxes'
			attachment = ''
	elif (len(argList)==2):
		to = argList[0]
		text = argList[1]	
		subject = argList[2]
		attachment = ''			
	elif (len(argList)>2):
		to = argList[0]
		text = argList[1]		
		subject = argList[2]
		attachment = argList[3]			
	
	user = #GMAIL ADDRESS
	pwd  = #GMAIL PASSWORD
	send_email(user, pwd, to, subject, text, attachment)
