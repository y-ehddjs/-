# for i in range(1,101,2):
#     print(i)

# dan = int(input("원하는 단은:"))
# for i in range(1,10):
#     print(f'{dan} * {i} = {dan*i}')

# sum=0
# for i in range(1,101):
#     sum+=i
# print(sum)

# n=input()
# sum=0
# for i in n:
#     if i=='a':
#         sum+=1
# print(sum)

# n=int(input())
# for i in range(0, n+1):
#     print(i,end=" ")

# n=int(input())
# for i in range(1,n+1):
#     print('*',end="")

# array= [273, 74, 103, 57, 52]
# for i in range(0,len(array)):
#     print(i , end=" ")
#     print( array[i])

# import turtle as t
# for count in range(1,7):
#     t.circle(100)
#     t.rt(60)

# import turtle as t
# for i in range(1,5):
#     t.forward(100)
#     t.lt(90)

# import turtle as t
# n=int(input("정수입력>"))
# for i in range(1,n+1):
#     t.forward(100)
#     t.lt(360/n)

# import turtle as t
# for i in range(1,6):
#     t.fd(100)
#     t.rt(144)

# n=int(input('정수입력>'))
# sum=1
# for i in range(1,n+1):
#     sum*=i
# print(f'{5}!은 {sum}')

# sum=0
# for i in range(1,101):
#     sum = sum + i
#     if sum>1000:
#         sum=i
#         break
# print(f'1~100의 합에서 최초로 1000이 넘는 위치 : {sum}')

# sum = 0
# for i in range(1,101):
#     if i%3==0:
#         continue
#     sum+=i
# print('1~100의 합(3의배수제외):',sum)

# mult = 1
# for a in range(1, 100):
#     if a%2==0:
#         continue
#     print(f'{mult} * {a} = {mult*a}')
#     mult = mult * a
#     if mult>=100:
#         break