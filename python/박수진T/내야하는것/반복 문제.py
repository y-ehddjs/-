# weight = 70
# while weight>60:
#     print("운동하자")
#     weight-=1
# print("목표달성!")

# 공사중 = '예'
# while 공사중 == '예':
#     print('공사중')
#     공사중=input("공사중입니까(예/아니오)")
# print("공사가 끝났네")

# a=0
# while a<5:
#     print("안녕하세요")
#     a+=1

# n= int(input('n:'))
# while n>0:
#     print("실행")
#     n-=1

# n=int(input())

# while n>=0:
#     print(n)
#     n-=1

# n=100
# while n==100:
#     if sum=='y':
#         break
#     sum=input("y입력시 종료>")
#     print(sum)

# sum=0
# a=1
# n=int(input())
# while a <= n:
#     sum = sum + a
#     a = a + 1
# print(sum)

# a=1
# while a<=100 :
#     if a%3==0:
#         print("짝",end=" ")
#     else:
#         print(a,end=" ")
#     a+=1

# alist = [1,2,1,2]

# while 2 in alist:
#     alist.remove(2)

# print(alist)

# bts = ['정국', '뷔', '지민', '슈가', '진', 'RM', '제이홉']
# i = 0
# while i < len(bts):
#     print(bts[i])
#     i += 1

# dan = int(input("원하는 단은: "))
# i = 1
# while i <= 9:
#     print(f"{dan} x {i} = {dan * i}")
#     i += 1

# import random
# com = random.randint(1, 100) 
# player = 0 
# while player != com:
#     player = int(input("1부터 100 사이의 숫자를 맞춰봐: "))
#     if player < com:
#         print("UP")
#     elif player > com:
#         print("DONW")
#     else:
#         print("정답!")

# import random
# import time

# wlist = ['cat', 'dog', 'fog', 'monkey', 'mouse', 'panda', 'frog', 'snake', 'wolf']

# print("[타자게임] 준비되면 엔터!")
# input()
# start = time.time()  

# n = 1  
# while n <= 5:
#     com = random.choice(wlist) 
#     print(f"\n문제 {n}: {com}")
#     player = input(">>> ")

#     if player == com:
#         print("통과!")
#         n += 1
#     else:
#         print("오타! 다시도전")

# end = time.time()
# elapsed = round(end - start, 2)

# print("\n게임 종료!")
# print(f"타자 시간: {elapsed}초")