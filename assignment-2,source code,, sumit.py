print("answer 1")
string="python is a case sensitive language"
print(string)

print("\n (a)")
#length of the given sentance
print('length of string is:',len(string))

print("\n (b)")
#reversed string
print("reversed string:",string[::-1])

print('\n (c)')
p=(string[10:35])
print('new string:',p)

print('\n (d)')
print(string.replace('a case sensitive' , 'object oriented'))

print("\n (e)")
print("index of substring a:",string.find("a"))

print("\n (f)")
#removing white spaces from the string
print(string.replace(" ",""))


print("answer 2")
p=str(input("enter your name:"))
q=int(input("enter your SID:"))
r=str(input("department name:"))
s=float(input("enter your CGPA:"))
print('hey,'+p+' here!')
print('My SID is '+str(q))
print('I am from '+r+' department and my CGPA is '+str(s)) 



print("\n answer 3")
#bitwise operator
#      32 16 8 4 2 1
#a=56   1  1 1 0 0 0
#b=10   0  0 1 0 1 0
a=56
b=10
print('\n a&b is:',a&b)
print('\n a|b is:',a|b)
print('\n a^b is:',a^b)
print('\n a<<2:',a<<2,' , b<<2:',b<<2)
print('\n a>>2:',a>>2,' , b>>4:',b>>4)



print("\n answer 4")
a=int(input("first number:"))
b=int(input("second number:"))
c=int(input("third number:"))
if a>b and a>c :
   print('first is the greatest of three numbers')
elif b>c:
    print('second is the greatest of three numbers')
else:
    print('third is the greatest of three numbers')




print("\n answer 5 ")
x=str(input("enter the string:"))
if "name" in x:
    print("Yes")
else:
    print("No")


print("\n answer 6")
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
if a>b+c:
      print("given input lengths can form a triangle:NO")
elif b>a+c:
    print("given input lengths can form a triangle:NO")
elif c>a+b:
    print("given input lengths can form a triangle:NO")
else:
    print("given input lengths can form a triangle:YES")

   




