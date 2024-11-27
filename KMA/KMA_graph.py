## [데이터 시각화]

import csv
import matplotlib.pyplot as plt #파이플롯
## 인터프린트 언어는 대부분 별칭이 있다.
## matplotlib에는 수학적 연산, 정교한 그래프 등을 포함한다.(라이브러리)
## 라이브러리는 기본적으로 제공되지 않기 때문에 impot를 해줘야한다.
## jsoup, ojdbc6.jar 같은 거다.

file_path = "test.csv"

date_list = []
temps = []
with open(file_path,mode='r') as file :
    reader = csv.reader(file) 

    header = next(reader)

## Alt + 3 , 4
##    i = 0
    for row in reader :
        a = row[2] 
        b = row[-2]
        if a.startswith("Jan") :
            print(a,b)
            date_list.append(a)
            temps.append(float(b))
##            i += 1
##            if i == 10 :
##                break

##그래프를 그리고()
##그린 그래프를 화면에 출력해줘()
##plt.plot(x축 데이터, y축 데이터)
plt.plot(date_list,temps,marker='o',color='r', linestyle=':')
plt.title("Temperature in january",fontsize=15)
plt.xlabel("Date", fontsize=10)
plt.ylabel("Temperature", fontsize=10)
plt.show()
