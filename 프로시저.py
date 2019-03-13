#인자 없는 프로시저
def greet():
    print('How are you?')

def star():
    print('**********')


#인자 있는 프로시저

def greetName(name):
    print('How ar you?',name)

name=input('이름 입력:')
greetName(name)


def starNum(count):
    n=0
    while n<count:
        print('*',end='')
        n+=1

num=int(input('별의 갯수:'))
starNum(num)

print()

def square(n):
    print(n,'의 제곱은 ',n*n)

num=float(input('실수 입력:'))
square(num)
