# # 1번 문제 학생수 입력받고 출석일 합계구하기
# n=int(input())          
# daylist=[]             
# for i in range(n):        
#     att=input().split()
#     daylist.append(att)
# count=0
# for i in daylist:
#     count+=i.count('1')   
# print(count)

# # 2번 문제 주민등록 번호 정보출력
# n=input("주민등록번호 입력>")
# if n[7]=="1":print("19"+n[0:2]+"년 태어난 남자입니다.")
# elif n[7]=="2":print("19"+n[0:2]+"년 태어난 여자입니다.")
# elif n[7]=="3":print("20"+n[0:2]+"년 태어난 남자입니다.")
# elif n[7]=="4":print("20"+n[0:2]+"년 태어난 여자입니다.")

# num1=int(input())
# num2=int(input())
# T=(num2%100)
# A=T%10
# B=(T-A)//10
# C=(num2-T)//100
# print(num1*A)
# print(num1*B)
# print(num1*C)
# print(num1*num2)

# s=int(input())
# n=[]
# for i in range(s):
#     a=int(input())
#     n.append(a)
# for i in range(s+1):
#     c=n[i]
#     for j in range(s)

# def fact(n):
#     if n<=1:
#         return 1
#     return n * fact(n-1)
# a,b=map(int, input().split())
# print(fact(a)//(fact(a-b)*fact(b)))

# a,b=map(int, input().split())
# for i in range(1,a+1):
#     for j in range(b+1):


# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print("\n")