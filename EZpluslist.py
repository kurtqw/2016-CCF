# coding: utf-8
import numpy
import csv
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
import time


# csvfile = file('product_market1.csv', 'rb')
# reader = csv.reader(csvfile)
# csvfile1 = file('producttimestamp1.csv', 'wb')
# writer = csv.writer(csvfile1)

# csvfile.readline()
# for line in reader:
# 	timeArray = time.strptime(line[9],"%Y/%m/%d")
# 	#转换为时间戳:
# 	timeStamp = int(time.mktime(timeArray))
# 	print timeStamp
# 	writer.writerow([line[1]]+[line[3]]+[line[9]]+[timeStamp])

# csvfile.close() 
# csvfile1.close()

csvfile4 = file('farmingpluslist.csv', 'wb')
writer4 = csv.writer(csvfile4)

csvfile2 = file('pluslist.csv','rb')
reader2 = csv.reader(csvfile2)
pre = ['','','']
for line2 in reader2:
	if not (line2[0]==pre[0] and line2[1]==pre[1] and line2[4]==pre[2]):	#判断是否需要计算曲线
		csvfile3 = file('farmingwithTYPE.csv', 'rb')	#读文件
		reader3 = csv.reader(csvfile3)
		i=0
		for line3 in reader3:
			
			if (line2[0]==line3[0] and line2[1]==line3[1] and line2[4]==line3[5]):
				# if(float(line3[3])>=1464710400):
				writer4.writerow(line3)
				print line3
				i+=1
				
			if(i>0 and not (line2[0]==line3[0] and line2[1]==line3[1] and line2[4]==line3[5])):
				# if(j==1):
				# 	print line2
				break
			
		pre[0]=line2[0]
		pre[1]=line2[1]
		csvfile3.close()


	# print line2
	# writer4.writerow([line2[0]]+[line2[1]]+[line2[2]]+[a*a*a*z1[0]+a*a*z1[1]+a*z1[2]+z1[3]])
csvfile4.close()
csvfile2.close()




# 2producttimestamp 0市场 1产品 2日期 3时间戳
# 3farmingtimestamp 0市场 1产品 2日期 3时间戳 4价格


# 市场名称映射值, 农产品名称映射值, 预测价格产生时间, 预测平均交易价格

# 时间戳转时间
# timeStamp = 1381419600
# timeArray = time.localtime(timeStamp)
# otherStyleTime = time.strftime("%Y/%m/%d", timeArray)