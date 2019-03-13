
#hwang in gyu
#Define the message
msg="Hi"
print(msg)

#자료를 입력하면 무조건 문자열로 입력됨. 그래서 int로 정수로 바꿔주는 것
cost1 = int(input('1분기 지출 금액 : '))
cost2 = int(input('2분기 지출 금액 : '))

sum = 0
#Insert the code here to add the numbers
sum = cost1 + cost2
mean = (cost1+cost2)/2

#총액 출력
print("총액은", sum, "평균지출액은",mean)


#floatPI를 정의하고 초기화한다.
floatPI = float(3.14)

#floatPI를 출력한다.
print(floatPI)


myAge=1
#assign value to myAge
myAge=21

#print myAge
print(myAge)


a=50;b=2
print(a,'+',b,end='',sep=',')
print('=',a+b)
