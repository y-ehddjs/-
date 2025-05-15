id="이재준개돼지"
ad="admin"
pawd= 1234

idw=input('아이디를 입력하시오:')
pawdw=int(input('비밀번호를 입력하시오:'))
if id==idw and pawd==pawdw:
    print('환영합니다.')
elif ad==idw:print("관리자가 로그인하였습니다.")
elif id!=idw and pawd!=pawdw:print("아이디와 비밀번호가 일치하지 않습니다.")
elif id!=idw and pawd==pawdw:print("아이디를 찾을 수 없습니다.")
