from socket import *

TO_ADDR = ('127.0.0.1', 8010)

fd = socket(AF_INET, SOCK_DGRAM)

msg = 'hello, world!'

fd.sendto(msg, TO_ADDR)


