import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_server = "smtp.gmail.com" 
smtp_port = 587 
email_address = "munjjac@gmail.com" 
password = "tnil bpzr ikie vnbp" 

recipient_email = "munjjac@hanmail.net" 

msg = MIMEMultipart()
msg['From'] = email_address
msg['To'] = recipient_email
msg['Subject'] = "hello"
message = "be happy" 
msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls() 
server.login(email_address, password)  
server.send_message(msg) 
server.quit()