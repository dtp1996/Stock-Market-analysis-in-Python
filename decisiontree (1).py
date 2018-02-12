import random
import MySQLdb
import math
from sklearn import svm
from sklearn import linear_model
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from decimal import Decimal
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import pandas

def direction():
	sen,nif=0,0
	if list5[size-1]<predicted1[0]:
		nif=1
	else:
		nif=0
	if list1[size-1]<predicted[0]:
		sen= 1
	else:
		sen= 0
	return nif or sen

#import pandas.io.sql as psql
for x in range(0,30):
	day=random.randint(1,31)
	month=random.randint(1,12)
	year=random.randint(2010,2015)
	date=str(year)+"-"+str(month)+"-"+str(day)

	#date1=str(year)+"-"+str(month)+"-"+str(day)

	#date="2013-08-14"
	#date1="2013-08-14"

	#print date
	size=30
	conn=MySQLdb.connect(host="localhost",user="root",passwd="sumath",db="project")
	cur1=conn.cursor()
	cur1N=conn.cursor()
	cur2=conn.cursor()
	cur3=conn.cursor()
	cur4=conn.cursor()

	list1=[]
	list2=[]
	list3=[]
	list4=[]
	list5=[]

	quer1="select * from SENSEX where Date>\""+date+"\";"
	quer2="select * from FTSE100 where Date>\""+date+"\";"
	quer3="select * from HANGSENG where Date>\""+date+"\";"
	quer4="select * from OIL where Date>\""+date+"\";"
	quer5="select * from NIFTY where Date>\""+date+"\";"

	cur1.execute(quer1)
	cur2.execute(quer2)
	cur3.execute(quer3)
	cur4.execute(quer4)
	cur1N.execute(quer5)
	date1=[]
	date2=[]
	date3=[]

	row1=cur1.fetchone()
	row2=cur2.fetchone()
	row3=cur3.fetchone()
	row4=cur4.fetchone()
	row5=cur1N.fetchone()

	tdf=[]
	prev=0
	counter=0
	for i in range(0,1500):
	
		date1.append(row1[0])
		date2.append(row2[0])
		date3.append(row3[0])
	
		list1.append(row1[6])
		list2.append(row2[6])
		list3.append(row3[6])	
		list4.append(row4[1])
		list5.append(row5[6])
	
		row1=cur1.fetchone()
		row2=cur2.fetchone()
		row3=cur3.fetchone()
		row4=cur4.fetchone()
		row5=cur1N.fetchone()
		counter+=1
	
		if counter==size:
			break
	'''
	for i in range(0,30):
		print date1[i],list1[i],date2[i],list2[i],date3[i],list3[i]
	'''
	test1=[]
	test2=[]
	test3=[]

	result=[]
	result1=[]

	for i in range(0,3):
		test1.append(row2[6])
		test2.append(row3[6])
		test3.append(row4[1])
		result.append(row1[6])
		result1.append(row5[6])
	
		row1=cur1.fetchone()
		row2=cur2.fetchone()
		row3=cur3.fetchone()
		row4=cur4.fetchone()
		row5=cur1N.fetchone()
	
	#quer1="select `Adj Close` from SENSEX where Date>\""+date+"\";"
	#cur.execute(quer1)
	df=pandas.DataFrame({'FTSE100':list2,'HANGSENG':list3,'OIL':list4})
	df1=pandas.DataFrame({'SENSEX':list1})

	df2=pandas.DataFrame({'NIFTY':list5})

	test_df=pandas.DataFrame({'FTSE100':test1,'HANGSENG':test2,'OIL':test3})
	#cols=['SENSEX','FTSE100']
	#df.columns = cols
	#X = preprocessing.scale(df)
	X=df.as_matrix()
	y=df1.as_matrix()
	y1=df2.as_matrix()
	#testing=test_df.as_matrix()
	#X_scaled = preprocessing.scale(X)
	#print y
	#y=[0,1,0,0,1,1,1,1,1,0]
	test=test_df.as_matrix()
	#working OK
	
	model = tree.DecisionTreeRegressor()
	model1= tree.DecisionTreeRegressor()
	
	model.fit(X,y.ravel())
	model1.fit(X,y1.ravel())
	#print model.score(X,y.ravel())

	predicted= model.predict(test)
	predicted1=model1.predict(test)
	#print predicted
	i=0
	error=0
	error=float(float(predicted[0])-float(result[0]))/float(result[0])
	error=(error)*100
	error=round(error,3)
	
	error1=0
	error1=float(float(predicted1[0])-float(result1[0]))/float(result1[0])
	error1=(error1)*100
	error1=round(error1,3)
	
	if error<1 and error>-1:
		if error1<1 and error1>-1:
			print"\n******************************************************************\n"
			print "*\tThe prediction for index SENSEX:\n*\tDate:"+date
			print "*\tPredicted Value: "+str(predicted[0])
			print "*\tActual Value: "+str(result[0])
			print "*\tError: "+str(error)+"%"
			#print "*\tDay-1 Value: "+str(list1[size-1])
			indicate= direction()
			if indicate==1:
				print "*\t+ve Direction"
			else:
				print "*\t-ve Direction"
			print"\n******************************************************************\n"	
			print "*\tThe prediction for index NIFTY:\n*\tDate:"+date
			print "*\tPredicted Value: "+str(predicted1[0])
			print "*\tActual Value: "+str(result1[0])
			print "*\tError: "+str(error1)+"%"
			#print "*\tDay-1 Value: "+str(list5[size-1])
			indicate= direction()
			if indicate==1:
				print "*\t+ve Direction"
			else:
				print "*\t-ve Direction"
			print"\n******************************************************************\n"
			break



