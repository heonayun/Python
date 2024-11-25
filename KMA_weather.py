## 3번째 일시
## 4번째 평균 기온

import csv

file_path = "test.csv"

## with open(파일명,mode='어떤모드로 읽을지',encoding="UTF-8") as 객체명 :
## 로드가 완료된것
## reader는 보라색이 아니다 >> 내장함수가 아니다 >> csv의 패키지꺼임
with open(file_path,mode='r') as file :
    reader = csv.reader(file) ## 자바에서 패키지, 파이썬에서는 모듈

    ## 첫줄을 읽어버리고
    header = next(reader)
    
    for row in reader :
        a = row[2] ##12월인 데이터만 출력하고싶어
        b = row[-2]
        ## if a가 Dec 시작하면 :
        if a.startswith("Jan") :
            print(a,b) ## 파이썬에서 문자열을 붙이기 위해 , 를 사용한다.
        ## print(row) ## row가 list타입 파일이다.
