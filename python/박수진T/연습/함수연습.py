# def sum(a,b):
#     return a + b
# print(sum(10,5))

# def avg(m, s, i):
#     average = (m+s+i) / 3
#     return average
# mat=int(input("수학 점수 입력:"))
# sci=int(input("과학 점수 입력:"))
# info=int(input("정보 점수 입력:"))
# result = avg(mat,sci,info)
# print("평균:",result)

def greatest(data):
    greater = data[0]
    for i in range(1, len(data)):
        if greater < data[i]:
            greater = data[i]
    return greater

nums = [75,80,50,85,100,95,90,65,80,70]
result = greatest(nums)
print(result)