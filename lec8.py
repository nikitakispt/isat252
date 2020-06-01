"""

lec 8

"""

def my_function(a,b):
    
    result = a + b
    
    print('a is ',a)
    print('b is ',b)
    return result
    
print(my_function(b=2,a=1))


#ex1

def calculate_abs(a):
    
    if type(a) is str:
        return ('wrong data type')
        
    elif a >=0:
        return
    else:
        return -a
        
print(calculate_abs('a'))

def cal_sigma(m,n):
    
    result = 0
    for i in range(n,m+1):
        result = result + i
        
    return result

print(cal_sigma(5,3))


