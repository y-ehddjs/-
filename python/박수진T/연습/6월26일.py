# while True:
#     n=int(input())
#     if 100>=n>=80:
#         print("합격입니다.")
#         break
#     elif 80>=n>=0:
#         print("불합격입니다.")
#         break
#     else:
#         print("에러 다시 입력하세요")

# planet= [["수성",2440,0.055],
#          ["금성",6052,0.815],
#          ["지구",6378,1.0]]
# name=input("조회할 행성이름>")
# for i in range(0,3):
#     if name in planet[i]:
#         k=i
# print("===================")
# print("이름:",planet[k][0])
# print("크기:",planet[k][1])
# print("질량:",planet[k][2])

s=[i**2 for i in range(1,100) if i%3==0 and i%5==0]
print(s)

