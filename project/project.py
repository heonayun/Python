import csv
import matplotlib.pyplot as plt

# 들고올 csv 데이터 
file_path="project.csv"

# 데이터 배열
years=[]
births=[]
merries=[]

# 파일을 열어서 읽기
with open(file_path,mode='r') as file :
    reader = csv.reader(file) 

    # 한줄 먼저 읽어서 수치만 표시
    header = next(reader)

    # 알맞은 값을 배열 넣기
    for row in reader :
        a = row[0] 
        b = row[1]
        c = row[-1]
        print(a,b,c)

        # 배열에 저장하기 위해 형변환 하여 타입을 지정
        years.append(int(a))
        births.append(int(b))
        merries.append(float(c))

plt.plot(date_list,temps,color='r')
plt.title("Temperature in january",fontsize=15)
plt.xlabel("Date", fontsize=10)
plt.ylabel("Temperature", fontsize=10)
plt.show()
