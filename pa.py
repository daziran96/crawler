import datetime
import time
from chinese_calendar import is_workday
import smtplib
from email.mime.text import MIMEText
from email.header import Header


startDate = datetime.datetime(2022, 2, 21)
date = datetime.datetime.now().date()


if is_workday(date):
    file = open('1', encoding= 'utf-8')
    text = file.readline()  # 只读取一行内容
    if text.find("|"):
        text = text.replace('|', r'<br>-')
        text = '-' + text
    print(text)
    file.close()

    with open("1", "r", encoding="utf-8") as f:
        lines = f.readlines()
        # print(lines)
    with open("1", "w", encoding="utf-8") as f_w:
        for line in lines[1:]:
            f_w.write(line)


    msg_from = '499952297@qq.com'  # 发送方邮箱

    passwd = 'hybpnudncanabgfe'  # 填入发送方邮箱的授权码
    msg_to = ['499952297@qq.com', 'liu.sophie@cummins.com', 'liziran2@huawei.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    subject = '【' +  time.strftime('%m-%d',time.localtime(time.time())) + '】讲给禹宸的土味情话~'
    content = text
    msg = MIMEText(content, "html")
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = Header("Sophie Liu", 'utf-8')
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 邮件服务器及端口号
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
    finally:
        s.quit()
