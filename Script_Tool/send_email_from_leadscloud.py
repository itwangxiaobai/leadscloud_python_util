# -*- coding: utf-8 -*-
# @Time: 2019/2/28 16:43
# @Author : Yang DaWei
# @Project : LeadsCloudAutomation
# @FileName: send_email_from_leadscloud.py

import smtplib
# import requests
# import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import time
from time import ctime


mail_host="smtp.gmail.com"
mail_user="davieyang000000@gmail.com"
mail_pass="alex005x"
sender = "davieyang000000@gmail.com"
receivers = ['alexyang_cool@163.com', 'leadscloud@sohu.com']



# , 'momjiang@163.com'


for i in range(1000):

    try:
        message = MIMEMultipart()
        message['From'] = Header(u"询盘云"+str(i+1)+"第封邮件")
        message['To'] = ','.join(receivers)
        message['Subject'] = Header(u'来自询盘云的第'+str(i+1)+'邮件', 'utf-8').encode()
        message.attach(MIMEText('询盘云IMAP发件箱同步', 'plain', 'utf-8'))
        """
        定义附件
        """
        att = MIMEText(open('resource.txt', 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="resource.txt"'
        message.attach(att)
        smtp = smtplib.SMTP_SSL(host=mail_host)
        smtp.connect(host=mail_host, port=465)
        smtp.login(mail_user, mail_pass)
        # smtp.sendmail(sender, message['To'].split(','), message.as_string())
        smtp.sendmail(sender, message['To'].split(','), message.as_string())
        # string = 
        print("在%s第" %ctime()+str(i+1)+"封邮件发送")
        smtp.quit()
        time.sleep(20)
		
    except smtplib.SMTPException as e:
        raise e

"""
try:
    smtpObj = smtplib.SMTP(mail_host)
    smtpObj.connect(mail_host, 587)
    smtpObj.starttls()
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as e:
    raise e
"""
# 等待3秒
# time.sleep(60)

"""
调用同步收信接口，并打印结果
"""

