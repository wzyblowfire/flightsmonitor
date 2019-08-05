# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 17:27:20 2019

@author: win 10
"""

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib
    
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# 输入Email地址和口令:
from_addr = 'wuziyue925@163.com'
password = '728722551wzy'
# 输入收件人地址:
to_addr = 'wuziyue925@foxmail.com'
# 输入SMTP服务器地址:
smtp_server = 'smtp.163.com'

message = '你好！\n' + '监测到最低价格为111\n' + 'https://flights.ctrip.com/international/search/oneway-hkg0-man?depdate=2019-09-17&cabin=y_s&adult=1&child=0&infant=0' 
msg = MIMEText(message, 'plain', 'utf-8')

msg['From'] = _format_addr('机票价格监测 <%s>' % from_addr)
msg['To'] = _format_addr('用户 <%s>' % to_addr)
msg['Subject'] = Header('出现低价机票', 'utf-8').encode()
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()