##review~~

#1.자동차 속도가 110킬로미터를 초과한 경우, '과속', 그렇지않으면 '속도OK'를 출력하라
#(단, 속도는 mySpeed변수에 입력받는다.)

mySpeed=float(input('자동차 속도를 입력 : '))

if mySpeed > 110 :
    print('과속')
else:
    print('속도OK')

#2.for문을 활용하여 별 5개를 출력하라 (counter변수 사용)

for counter in range(5):
    print('*',end='')

#3.while를 사용하여 별 5개씩 3줄을 출력하라

print()

i=0
while i<3:
    j=0
    while j<5:
        print('*',end='')
        j+=1
    print('')
    i+=1
