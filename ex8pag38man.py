a='A B C D E F G Y Z I'
for i in range(0,len(a)) :
    if ord(a[i])>65 and ord(a[i])<89 :
        print(a[i])
b='D G Y Z Z B D N'
for i in range(0,len(b)) :
    k=b.replace('Z','A')
print('b)',k)
c='A B N M N Z Y'
for i in range(0,len(c)) :
    y=c.replace(' ','-')
print('c)',y)