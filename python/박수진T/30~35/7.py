m=int(input('연소득 입력>'))
y=int(input('재직기간 입력>'))

if m>=40000000 and y>=2:
    print('대출자격 있음')
if m<40000000:
    print('연봉 4000만원 이상 필요')
if y<2:
    print('재직기간 2년 이상 필요')