
import struct

f = open('dat', 'r')

data = f.read()

print struct.unpack('iii', data)

