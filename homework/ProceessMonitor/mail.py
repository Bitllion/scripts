# 发送邮件
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
from config import config
def sendmail(content, title):
    # qq邮箱smtp服务器
    host_server = "smtp.qq.com"
    # sender_qq为发件人的qq号码
    sender_qq = config.mail
    # pwd为qq邮箱的授权码
    pwd = config.pwd
    # 发件人的邮箱
    sender_qq_mail = config.mail
    # 收件人邮箱
    receiver = config.receiver

    # 邮件的正文内容
    smtp = SMTP_SSL(host_server)
    smtp.set_debuglevel(1)
    smtp.ehlo(host_server)
    smtp.login(sender_qq, pwd)

    msg = MIMEText(content, "plain", "utf-8")
    msg["Subject"] = Header(title, "utf-8")
    msg["From"] = sender_qq_mail
    msg["To"] = receiver
    smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
    smtp.quit()