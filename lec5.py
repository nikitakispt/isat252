"""
lecture 5 python note
"""

print(1 +

    2)
print([1,2,3,


        4,5,6]   )
m = 1+\
    2
print(m)

a = 123
print(id(123))
print(id(a))

a = [1,2,3]
b = [1,2,3]

print(a == b)
print( a is b)

print(id(a))
print(id(b))

x = None

print(id(None))
print(id(x))

y = []
print(y == None)

print(True and False)

print(False)

print(not 0)

if 2>1 :
    print('2>1')
    
if 2<=1:
    print('2<=1')
elif 2<=2:
    print('2<=2')
else:
    print('2>1')
    
if None:
    print(1)
elif {}:
    print(2)
elif '0' :
    print(3)
else:
    print(4)