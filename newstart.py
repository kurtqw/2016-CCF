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
# 	writer.writerow([line[1]]+[line[3]]+[line[12]]+[timeStamp]+[line[9]]+[line[2]])

# csvfile.close() 
# csvfile1.close()



# csvfile = file('product_market.csv', 'rb')
# reader = csv.reader(csvfile)
# csvfile1 = file('producttimestamp.csv', 'wb')
# writer = csv.writer(csvfile1)

# csvfile.readline()
# for line in reader:
# 	timeArray = time.strptime(line[4],"%Y-%m-%d")
# 	#转换为时间戳:
# 	timeStamp = int(time.mktime(timeArray))
# 	print timeStamp
# 	writer.writerow([line[1]]+[line[3]]+[line[4]]+[timeStamp]+[line[2]])

# csvfile.close() 
# csvfile1.close()

csvfile4 = file('farmingwithTYPE.csv', 'wb')
writer4 = csv.writer(csvfile4)


csvfile2 = file('producttimestamp.csv','rb')
reader2 = csv.reader(csvfile2)
pre = ['','','']
for line2 in reader2:
	if not (line2[0]==pre[0] and line2[1]==pre[1] and line2[2]==pre[2]):	#判断是否需要计算曲线
		csvfile3 = file('farmingtimestamp.csv', 'rb')	#读文件
		reader3 = csv.reader(csvfile3)
		i=0
		for line3 in reader3:
			
			if (line2[0]==line3[0] and line2[1]==line3[1] and line2[2]==pre[2]):
				i+=1
				
			if(i>0 and not (line2[0]==line3[0] and line2[1]==line3[1]) and line2[2]==pre[2]):
				writer4.writerow(line3)
				break

			if (i==0):
				print line2
			
		pre[0]=line2[0]
		pre[1]=line2[1]
		pre[2]=line2[2]
		csvfile3.close()

csvfile2.close()
csvfile4.close()

# 2producttimestamp 0市场 1产品 2日期 3时间戳 4产品类别
# 3farmingtimestamp 0市场 1产品 2日期 3时间戳 4价格 5产品类别


# 市场名称映射值, 农产品名称映射值, 预测价格产生时间, 预测平均交易价格

# 时间戳转时间
# timeStamp = 1381419600
# timeArray = time.localtime(timeStamp)
# otherStyleTime = time.strftime("%Y/%m/%d", timeArray)