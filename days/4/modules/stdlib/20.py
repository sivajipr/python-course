import zlib

s = 'this is a looooooooooooooooooooooooong string'

print len(s)

t = zlib.compress(s)

print len(t)

print zlib.decompress(t)
