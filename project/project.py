import csv
import matplotlib.pyplot as plt

file_path="project.csv"

years=[]
births=[]
merries=[]

with open(file_path,mode='r') as file :
    reader = csv.reader(file) 

    header = next(reader)

    for row in reader :
        a = row[0] 
        b = row[1]
        c = row[-1]
        print(a,b,c)
        years.append(int(a))
        births.append(int(b))
        merries.append(float(c))

fig, ax1 = plt.subplots()
ax1.bar(years, births, color='tan', width=0.5, label='births', alpha=0.6)

ax2 = ax1.twinx()
ax2.plot(years, merries, color='r', marker='o', label='merries', linewidth=2)

ax1.set_xlabel('years')
ax1.set_ylabel('births')
ax2.set_ylabel('merries')

ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.title("Birth Rate",fontsize=15)
plt.show()
