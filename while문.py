count=1

while count<=5:
    print('hello')
    count+=1


####
n=int(input('Enter n:'))

a=2
even_sum=0

while a <= n:
    even_sum +=a
    a+=2
print('1부터 {}까지의 짝수의 합: {}'.format(n,even_sum))

a=2
even_sum=1

while a <= n:
    even_sum *=a
    a+=2
print('1부터 {}까지의 짝수의 곱: {}'.format(n,even_sum))


#######
st="Korea"
i=0
while i<len(st) :
    print(st[i])
    i+=1


i=1
while i<9:
    if i%2==0 :
        print(i,end=' ')
    i+=1

print()

fruit = ['apple', 'cherry', 'banana']
i=0
while i < len(fruit):
    print(fruit[i])
    i+=1
    
i=0
while i<3:
    j=0
    while j<10:
        print('*',end='')
        j+=1
    i+=1
    print()


summ=0
i=0
while i<=100:
    summ+=i
    i+=1
print(summ)


######continue, break

for i in range(10):
    if i % 2==0:
        continue
    print(i,end=' ')

print()

for j in range(1,20):
    if j % 5 == 0:
        break
    print(j)

###구구단~

den=1
while den<10:
    i=1
    while i<10:
        print(den,'*',i,'=',den*i)
        i+=1
    print(den)
    den+=1

for dan in range(2,10):
    print(dan,'단')
    for i in range(10):
        print(dan,'*',i,'=',dan*i)
    print()
