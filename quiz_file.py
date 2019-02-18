import socket
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#
message = "Your message"  # Type your message
msg = MIMEMultipart()
password = "********"  # Type your password
msg['From'] = "petertountas1@gmail.com"  # Type your own gmail address
msg['To'] = "petertountas1@gmail.com"  # Type your friend's mail address
msg['Subject'] = "title"  # Type the subject of your message
msg.attach(MIMEText(message, 'plain'))
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()
server.login(msg['From'], password)
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()