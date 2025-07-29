"""
#===============
#Celsius --->Farenheit
c=input('Celsius:  ')
c=float(c)
f=(c*9/5) +32
print('Farenheit is ',f)

#===============
#Farenheit ---> Celsius
f=input('Farenheit is  ')
f=float(f)
c=5/9*(f-32)
print('Celsius is ',c)

#===============
#SI calculator
p=input('principal: ')
t=input('time: ')
r=input('rate: ')

p=int(p)
t=int(t)
r=int(r)
si =p * t * r
print( 'simple interest is', si)

#===============
#check the input method
time= input(  )
print(time)

#===============
#print absolute value
print(abs(-92883))

#===============
#print max value
print(max(4,5,6,1,22,3,5))

#===============
#print min value
print(min(892,11,2,0,99,3))

#===============
#print power operation
print(pow(2,6))

#===============
a=6
if a>5:
    print("a is greater than 5")
print("none")
#===============
#if_else statement
a= int(input( 'age of a girl is : '))

if a>=40:
    print("age is good")
else :
    print('age is not good')
print('thank you')
#===============
# elif statement -- math operation example
operand1=int(input('operand1 is  '))
operand2=int(input('operand2 is  '))
operator=input('+,-,*,/'  )

if (operator=='+'):
    print('addition is', operand1+operand2)
elif(operator=='-'):
    print('substraction is', operand1-operand2)
elif(operator=='*'):
    print('multiplication is', operand1*operand2)
elif(operator=='/'):
    print('division is', operand1/operand2)
else:
    print('none ')
print('thank you')
#===============
# range functions usage
n=list(range(0, 10, 2))
print(n)
#===============
"""
n=list(range(1, 10))
print(n)