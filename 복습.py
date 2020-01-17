텍스트 파일 읽기

파일 핸들러 객체 = open("경로/이름", 모드) #r, w, b, a

#텍스트파일의 전체 내용을 문자열로, 파일핸들러객체.read()

["row 문자열\n"] = 파일핸들러 객체.readlines()

파일핸들러 객체.close()

자동으로 닫혀준다.

with open("경로/이름", 모드) as 별칭(파일 핸들러) :



메모리에 생성된 파이썬 객체를 저장 : Serialize, Marshalling


-> pickle 모듈의 dump()함수

파일 등에 저장된 파이썬 객체를 읽어 와서 메모리에 생성 - load() 함수


csv파일 형식 읽기

csv모듈의 reader(), writerow()



DB의 세션 정보객체 cx_Oracle 모듈.connect(user명, password, url정보)

Cursor 객체 생성

cursor 객체 = execute("sql 문장")
