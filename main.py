# -*- coding: utf-8 -*-

import urllib2, base64
from BeautifulSoup import BeautifulSoup
import smtplib
import time
from email.mime.text import MIMEText

def mail(body):
    mail_body=body
    mail_from='363602094@qq.com'
    mail_to=['13522032151@139.com']
    msg=MIMEText(mail_body, _subtype='plain', _charset='UTF-8')
    msg['Subject']='Every day every news'
    msg['From']=mail_from
    msg['To']=';'.join(mail_to)
    msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')
    smtp=smtplib.SMTP()
    smtp.connect('smtp.qq.com')
    smtp.login('363602094@qq.com','!@#zx19880427')
    smtp.sendmail(mail_from,mail_to,msg.as_string())
    smtp.quit()
    print 'ok'

if __name__ == '__main__':
    url = 'http://192.168.1.1/userRpm/StatusRpm.htm'
    login_user = 'admin'
    login_pw = 'admin'

    auth = 'Basic ' + base64.b64encode(login_user + ':' + login_pw)
    heads = { 'Referer' : url,
             'Authorization' : auth
    }
    
    request = urllib2.Request(url, None, heads)
    response = urllib2.urlopen(request).read()
    parse_html = BeautifulSoup(response)
    n = 0
    l = []
    for line in response.splitlines():
        if line == 'var wanPara = new Array(':
            n = 4
            pass
        if n > 0:
            l.append(line)
            n -= 1

    ip = l[-1].replace(',', '').replace('"', '')
    print ip

    last_fip = open('./last_foreign_ip', 'a+')

    if ip != last_fip.read():
        mail(ip)
        last_fip.seek(0)
        last_fip.truncate()
        last_fip.write(ip)
        pass
    last_fip.close()