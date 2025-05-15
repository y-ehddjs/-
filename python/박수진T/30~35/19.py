import random as r
a=r.randint(0,99)
sum=int(input("복권번호를 입력하시오(0~99)"))
if sum==a:
    print(f"당첨번호는{a}입니다.")
    print("상금 100만원!")
elif sum//10==a//10 or sum%10==a%10:
    print(f"당첨번호는{a}입니다.")
    print("상금 50만원!")
else:
    print(f"당첨번호는{a}입니다.")
    print("상금이 없습니다")