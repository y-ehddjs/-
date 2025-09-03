# sumid=input()
# sumpwd=input()
# id="admin"
# pwd=1234

# special_chars = ['#', '!', '"', '\\', '(', ')']

# if any(char in sumid for char in special_chars):
#     print("특수문자 ㄲㅈㄹ")
# elif sumid == id and sumpwd == pwd:
#     print("환영합니다")
# elif sumid == id and sumpwd != pwd:
#     print("비번틀림 ㅅㄱ")
# elif sumid != id and sumpwd == pwd:
#     print("아이디틀림 ㅅㄱ")
# else:
#     print("다틀림 ㅅㄱ")

# age = int(input("현재 나이를 입력하세요: "))
# target_year = int(input("가고 싶은 연도를 입력하세요: "))
# current_year = 2025  # 기준년도
# birth_year = current_year - age
# age_in_target_year = target_year - birth_year
# if age_in_target_year < 0:
#     print("그 해에는 아직 태어나지 않았어요!")
# else:
#     print(f"{target_year}년에는 {age_in_target_year}살입니다.")

# import random
# sides = int(input("주사위 눈의 수를 입력하세요: "))
# predict = input("합이 홀수인지 짝수인지 예측하세요 (홀/짝): ")
# dice1 = random.randint(1, sides)
# dice2 = random.randint(1, sides)
# total = dice1 + dice2
# print(f"첫 번째 주사위: {dice1}")
# print(f"두 번째 주사위: {dice2}")
# print(f"합: {total}")
# result = "홀" if total % 2 == 1 else "짝"
# if result == predict:
#     print("맞췄습니다!")
# else:
#     print("틀렸습니다!")

# jumin = input("주민등록번호를 입력하세요: ")
# print(jumin.count('2'))

# N = int(input())

# for i in range(1, N + 1):
#     if i % 2 == 1:
#         print(i)

# money = int(input())
# days = int(input())
# changes = list(map(int, input().split()))
# for change in changes:
#     money += money * (change / 100)
# start = int(input())
# if money > start:
#     print("인생역전")
# elif money < start:
#     print("인생역전실패")
# else:
#     print("본전을 출력한다.")

# base = int(input("배수를 찾아봐요~~ : "))
# for _ in range(10):
#     num = int(input("수를 입력하세요! : "))
#     if num % base == 0:
#         print(f"{base}의 배수입니당!")
#     else:
#         print(f"{base}의 배수가 아닙니다!")
# print("배수 찾기를 종료합니다")

# n = int(input())
# nums = []
# for _ in range(n):
#     nums.append(int(input()))
# max_num = max(nums)
# position = nums.index(max_num) + 1
# print(max_num)
# print(position)

# n = int(input())

# for _ in range(n):
#     print("*" * n)

# n = int(input())
# for i in range(1, n + 1):
#     s = str(i)
#     if '3' in s or '6' in s or '9' in s:
#         print("짝", end=" ")
#     else:
#         print(i, end=" ")

# def solve_money_game(transactions):
#     balances = {}
#     for transaction in transactions:
#         parts = transaction.split()
#         sender = parts[0]
#         receiver = parts[1]
#         amount = int(parts[2])

#         if sender not in balances:
#             balances[sender] = 10000
#         if receiver not in balances:
#             balances[receiver] = 10000
        
#         balances[sender] -= amount
#         balances[receiver] += amount
    
#     max_balance = -1
#     richest_person = ''
    
#     sorted_people = sorted(balances.keys())

#     for person in sorted_people:
#         if balances[person] > max_balance:
#             max_balance = balances[person]
#             richest_person = person
#     return f"{richest_person}가 {max_balance}원으로 돈이 가장 많다."
# n1 = 3
# transactions1 = [
#     "a b 5000",
#     "c a 3000",
#     "b a 4000"
# ]
# print(f"출력 1: {solve_money_game(transactions1)}")
# n2 = 5
# transactions2 = [
#     "a e 2000",
#     "d c 5000",
#     "b a 4000",
#     "e d 3000",
#     "c a 8000"
# ]
# print(f"출력 2: {solve_money_game(transactions2)}")

# def solve_password_game(numbers_str):
#     padded_numbers = [num.zfill(5) for num in numbers_str]
#     digit_1 = padded_numbers[0][4]
#     digit_2 = padded_numbers[1][3]
#     digit_3 = padded_numbers[2][2]
#     digit_4 = padded_numbers[3][1]
#     digit_5 = padded_numbers[4][0]
#     password = digit_5 + digit_4 + digit_3 + digit_2 + digit_1
#     return password
# numbers1 = [
#     "49802",
#     "10092",
#     "38402",
#     "09214",
#     "10002"
# ]
# print(f"출력 1: {solve_password_game(numbers1)}")
# numbers2 = [
#     "20941",
#     "12405",
#     "12094",
#     "09421",
#     "04921"
# ]
# print(f"출력 2: {solve_password_game(numbers2)}")
