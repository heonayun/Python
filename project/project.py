# 필요한 라이브러리 임포트
import csv
import matplotlib.pyplot as plt

# CSV 파일 경로 지정
file_path = "project.csv"

# 데이터를 저장할 빈 리스트 초기화
years = []    # 연도
births = []   # 출생 수
merries = []  # 결혼율

# CSV 파일을 읽고 처리하기
with open(file_path, mode='r') as file:
    reader = csv.reader(file)  # CSV 파일을 읽기 위한 객체 생성

    # 첫 번째 줄은 헤더이므로 건너뜀
    header = next(reader)

    # 나머지 데이터 행을 반복하며 처리
    for row in reader:
        a = row[0]  # 첫 번째 값(연도)을 a에 저장
        b = row[1]  # 두 번째 값(출생 수)을 b에 저장
        c = row[2]  # 세 번째 값(결혼율)을 c에 저장

        # 각 값을 출력하여 확인
        print(a, b, c)

        # 리스트에 데이터 추가
        years.append(int(a))      # 연도는 정수로 변환하여 추가
        births.append(int(b))     # 출생 수는 정수로 변환하여 추가
        merries.append(float(c)) # 결혼율은 실수로 변환하여 추가

# 시각화를 위한 그래프 설정
fig, ax1 = plt.subplots()  # 하나의 그래프를 그리기 위한 subplot 생성

# 첫 번째 y축을 기준으로 출생 수를 막대그래프(bar chart)로 표시
ax1.bar(years, births, color='tan', width=0.5, label='births', alpha=0.6)

# 두 번째 y축을 설정 (출생 수와 결혼율이 다른 범위의 값을 가지므로)
ax2 = ax1.twinx()

# 두 번째 y축을 기준으로 결혼율을 선 그래프(line plot)로 표시
ax2.plot(years, merries, color='r', marker='o', label='merries', linewidth=2)

# 첫 번째 y축 레이블 설정
ax1.set_xlabel('years')   # x축은 연도를 표시
ax1.set_ylabel('births')   # 첫 번째 y축은 출생 수
ax2.set_ylabel('merries') # 두 번째 y축은 결혼율

# 범례 설정
ax1.legend(loc='upper left')  # 첫 번째 그래프에 대한 범례 위치
ax2.legend(loc='upper right') # 두 번째 그래프에 대한 범례 위치

# 그래프 제목 설정
plt.title("Birth Rate", fontsize=15)

# 그래프 출력
plt.show()
