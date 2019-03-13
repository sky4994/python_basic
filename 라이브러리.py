import math

r=float(input('반지름 입력:'))
area=math.pi*pow(r,2)
print('반지름',r,'원 면적',area)

import random
r=random.randint(1,9)
rr=random.randrange(1,10,1)
print(r,rr)

import time
t=time.localtime()

st=time.strftime('%H:%M:%S')
print(st)
