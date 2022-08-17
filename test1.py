#Operators

"""
print(2+3)
print(2-3)
print(2*3)
print(2/3)
print(5%3)
print(2**3)
print(3//2)  #floor division


if not(a<b and x>y):
    print("hello ")
else:
    print("ok")
    
x=10
y=5
a=3
b=4

print(id(x))
print(id(y))

print(x is not y)

name= ["hi", "john", "bill","pal"]

if "scott" not in name:
    print("Yes")
    
else:
    print("Not present")
    

name1=  5
print(type(name1))
print(dir(name1))
print(name1.lower())
k= 1j
print(type(k))

a=int(2.0)
print(type(a))

b=complex(5) 
print(type(b))


print(list(range(11,135,11)))

print(bin(1000))

blog= "hello world"


print(len(blog))
print(blog[11])
print(blog.upper())
#---------------------------------------------------------------------------
#Random
import random
import secrets

print(random.randint(0,10))
a= random.randint(0,10)
print(a)

print(random.randrange(0,20,5))

print(random.sample(range(0,55), 3))

secret_rand= secrets.randbelow(10)
print(secret_rand)
#---------------------------------------------------
#String slicing
msg= "   hello world  "

print(msg[3])

txt = "The best things, in, life are free!"
print("free" in txt)

print(txt[5:17])
print(txt[-20:-1])

print(msg.islower())
print(msg.strip())
print(msg.replace("hello", "hi"))
print(txt.split(","))
#All string methods return new values. They do not change the original string

#bool
x = "0"
y = 100

print(bool(x))
print(bool(y))
"""