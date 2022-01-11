#question 1
print('ques',1)
x=int(input("enter the first number:"))
y=int(input("enter the second number:"))
z=int(input("enter the third number:"))
#average of three numbers
avg=(x+y+z)/3
print('average=',avg)

print()

#question 2
print('ques',2)
#input from user for gross income and number of dependents
gi=int(input("entre gross income:"))
n=int(input("entre number of dependents:"))
#taxable income
ti=gi-10000-(n*3000)
print('taxable income=',ti)
#finding tax
tx=ti*20/100
print('tax=',tx)

print()

#question 3
print('ques',3)
#input from student
sid=int(input('enter your sid:'))
n=input('enter your name:')
g=input('enter your gender =f for female or m for male or u for unknown:')
c=input('enter your course name:')
cgpa=float(input('enter yout cgpa:'))
student=[sid,n,g,c,cgpa]
print('student:',student)

print()

#question 4
print('ques',4)
#taking input of marks
s1=int(input('enter marks of first student:'))
s2=int(input('enter marks of second student:'))
s3=int(input('enter marks of third student:'))
s4=int(input('enter marks of fourth student:'))
s5=int(input('enter marks of fifth student:'))
marks=[s1,s2,s3,s4,s5]
print('before sorting:',marks)
marks.sort()
#sorting a list
print('after sorting:',marks)

print()

#question 5
print('ques',5)
color=['red','green','white','black','pink','yellow']
print('color',color)
print()

#part a 
color.pop(3)
#after removing 4th element from the list
print('part(a),output color',color)

print()

#part b
color=['red','green','white','black','pink','yellow']
color.pop(3)
color.pop(3)
color.insert(3,'purple')
print('part(b),output color:',color)




 
