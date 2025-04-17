month=int(input())
if month>=3 and month<=5:
    print('봄입니다.')
elif month>=6 and month<=8:
    print('여름입니다.')
elif month>=9 and month<=11:
    print('가을입니다.')
elif month==12 or month==1 or month==2:
    print('겨울입니다.')