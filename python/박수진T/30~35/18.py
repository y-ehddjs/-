a = input("윷의 결과를 입력해주세요>")
count = 0
n = "1"
if n==a[1]:count+=1
if n==a[0]:count+=1
if n==a[2]:count+=1
if n==a[3]:count+=1

if count==1:print("도")
elif count==2:print("개")
elif count==3:print("걸")
elif count==4:print("윷")
else:print("모")