import smtplib
sender_email = "pattnaikrissan27@gmail.com"
rec_email = "123rissan@gmail.com"
password = input(str("Please enter your password:"))
message = "Hey"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
print("Login Successful")
server.send_message(sender_email, rec_email, message)
print("Email is sent to ", rec_email)
