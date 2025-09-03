# def sum_n(n):
#     sum=0
#     for i in range(n+1):
#         sum+=i
#     return sum
# n=int(input())
# print(sum_n(n))

# def sum_n(n):
#     n=n*(n+1)/2
#     return int(n)
# n=int(input())
# print(sum_n(n))

# def find_Max(a):
#     sum=a[0]
#     for i in range(1,len(a)):
#         if sum < a[i]:
#             sum = a[i]
#     return sum

# a=[17,92,18,33,58,7,33,42]
# print((find_Max(a)))

# def find_Max_idx(a):
#     sum=0
#     for i in range(1,len(a)):
#         if a[sum] < a[i]:
#             sum = i
#     return sum
# a=[17,92,18,33,58,7,33,42]
# print(find_Max_idx(a))

# def find_same_name(a):
#     sum=0
#     result=set()
#     for i in range(len(a)):
#         for j in range(i+1,len(a)):
#             if a[i] == a[j]:
#                 result.add(a[j])
#     return result    
# name = ["Tom", "Jerry", "Mike", "Tom"]
# print(find_same_name(name))
# name2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
# print(find_same_name(name2))

# def fact(n):
#     sum=1
#     for i in range(1,n+1):
#         sum*=i
#     return sum
# a=int(input())
# print(fact(a))

# def fact(n):
#     if n <= 1 :
#         return 1    
#     return n * fact(n-1)
# a=int(input())
# print(fact(a))

# def gcd(a,b):
#     i=min(a,b)
#     while True:
#         if i==1:
#             return i
#         elif a%i==0 and b%i==0:            
#             return i
#         else:
#             i-=1
# print(gcd(99,27))

# def gcd(a,b):
#     if b==0:
#         return a
#     return gcd(b,a%b)
# print(gcd(99,27))

# def hanoi(n,from_pos,to_pos,aux_pos):
#     if n==1:
#         print(from_pos,"->",to_pos)
#         return
#     hanoi(n-1,from_pos,aux_pos,to_pos)
#     print(from_pos,"->",to_pos)
#     hanoi(n-1,aux_pos,to_pos,from_pos)
# print("n=3")
# hanoi(3,1,3,2)

# def search_list(a,x):   #반복문 한번만 도니깐 시간 복잡도 O(n)
#     for i in range(1,len(a)):
#         if a[i]==x:
#             return i
#     return -1
# v = [17, 92, 18, 33, 58, 7, 33, 42]
# print(search_list(v, 18))   # 2(순서상 세 번째지만, 위치 번호는 2)
# print(search_list(v, 33))   # 3(33은 리스트에 두 번 나오지만 처음 나온 위치만 출력)
# print(search_list(v, 900))  # -1(900은 리스트에 없음)

# def find_min_idx(a):
#     min_idx=0
#     for i in range(1,len(a)):
#         if a[i] < a[min_idx]:
#             min_idx=i
#     return min_idx
# def sel_sort(a):
#     result=[]
#     while a:
#         min_idx=find_min_idx(a)
#         value=a.pop(min_idx)
#         result.append(value)
#     return result
# d = [2, 4, 5, 1, 3]
# print(sel_sort(d))

# def sel_sort(a):
#     for i in range(0,len(a)-1): #보통 이중 포문이면 O(n²)이다
#         min_idx=i
#         for j in range(i+1,len(a)):
#             if a[j] < a[min_idx]:
#                 min_idx = j
#         a[i], a[min_idx] = a[min_idx], a[i]
# d = [2, 4, 5, 1, 3]
# sel_sort(d)
# print(d)

# def find_ins_idx(r,v):
#     for i in range(0, len(r)):
#         if v <r[i]:
#             return i
#     return len(r)
# def ins_sort(a): #와일문안에서 함수호출을 했는데 그 함수에서 반복문이 돌아가서 O(n²)
#     result=[]
#     while a:
#         value=a.pop(0)
#         ins_idx=find_ins_idx(result, value)
#         result.insert(ins_idx, value)
#     return result
# d = [2, 4, 5, 1, 3]
# print(ins_sort(d)) 

# def ins_sort(a):
#     for i in range(1,len(a)):
#         key=a[i]
#         j=i-1
#         while j >= 0 and a[j] > key:
#             a[j + 1] = a[j]
#             j-=1
#             a[j+1]=key
# d = [2, 4, 5, 1, 3]
# ins_sort(d)
# print(d)

# def merge_sort(a):
#     if len(a) <= 1:
#         return a
#     mid= len(a)//2
#     left=merge_sort(a[:mid])
#     right=merge_sort(a[mid:])
#     result = []
#     while left and right:
#         if left[0] < right[0]:
#             result.append(left.pop(0))
#         else:
#             result.append(right.pop(0))
#     while left:
#         result.append(left.pop(0))
#     while right:
#         result.append(right.pop(0))
#     return result
# d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
# print(merge_sort(d))

# def merge_sort(a):
#     if len(a) <= 1:
#         return
#     mid=len(a)//2
#     left=a[:mid]
#     right=a[mid:]
#     merge_sort(left)
#     merge_sort(right)
#     i=0
#     j=0
#     k=0
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             a[k]=left[i]
#             i+=1
#             k+=1
#         else:
#             a[k]=right[j]
#             j+=1
#             k+=1
#     while i <len(left):
#         a[k]=left[i]
#         i+=1
#         k+=1
#     while j <len(right):
#         a[k]=right[j]
#         j+=1
#         k+=1
# d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
# merge_sort(d)
# print(d)

