import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email = 'pattnaikrissan27@gmail.com'
password = 'Wipro@1234'
sent_to_email = '123rissan@gmail.com'
subject = 'Test Email'
message = 'This is a sample message'

msg=MIMEMultipart()
msg['From'] = email
msg['To'] = sent_to_email
msg.attach(MIMEText(message, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
text = msg.as_string()
server.sendmail(email, sent_to_email, text)
