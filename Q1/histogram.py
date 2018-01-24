import csv 
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

x = []

f = csv.reader(open('JHfield1.csv', 'rU'), delimiter=",")

for row in f:
	x.append(float(row[1])) # to convert the string type to float type


plt.hist(x, 500, facecolor='green') # 500 is the number of bins
plt.xlabel('J-H Colour Index')
plt.ylabel('N (Number of stars)')
plt.title('Number of Stars with specific J-H colour in Field 1')
plt.xlim(1,3)
plt.show()

#Reference: Lecture notes for seaborn and matplotlib histogram handling and csv module documenation for python
