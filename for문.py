for name in 'korea' :
    print(name)


for name in [1,2,3,4,5,7] :
    print(name)
    
names= 'AliCe'
for x in names:
    print(x.upper())

for x in ['red', 'blue', 'white']:
    print(x,end=' ')

print(end='\n')

number = [4,10,9,-5,5,1,8,2,-2]
total=0
for n in number:
    if n%2 == 0:
        total += n
    print('total:',total, end='\n')

#for문과 같이 잘쓰이는 range 함수. range(시작,끝+1,간격) ex)range(1,5,2)=1,3

for a in range(5):
    print(a,end=' ')

print()

#repeat함수를 쓸때는 import itertools을 하고
#itertools.repeat(반복할 숫자, 반복횟수)로 사용한다.

x=[1,2,3,4,5]
for i in x:
    print(i, end=' ')

print()
fruit = ['apple','cherry', 'banana']
for item in fruit:
    print(item)

L=range(1,16,2)
for n in L :
    print(n,end=' ')

print()

for n in range(3) :
    for k in range(10):
        print('*',end=' ')
    print('&')
