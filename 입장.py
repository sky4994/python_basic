age= int(input('나이를 입력하시오 :'))

if age>= 8 :
    height=float(input('키를 입력하시오 :'))
    if height>=120:
        print('입장가능합니다.')
    else:
        print('키가 120cm이하면 입장이 불가능 합니다.')
else:
    print('나이가 7살이하면 입장이 불가능 합니다.')
