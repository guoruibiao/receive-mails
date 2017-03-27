# coding: utf8
from base64 import decodebytes
bytes = decodebytes(b'ufnosQ==')

print(str(bytes, 'gb18030'))

pop3server = "pop."+"1064319632@163.com".split('@')[-1]
print(pop3server)


ls = [1,2,3,4,5,6,7,8,9,0]
print(ls[-1:3])