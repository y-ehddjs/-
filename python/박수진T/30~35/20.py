a=int(input('직선1의 길이>'))
b=int(input('직선2의 길이>'))
c=int(input('직선3의 길이>'))
max=0
min=0
if a>=b and a>=c:
    max=a
    min=b+c
if b>=a and b>=c:
    max=b
    min=a+c
if c>=a and c>=b:
    max=c
    min=a+b
if max<min:
    print('삼각형 가능')
else:
    print('삼각형 불가능')