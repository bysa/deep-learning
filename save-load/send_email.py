import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from myconfig import username, password

email = username
password = password
send_to_email = 'shafighparsazad@gmail.com'
subject = 'This is the subject'
message = 'This is my message'

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject

msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
text = msg.as_string()
server.sendmail(email, send_to_email, text)
server.quit()
