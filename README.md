# 아시아경제 국비지원 교육 클라우드과정


#### 1일차 파이썬 환경설치 및 간단한 OT
[이재웅_파이썬 교육_ver2.pdf](https://github.com/schw240/-/files/4979913/_._ver2.pdf)

### 2일차 
오전
1.	메서드(Method)
2.	리스트(List)
3.	반복문(for)
4.	반복문(While)
5.	종합 프로그램 구현


오후
6.	인스턴스 변수와 클래스
7.	인스턴스 변수 멤버
8.	더 정교한 변수
9.	종합 프로그램 구현

### 3일차
오전
1.	HTML, CSS
2.	종합 프로그램 고도화(어제 파이썬 복습)


오후
3.	Selenium (웹 크롤링)

### 4일차
오전
1.	Xpath 구조
2.	크롤링 데이터 모델화


오후
3.	종합 프로그램

### 5일차

오전
1.	야후 파이낸스 크롤링

크롤링 시나리오
1. get >> https://finance.yahoo.com/quote/MSFT/history?p=MSFT
time.sleep(2)
2. 날짜 클릭
time.sleep(2)
3. MAX 클릭
time.sleep(2)
4. APPLY 클릭
time.sleep(2)
5. Download 클릭

오후
1.	종합 프로그래밍 고도화

### 6일차

오전
1.	데이터베이스 MSSQL
데이터베이스 - 새 데이터베이스 만들기
우리가 선택한 주제를 가지고 이름 정하기 ex 금융


오후
1.	종합 프로그래밍 고도화



### 7일차

오전
1.	데이터베이스 MSSQL를 이용하여 네이버 영화 랭킹 페이지 크롤링하여 데이터 담기

1)	네이버 영화 페이지를 크롤링하여 그 정보를 movie_list에 담음
2)	데이터베이스에 해당 정보를 저장(중복도 제거)
3)	데이터베이스를 조회하여 영화 정보를 가지고옴(더 이상 인터넷에서 X)
4)	각 영화의 url을 가지고 배우 정보를 크롤링
5)	배우 정보를 데이터베이스에 저장

오후
1.	종합 프로그래밍 고도화

### 8일차

오전
1.	어제 했던 것 복습 똑같은 것 다시 만들어보기


1)	영화 테이블 생성 <PRIMARY KEY 필수>
2)	스텝 테이블 생성 <PRIMARY KEY 필수>
3)	캐스팅 테이블 생성 <영화 CODE< 스텝 CODE 필수>
4)	C:/python/navermovie02
5)	각 테이블에 대한 모델(클래스)설계
6)	어댑터 역할 .py 각각 생성(ex: adp_movie.py)
7)	어댑터에서 pymssql과 db정보 (ip, id, pw , db)준비
8)	리스트 <class>를 반환(return)하는 각각의 조회(SELECT) 메서드 구현
	Conn = 접속정보
	Cursor = conn.cursor()
	Cursor.execute(쿼리)
	Row = cursor.fetchone() 결과 가장 사위 데이터 꺼내기
	While fetchone() 반복
9)	Main.py 생성 및 while 문 명령 추가
	‘1’, ‘2’, ‘3’, 각각 조회해서 출력하는 기능
	(데이터베이스 안에서 임시로 데이터 직접 추가해서 확인
	출력할때 클래스 안에 포함된 메서드를 사용(예:show)
10)	영화 , 스텝 코드 중복 체크 메서드 (반환 True/False)
11)	Insert 메서드 구현
	Main.py에 명령어 추가
	어댑터py에 메서드 구현
	Insert 호출 전에 중복 체크
12)	Crawling_movie.py 생성 및 영화 크롤링 기능 구현
	영화 정보 insert(중복체크 후)
	Main.py에서 호출되도록 명령 추가
13)	Crawling_casting.py생성 및 데이터 등록
	영화 목록(DB에 있는 데이터)를 기반으로 영화배우 크롤링 시작
	STAFF 중복 체크 및 INSERT
	CASTING 중복 체크 및 INSERT
	(스태프 및 캐스팅 정보의 중복유무를 한번에 체크하기 위한 아이디어 고민! 공통인 staff_code를 통해서 검사)
14)	영화테이블에서 CASTING_COUNT 컬럼 추가
	CASTING_COUNT(INT) 추가 (배우 전체 수)
15)	영화 목록 html 저장
16)	영화 목록 클릭 시 상세화면 html저장


### 9일차

오전
1.	7일차에 했던 것 이어서 계속 진행(현재 12단계 완료)


