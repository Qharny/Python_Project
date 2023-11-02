import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("your_email", "your_password")

msg = "Hello, this is a test email!"
server.sendmail("your_email", "recipient_email", msg)
server.quit()