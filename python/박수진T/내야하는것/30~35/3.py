import random as r

print('동전 던지기 게임을 시작합니다.')

a=r.randint(0,1)

sum=int(input('앞면(0)/뒷면(1)을 입력해 주세요.'))

if a==sum:
    print("맞았습니다.")
else:
    print('틀렸습니다.')

if a==0:
    print('앞면입니다.')

else:
    print('뒷면입니다.')

print('게임이 종료되었습니다.')