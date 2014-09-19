import urllib2

f = urllib2.urlopen('http://pramode.net')

for line in f:
    print line
