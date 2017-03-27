# coding: utf8

import poplib

# 邮箱个人信息
useraccount = 'spidersmall@163.com'
password = 'guoruibiao285514'
# 邮件服务器地址
pop3_server = 'pop.163.com'

# 开始连接到服务器
server = poplib.POP3(pop3_server)
# 可选项： 打开或者关闭调试信息，1为打开，会在控制台打印客户端与服务器的交互信息
server.set_debuglevel(1)
# 可选项： 打印POP3服务器的欢迎文字，验证是否正确连接到了邮件服务器
print(server.getwelcome().decode('utf8'))

# 开始进行身份验证
server.user(useraccount)
server.pass_(password)

# 返回邮件总数目和占用服务器的空间大小（字节数）， 通过stat()方法即可
print("Mail counts: {0}, Storage Size: {0}".format(server.stat()))
# 使用list()返回所有邮件的编号，默认为字节类型的串
resp, mails, octets = server.list()
print("响应信息： ", resp)
print("所有邮件简要信息： ", mails)
print("list方法返回数据大小（字节）： ", octets)

# 关闭与服务器的连接，释放资源
server.close()

