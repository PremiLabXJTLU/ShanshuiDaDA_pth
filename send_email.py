import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

address = sys.argv[1]
attachment = sys.argv[2]


msg = MIMEMultipart('related')
msgText = MIMEText('Hey! This is DaDA sending you this email. Thanks to your kindly participance and here attached is the Shanshui painting we just created together, please check it out! And if you want to know more about DaDA, you can find more information here: http://www.aven.cc/DaDA , if you want reach out to Aven, the creator of this project, send him email to aven@nyu.edu or hi@aven.cc .')

img = open(attachment, 'rb').read()
msgImg = MIMEImage(img, 'jpg')
msgImg.add_header('Content-ID', '<image1>')
msgImg.add_header('Content-Disposition', 'inline', filename=attachment)

me = 'deeplearning4fun@163.com'
msg['Subject'] =  'Checkout the Shanshui Painting You Created with DaDA!'
msg['From'] = me
msg['To'] = address
msg.attach(msgText)
msg.attach(msgImg)

s = smtplib.SMTP(host = 'smtp.163.com',port = 25)
s.starttls()
s.login(me,'?')
s.send_message(msg)
s.quit()