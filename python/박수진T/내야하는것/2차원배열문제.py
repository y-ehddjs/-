# score = [80,90,75,25,50]
# for i in score:
#     print(i)

# score = [80,90,75,25,50]
# for i in range(5):
#     print(score[i])

# score = [80,90,75,25,50]
# for i in range(0,len(score)):
#     print(score[i])

# email = input().split("@")
# print(email[0])

# food = input().split( )
# for i in food:
#     print(i)

# score = input().split()
# total = 0
# score[0] = int(score[0])
# score[1] = int(score[1])
# score[2] = int(score[2])
# total = score[0] + score[1] + score[2]
# avg = total / 3
# print(f"{avg:.2f}")

# num = list(map(int, input().split()))
# count = 0
# for n in num:
#     if n % 2 == 0:
#         count += 1
# print(count)

# Scores = [
#     [92, 80, 87],   
#     [94, 82, 86],   
#     [74, 65, 69],   
#     [87, 89, 81]    
# ]
# Scores = [[92, 80, 87], [94, 82, 86], [74, 65, 69], [87, 89, 81]]
# m_total = 0
# for row in Scores:
#     m_total = m_total + row[0]
# print(m_total)

# Scores = [[92, 80, 87], [94, 82, 86], [74, 65, 69], [87, 89, 81]]
# m_total = 0
# for row in Scores:
#     m_total = m_total + row[0]
# avg = m_total / 4
# print(avg)

# Scores = [[92, 80, 87], [94, 82, 86], [74, 65, 69], [87, 89, 81]]
# for row in Scores:
#     s_total = 0
#     for col in row:
#         s_total = s_total + col
#     print(s_total)

# Scores = [[92, 80, 87], [94, 82, 86], [74, 65, 69], [87, 89, 81]]
# for row in Scores:
#     s_total = 0
#     for col in row:
#         s_total = s_total + col
#     print(round(s_total / 3, 2))

# Scores = [['김정호', 92, 80, 87], ['박문수', 94, 82, 86], ['이사부', 74, 65, 69], ['장영실', 87, 89, 81]]
# for row in Scores:
#     s_total = row[1] + row[2] + row[3]
#     print(row[0], round(s_total / 3, 2))

# medal = [[6, 4, 10], [38, 32, 19], [26, 14, 17]]
# g_total = 0
# s_total = 0
# b_total = 0
# for row in medal:
#     g_total += row[0]
#     s_total += row[1]
#     b_total += row[2]
# print("금:", g_total)
# print("은:", s_total)
# print("동:", b_total)

# medal = [['대한민국', 6, 4, 10], ['중국', 38, 32, 19], ['일본', 26, 14, 17]]
# for row in medal:
#     name = row[0]
#     total = row[1] + row[2] + row[3]
#     print(name, total)

# daylist = [[0, 1, 0, 0, 1, 0, 0], 
#            [0, 0, 1, 0, 1, 0, 0], 
#            [0, 1, 0, 1, 0, 0, 0], 
#            [0, 0, 0, 1, 0, 0, 0]]
# count = 0
# for row in daylist:
#     for d in row:
#         if d == 0:
#             count += 1

# print(count)

# daylist = [[1, 0, 1, 0, 1, 0, 0], 
#            [0, 0, 1, 0, 0, 1, 0], 
#            [0, 1, 0, 0, 0, 0, 0]]

# count = 0
# for row in daylist:
#     if row[1] == 0:
#         count += 1

# print(count)

# n = int(input())
# daylist = []
# for i in range(n):
#     att = list(map(int, input().split()))
#     daylist.append(att)
# count = 0
# for row in daylist:
#     for d in row:
#         if d == 0:
#             count += 1
# print(count)