# def quick_sort(a):
#     if len(a) <= 1:
#         return a
#     pivot=a[-1]
#     big=[]
#     small=[]
#     for i in range(0,len(a)-1):
#         if a[i] < pivot:
#             small.append(a[i])
#         else:
#             big.append(a[i])
#     return quick_sort(small)+[pivot]+quick_sort(big)
# d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
# print(quick_sort(d))

# def quick_sort_sub(a,start,end):
#     if end-start <= 0:
#         return
#     pivot=a[end]
#     i=start
#     for j in range(start,end):
#         if a[j] <= pivot:
#             a[i],a[j]=a[j],a[i]
#             i+=1
#     a[i], a[end] = a[end], a[i]
#     quick_sort_sub(a, start, i - 1)
#     quick_sort_sub(a, i + 1, end) 
# def quick_sort(a):
#     quick_sort_sub(a, 0, len(a) - 1)
# d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
# quick_sort(d)
# print(d)

# def binary_search(a,x):
#     start = 0
#     end= len(a)-1
#     while start <= end:
#         mid=(start+end)//2
#         if x==a[mid]:
#             return mid
#         elif x<a[mid]:
#             end = mid-1
#         else:
#             start = mid+1
#     return -1
# d = [1, 4, 9, 16, 25, 36, 49, 64, 81]
# print(binary_search(d,36))
# print(binary_search(d,50))

# def palindrome(s):
#     qu=[]
#     st=[]
#     for i in s:
#         if i.isalpha():
#             qu.append(i.lower())
#             st.append(i.lower())
#     while qu:
#         if qu.pop(0) != st.pop():
#             return False
#     return True
# print(palindrome("Wow"))
# print(palindrome("Madam, I’m Adam."))
# print(palindrome("Madam, I am Adam."))

# def find_same_name(s):
#     name_dict = {}
#     result = set()
#     for i in s:
#         if i in name_dict:
#             name_dict[i]+=1
#         else:
#             name_dict[i]=1
#         if name_dict[i]>=2:
#             result.add(i)
#     return result
# name = ["Tom", "Jerry", "Mike", "Tom"]
# print(find_same_name(name))
# name2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
# print(find_same_name(name2))

# def sum_ep(n):
#     sum=0 #합이니깐 0해도 상관 없음
#     for i in range(1,n+1): #1부터 n까지 다 돌려면 n+1해야됨
#         sum+=i**2
#     return sum
# n=int(input())
# print(sum_ep(n))

# def sum_eq(n):
#     sum=n*(n+1)*(2*n+1)/6 #나누니깐 실수형으로 바뀌는거 주의,나누기 주의
#     return int(sum) #그래서 반환할때 정수형으로 바꿔서 소수점 날리기
# n=int(input())
# print(sum_eq(n))

# def find_min(n):
#     sum=n[0]
#     for i in range(len(n)):
#         if sum<n[i]:
#             sum=n[i]
#     return sum
# n = [17, 92, 18, 33, 58, 7, 33, 42]
# print(find_min(n))

# def print_pairs(a):
#     for i in range(len(a)):
#         for j in range(i+1,len(a)): #중복 때문에 i+1부터 시작해야됨 안하면 Tom - Tom 나옴
#             print(a[i],"-",a[j])
# name = ["Tom", "Jerry", "Mike"]
# print_pairs(name)
# print()
# name2 = ["Tom", "Jerry", "Mike", "John"]
# print_pairs(name2)

# def sum_n(n):
#     if n<=1:
#         return 1
#     return n+sum_n(n-1)
# n=int(input())
# print(sum_n(n))

# def find_max(a,n):
#     if n==1:
#         return a[0]
#     max_n=find_max(a,n-1)
#     if max_n > a[n-1]:
#         return max_n
#     else:
#         return a[n-1]
# v = [17, 92, 18, 33, 58, 7, 33, 42]
# print(find_max(v, len(v)))  # 함수에 리스트의 자료 갯수를 인자로 추가하여 호출

# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n-2)+fibonacci(n-1)
# print(fibonacci(7))

# def bubble_sort(a):
#     while True:
#         changed = False
#         for i in range(0, len(a) - 1):
#             if a[i] > a[i + 1]:
#                 print(a)
#                 a[i], a[i + 1] = a[i + 1], a[i]
#                 changed = True
#         if changed == False:
#             break  # 모두 정렬됐으면 반복 종료
# d = [2, 4, 5, 1, 3]
# bubble_sort(d)
# print(d)

# def print_all_friends(g,start):
#     qu=[]
#     done=set()
#     qu.append(start)
#     done.add(start)
#     while qu:
#         pig=qu.pop(0)
#         print(pig)
#         for i in g[pig]:
#             if not i in done:
#                 qu.append(i)
#                 done.add(i)
# fr_info = {
#     'Summer': ['John', 'Justin', 'Mike'],
#     'John': ['Summer', 'Justin'],
#     'Justin': ['John', 'Summer', 'Mike', 'May'],
#     'Mike': ['Summer', 'Justin'],
#     'May': ['Justin', 'Kim'],
#     'Kim': ['May'],
#     'Tom': ['Jerry'],
#     'Jerry': ['Tom']
# }
# print_all_friends(fr_info, 'Summer')
# print()
# print_all_friends(fr_info, 'Jerry')
