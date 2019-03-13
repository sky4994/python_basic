print('어서오십시오! 우선 출입료를 계산해주십시오.')
age=int(input('나이를 입력하세요 :'))

if age>=65:
    print('무료')
elif age>=20:
    print('20,000원')
elif age>=13:
    print('10,000원')
elif age>=1:
    print('5,000원')

print('즐거운 시간 되시길 바랍니다.')
