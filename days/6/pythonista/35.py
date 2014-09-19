# warning: dangerous if template string is externally specified

def fun():
    name = 'ravi'
    score = 100
    
    print 'hello %(name)s, your score is %(score)d' % locals()

fun()


