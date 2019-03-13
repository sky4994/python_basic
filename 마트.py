money=float(input('구입 총액은?:'))

if money >= 90000:
    money= money*0.95
else:
    moeny= money*0.98
print('금액:',money)
