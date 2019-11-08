set -ex
python train.py --dataroot ./datasets/Sketch2Shanshui --name Sketch2Shanshui --model cycle_gan --pool_size 50 --no_dropout --display_id 0


python << END
import smtplib
from email.mime.text import MIMEText
msg = MIMEText('Hey! Model training is done! Check out http://10.7.6.75:8097')
me = 'deeplearning4fun@163.com'
msg['Subject'] =  'DaDA is done!'
msg['From'] = me
msg['To'] = 'mr.labmanager@icloud.com,aven@nyu.edu'
s = smtplib.SMTP(host = 'smtp.163.com',port = 25)
s.starttls()
s.login(me,'deeplearning4fun')
s.send_message(msg)
s.quit()
print("Email is sent...")
END

python -m visdom.server
