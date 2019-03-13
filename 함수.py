"""#
def squareReturn(n):
    return n*n
#
def add2(n,k):
    return n+k

a=float(input('실수입력:'))
b=float(input('실수입력:'))
print(a,'+',b,'=',add2(a,b))

#
def tupleMax(t):
       if t[0]>=t[1] and t[0]>=t[2] :
           return t[0]
       elif t[1]>=t[0] and t[1]>=t[2] :
           return t[1]
       else:
           return t[2]
    
a=float(input('실수 입력:'))
b=float(input('실수 입력:'))
c=float(input('실수 입력:'))
tupleMax(a,b,c)

#
def inputNumber():
    num=float(input('실수 입력:'))
    return num

a=inputNumber()
print(a)
def getName():
	name=input('이름:')
	return name
    
def getNam(name):
	name=input('이름:')
	return name



###재귀함수

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

a=int(input('정수입력:'))
print(a,'! = ',factorial(a))


def sumRecursive(n,m):
    if n==m:
        return m
    else :
        return n+sumRecursive(n+1,m)

a=int(input('정수입력:'))
b=int(input('정수입력:'))
print(a,'부터',b,'까지의 합',sumRecursive(a,b))

#기본값 넣기(기본값은 무조건 뒤쪽으로 배치)
def greetName(name,age=21,schoolnum=14):
    print(name,'의 나이는',age,'세이고, 학번은',schoolnum, '이다.')

#키워드로 넣을 경우
greetName(age=25, name='황인규',schoolnum=14)

#12.(p.134)
a=int(input('정수입력:'))
b=int(input('정수입력:'))
result=0

def mul(a,b):
    result=a*b
    print(a,'*',b,'=',result)

def di(a,b):
    result=a/b
    print(a,'/',b,'=',result)
mul(a,b)
di(a,b)

#13.(p.134)
name=""
def getName():
    name=input("이름 입력:")
    return name

name=getName()
print('your name?',name)

"""
##가변인자(가변인자는 기본값처럼 뒤쪽에 배치)

def greet(*name):
    print('How are you?', end='')
    for n in name:
        print(n,end='')
    print('\n',name)

def greetN(cnt, *name):
    while cnt > 0:
        print('Hi',name[cnt-1])
        cnt-=1
    
