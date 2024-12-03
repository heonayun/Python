import csv
import matplotlib.pyplot as plt

path = "lifespan.csv"

# 데이터 배열
years = []    # 연도
lifespans = []   # 평균 수명

with open(path, mode='r') as file:
    reader = csv.reader(file)  
    header = next(reader)
    
    for row in reader:
        a = row[0]  
        b = row[1]   

        years.append(int(a))
        lifespans.append(float(b))

plt.plot(years, lifespans, color='r')
plt.title("Average Lifespan Over the Years", fontsize=15)  # 타이틀 수정
plt.xlabel("Year", fontsize=10)  # x축 레이블 수정
plt.ylabel("Average Lifespan (years)", fontsize=10)  # y축 레이블 수정
plt.show()
