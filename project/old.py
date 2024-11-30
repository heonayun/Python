import csv
import matplotlib.pyplot as plt

# 들고올 csv 데이터 
file_path="old.csv"

# 데이터 배열
years=[]
olders=[]

# 파일을 열어서 읽기
with open(file_path,mode='r') as file :
    reader = csv.reader(file) 

    # 한줄 먼저 읽어서 수치만 표시
    header = next(reader)
    header = next(reader)

    # 알맞은 값을 배열 넣기
    for row in reader :
        a = row[0] 
        b = row[1]
        print(a,b)

        # 배열에 저장하기 위해 형변환 하여 타입을 지정
        years.append(int(a))
        olders.append(int(b))

# 고령화 수치 그래프 그리기
plt.plot(years, olders, color='r', label='Older Population')

# 그래프 제목 및 레이블 설정
plt.title("Older Population Over the Years", fontsize=15)
plt.xlabel("Year", fontsize=10)
plt.ylabel("Older Population (%)", fontsize=10)

# 범례 표시
plt.legend(loc='upper left')
plt.show()
