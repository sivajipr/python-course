from socket import *

LOCAL_ADDR = ('127.0.0.1', 8010)
MSG_LEN = 1000

fd = socket(AF_INET, SOCK_DGRAM)

fd.bind(LOCAL_ADDR)

s = fd.recvfrom(MSG_LEN)

print s