1)	영화 테이블 생성 <PRIMARY KEY 필수>
2)	스텝 테이블 생성 <PRIMARY KEY 필수>
3)	캐스팅 테이블 생성 <영화 CODE< 스텝 CODE 필수>
4)	C:/python/navermovie02
5)	각 테이블에 대한 모델(클래스)설계
6)	어댑터 역할 .py 각각 생성(ex: adp_movie.py)
7)	어댑터에서 pymssql과 db정보 (ip, id, pw , db)준비
8)	리스트 <class>를 반환(return)하는 각각의 조회(SELECT) 메서드 구현
	Conn = 접속정보
	Cursor = conn.cursor()
	Cursor.execute(쿼리)
	Row = cursor.fetchone() 결과 가장 사위 데이터 꺼내기
	While fetchone() 반복
9)	Main.py 생성 및 while 문 명령 추가
	‘1’, ‘2’, ‘3’, 각각 조회해서 출력하는 기능
	(데이터베이스 안에서 임시로 데이터 직접 추가해서 확인
	출력할때 클래스 안에 포함된 메서드를 사용(예:show)
10)	영화 , 스텝 코드 중복 체크 메서드 (반환 True/False)
11)	Insert 메서드 구현
	Main.py에 명령어 추가
	어댑터py에 메서드 구현
	Insert 호출 전에 중복 체크
12)	Crawling_movie.py 생성 및 영화 크롤링 기능 구현
	영화 정보 insert(중복체크 후)
	Main.py에서 호출되도록 명령 추가
13)	Crawling_casting.py생성 및 데이터 등록
	영화 목록(DB에 있는 데이터)를 기반으로 영화배우 크롤링 시작
	STAFF 중복 체크 및 INSERT
	CASTING 중복 체크 및 INSERT
	(스태프 및 캐스팅 정보의 중복유무를 한번에 체크하기 위한 아이디어 고민! 공통인 staff_code를 통해서 검사)
14)	영화테이블에서 CASTING_COUNT 컬럼 추가
	CASTING_COUNT(INT) 추가 (배우 전체 수)
15)	영화 목록 html 저장
16)	영화 목록 클릭 시 상세화면 html저장



9일차 16번까지 전부 완료 - 코드 다듬기

### 10일차
코드 정리 + HTML 

### 11일차
2주차동안 배운것 

### 12일차
미니프로젝트 <카드데이터 활용한 새로운 카드 제안하기>
데이터분석 + 인공지능 예측 활용
제안 ppt: [프레젠테이션1.pdf](https://github.com/schw240/07.27-12.1_CLOUD/files/5056425/1.pdf)

### 13일차
미니프로젝트 <카드데이터 활용한 새로운 카드 제안하기>
EDA [사진.zip](https://github.com/schw240/07.27-12.1_CLOUD/files/5062781/default.zip)

### 14일차
발표 [final_2.pptx](https://github.com/schw240/07.27-12.1_CLOUD/files/5068143/final_2.pptx)

### 15일차
1) 크롤링한 데이터 분석 방법
  : 자연어 분석 및 코드 실습
 
2) AWS로 웹서버 구축하기
  : 프로젝트를 AWS로 돌려보기

### 16일차
1) R 사용방법 및 실습
  : R을 이용하여 간단한 분석 및 시각화
  
2) 트위터 API를 활용하여 챗봇 만들어보기
  : 날씨 데이터를 크롤링해와서 날씨 정보를 트위터에 자동으로 업로드하기
  
### 17일차
1) 파이썬을 이용한 간단한 테스트 + 실습

2) 데이터베이스 이론 + 


### 18일차
1) 파이썬을 활용한 mysql 실습

2) 데이터베이스 실습(서브쿼리 + JOIN)

### 19일차
1) 파이썬 주유소 조회 프로그램 만들기

2) 데이터베이스 연습(JOIN)

### 20일차
1) 데이터베이스 연습(JOIN , VIEW ,FOREIGN KEY)

2) 웹프로그래밍 HTML

### 21일차
1) 웹프로그래밍 HTML

2) 웹프로그래밍 CSS

### 22일차
1) 웹프로그래밍 CSS

2) Git

### 23일차
1) 웹프로그래밍 CSS 진짜 웹페이지처럼 꾸며보기

### 24일차
1) 웹프로그래밍 - 자바스크립트 1일차(기본 문법)

### 25일차
1) 웹프로그래밍 - 자바스크립트 2일차(DOM) + 실습

### 26일차
1) 웹프로그래밍 - 자바스크립트 3일차(이벤트) + 실습

### 27일차
1) 웹프로그래밍 - 자바스크립트 4일차

2) 웹프로그래밍 - 장고(서버)

### 28일차
1) 웹프로그래밍 - 장고(서버)