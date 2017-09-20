from email.mime.text import MIMEText

def send_email(email, height)
	from_email = "davidjordanmcr@gmail.com"
	from_password = ""
	to_email = email
	
	subject = "Height data"
	message = "Hey there, your height is %s." % height
	
	msg = MIMEText(message, 'html')
	msg['Subject'] = subject
	msg['to'] = to_email
	msg['from'] = from_email
	
	gmail = smtplib.SMTP('smtp.gmail.com', 587)
	