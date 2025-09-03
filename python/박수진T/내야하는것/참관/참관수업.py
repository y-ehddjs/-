# a=[i**2 for i in range(1,21) if i%2==0]
# print(a)

# words = ["apple", "orange", "banana", "grape", "umbrella", "kiwi", "avocado", "egg"]
# rwords = [i for i in words if i[0] in 'aeiou' and len(i) >= 5]
# print(rwords)

# a=[i*j for i in range(1,6) for j in range(1,6)]
# print(a)

# print('입력',end='')
# a=input().split()
# b=input()
# sum=a.count(b)
# print(b,"은(는) 리스트에",sum,"번 등장합니다")

# a = input().split()
# a.sort()
# print("오름차순:", a)
# a.sort(reverse=True)
# print("내림차순:", a)

while True:
    a = input().split()
    if '0' in a:
        break
    a = list(map(int, a))
    if 3 in a:
        a.remove(3)
    print(a)

# all_numbers = []
# while True:
#     line = input().split()
#     if '0' in line:
#         break
#     nums = list(map(int, line))
#     all_numbers.extend(nums)


# all_numbers = [x for x in all_numbers if x != 3]

# print(all_numbers)