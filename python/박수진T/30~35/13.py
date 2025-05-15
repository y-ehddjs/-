y=int(input("연도를 입력해 주세요"))
if y%400==0 or y%100%4==0:
    print(f"{y}은 윤년입니다.")
else:
    print(f'{y}은 윤년이 아닙니다.')