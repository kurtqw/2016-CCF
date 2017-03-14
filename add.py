# coding: utf-8
import numpy
import csv
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
import time


# csvfile = file('farming.csv', 'rb')
# reader = csv.reader(csvfile)
# csvfile1 = file('farmingtimestamp.csv', 'wb')
# writer = csv.writer(csvfile1)

# csvfile.readline()
# for line in reader:
# 	timeArray = time.strptime(line[12],"%Y-%m-%d")
# 	#转换为时间戳:
# 	timeStamp = int(time.mktime(timeArray))
# 	print timeStamp
# 	writer.writerow([line[1]]+[line[3]]+[line[12]]+[timeStamp]+[line[9]])

# csvfile.close() 
# csvfile1.close()



csvfile1 = file('farmingNEW1.csv','wb')
writer1 = csv.writer(csvfile1)
csvfile2 = file('farmingwithinamonth.csv','rb')
reader2 = csv.reader(csvfile2)
csvfile3 = file('farmingpluslist.csv','rb')
reader3 = csv.reader(csvfile3)

for line2 in reader2:
	writer1.writerow(line2)
for line3 in reader3:
	writer1.writerow(line3)


csvfile1.close()
csvfile2.close()
csvfile3.close()





# 2producttimestamp 0市场 1产品 2日期 3时间戳
# 3farmingtimestamp 0市场 1产品 2日期 3时间戳 4价格


# 市场名称映射值, 农产品名称映射值, 预测价格产生时间, 预测平均交易价格

# 时间戳转时间
# timeStamp = 1381419600
# timeArray = time.localtime(timeStamp)
# otherStyleTime = time.strftime("%Y/%m/%d", timeArray)