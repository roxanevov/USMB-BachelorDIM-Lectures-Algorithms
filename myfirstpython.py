#python trials script
print('basic loop example...')
a=0
for i in xrange(10):
    a=a+i
print('a='+str(a))

if a>10:
    print('a>10')
elif a>5:
    print('a>5... never displayed...')

