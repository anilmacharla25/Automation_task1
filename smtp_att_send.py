
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "anil.macharla25@gmail.com"
toaddr = "macharlanil@gmail.com"

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "SUBJECT OF THE EMAIL"

body = "TEXT YOU WANT TO SEND"

msg.attach(MIMEText(body, 'plain'))

filename = "19-Apr-2022-04-41-07.pdf"
attachment = open("C:\\sequelstring1.0\\task1\\New folder\\19-Apr-2022-04-41-07.pdf", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "pwd5")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
print("done")
