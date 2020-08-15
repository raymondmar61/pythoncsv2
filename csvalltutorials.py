import csv

#Python Tutorial CSV Module - How to Read- Parse- and Write CSV Files
with open("names.csv","r") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	print(csvreader) #print <_csv.reader object at 0x7f23a250d198>
	for eachline in csvreader:
		print(eachline)
		'''
		['first_name', 'last_name', 'email']
		['John', 'Doe', 'john-doe@bogusemail.com']
		...
		'''
with open("names.csv","r") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	for indextwo in csvreader:
		print(indextwo[2])
		'''
		email
		john-doe@bogusemail.com
		...
		'''
with open("names.csv","r") as csvfile:
	csvreader = csv.reader(csvfile) #delimiter="," is default.  If comma, then no need to include delimiter.
	next(csvreader)
	for nocolumnheader in csvreader:
		print(nocolumnheader[2])
		'''
		john-doe@bogusemail.com
		maryjacobs@bogusemail.com
		...
		'''
with open ("names.csv","r") as csvfile:
	csvreader = csv.reader(csvfile)
	with open("newnames.csv","w") as newcsvfile:
		csvwriter = csv.writer(newcsvfile, delimiter="-")  #tab delimiter is delimiter="\t"
		for line in csvreader:
			csvwriter.writerow(line)
			'''
			first_name-last_name-email
			John-Doe-"john-doe@bogusemail.com"
			Mary-"Smith-Robinson"-maryjacobs@bogusemail.com
			Dave-Smith-davesmith@bogusemail.com
			...
			'''
with open ("names.csv","r") as csvfile:
	csvreader = csv.DictReader(csvfile)
	print(csvreader) #print <csv.DictReader object at 0x7fc523e3d358>
	for ordereddictionary in csvreader:
		print(ordereddictionary)
		print(ordereddictionary["email"])
		'''
		OrderedDict([('first_name', 'John'), ('last_name', 'Doe'), ('email', 'john-doe@bogusemail.com')])
		john-doe@bogusemail.com
		OrderedDict([('first_name', 'Mary'), ('last_name', 'Smith-Robinson'), ('email', 'maryjacobs@bogusemail.com')])
		maryjacobs@bogusemail.com
		...
		'''
with open ("names.csv","r") as csvfile:
	csvreader = csv.DictReader(csvfile)
	with open("newnamesdictionary.csv","w") as newcsvdictionary:
		columnheaders = ["first_name","last_name","email"]
		csvwriter = csv.DictWriter(newcsvdictionary, fieldnames=columnheaders, delimiter="\t")
		csvwriter.writeheader()
		for ordereddictionary in csvreader:
			csvwriter.writerow(ordereddictionary)
with open ("names.csv","r") as csvfile:
	csvreader = csv.DictReader(csvfile)
	with open("newnamesdictionary.csv","w") as newcsvdictionary:
		columnheaders = ["first_name","last_name"]
		csvwriter = csv.DictWriter(newcsvdictionary, fieldnames=columnheaders, delimiter="\t")
		csvwriter.writeheader()
		for ordereddictionarynoemail in csvreader:
			del ordereddictionarynoemail["email"]
			csvwriter.writerow(ordereddictionarynoemail)

#CSV Files in Python Python Tutorial Learn Python Programming
from datetime import datetime
import decimal
path = "/home/mar/python/Google Stock Market Data - google_stock_data.csv.csv"
file = open(path)
print(file) #print <_io.TextIOWrapper name='/home/mar/python/Google Stock Market Data - google_stock_data.csv.csv' mode='r' encoding='UTF-8'>
lines = [line for line in open(path)]
print(lines[0]) #print Date,Open,High,Low,Close,Volume,Adj Close
print(lines[1]) #print 8/19/2014,585.002622,587.342658,584.002627,586.862643,978600,586.862643
print(lines[0].strip()) #print Date,Open,High,Low,Close,Volume,Adj Close
print(lines[0].strip().split(",")) #print ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
googlestockdata = [line.strip().split(",") for line in file]
print(googlestockdata[0]) #print ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
print(googlestockdata[1]) #print ['8/19/2014', '585.002622', '587.342658', '584.002627', '586.862643', '978600', '586.862643']
print(googlestockdata[2]) #print ['8/18/2014', '576.11258', '584.512631', '576.002598', '582.162619', '1284100', '582.162619']
file.close()
path = "/home/mar/python/Google Stock Market Data - google_stock_data.csv.csv"
file = open(path)
reader = csv.reader(file)
noheader = next(reader) #The first line is the header.  Exclude the header row.
data = [row for row in reader]
print(noheader) #print ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
print(data[0]) #print ['8/19/2014', '585.002622', '587.342658', '584.002627', '586.862643', '978600', '586.862643'].  The header data[0] is not the zero index in contrast to lines[0] and googlestockdata[0]
file.close()
file = open(path)
reader = csv.reader(file)
noheader = next(reader) #The first line is the header.  Exclude the header row.
googlestockprice = []
for eachreader in reader:
	date = datetime.strptime(eachreader[0],"%m/%d/%Y")
	openprice = float(eachreader[1])
	high = float(eachreader[2])
	low = float(eachreader[3])
	close = float(eachreader[4])
	volume = int(eachreader[5])
	adj_close = float(eachreader[6])
	googlestockprice.append([date, openprice, high, low, close, volume, adj_close])
print(googlestockprice[0]) #print [datetime.datetime(2014, 8, 19, 0, 0), 585.002622, 587.342658, 584.002627, 586.862643, 978600, 586.862643]
file.close()
googlereturnspath = "/home/mar/python/googlereturns.csv"
file = open(googlereturnspath,"w")
writer = csv.writer(file)
writer.writerow(["Date","Return"])
for i in range(0, len(googlestockprice)-1):
	todaysrow = googlestockprice[i]
	todaysdate = todaysrow[0]
	todaysprice = todaysrow[-1]
	yesterdaysrow = googlestockprice[i+1]
	yesterdaysprice = yesterdaysrow[-1]
	dailyreturn = round(((todaysprice - yesterdaysprice)/yesterdaysprice)*100,2)
	todaysdate = todaysdate.strftime("%m/%d/%Y")
	writer.writerow([todaysdate, dailyreturn])
file.close()

#Reading CSV Files In Python
with open("samplecsv.csv","r") as fileobject:
	csvreader = csv.reader(fileobject) #delimiter default is comma
	print(csvreader) #print <_csv.reader object at 0x7f29992ee198>
	for eachcsvreader in csvreader:
		print(eachcsvreader)
		'''
		['Symbol', 'Current Price', 'Date', 'Time', 'Change', 'Open', 'High', 'Low', 'Volume']
		['IMSC', '', '6/28/2019', '18:07 EDT', '', '', '', '', '']
		['GWGWF', '', '6/28/2019', '18:07 EDT', '', '', '', '', '']
		['RLE.V', '', '6/28/2019', '18:07 EDT', '', '', '', '', '']
		['HEK', '', '6/28/2019', '18:07 EDT', '', '', '', '', '']
		['HIIT', '', '', '', '', '', '', '', '']
		['PRMW', '11.295', '3/16/2020', '15:12 EDT', '-2.0249996', '12.39', '12.96', '11.095', '2611014']
		...
		'''
print(csvreader) #print <_csv.reader object at 0x7f29992ee198>
#It seems I need another with open to read the csv file more than once.
with open("samplecsv.csv","r") as fileobject:
	csvreader = csv.reader(fileobject, delimiter=",")
	for eachsymbol in csvreader:
		print(eachsymbol[0])
		'''
		Symbol
		IMSC
		GWGWF
		RLE.V
		HEK
		HIIT
		PRMW
	
		'''
with open("samplecsv.csv","r") as fileobject:
	csvdictionaryreader = csv.DictReader(fileobject)
	for eachcsvdictionaryreader in csvdictionaryreader:
		#The header row is the key for the dictionary
		#print(type(eachcsvdictionaryreader)) #print <class 'collections.OrderedDict'>
		print(eachcsvdictionaryreader)
		'''
		OrderedDict([('Symbol', 'IMSC'), ('Current Price', ''), ('Date', '6/28/2019'), ('Time', '18:07 EDT'), ('Change', ''), ('Open', ''), ('High', ''), ('Low', ''), ('Volume', '')])
		OrderedDict([('Symbol', 'GWGWF'), ('Current Price', ''), ('Date', '6/28/2019'), ('Time', '18:07 EDT'), ('Change', ''), ('Open', ''), ('High', ''), ('Low', ''), ('Volume', '')])
		OrderedDict([('Symbol', 'RLE.V'), ('Current Price', ''), ('Date', '6/28/2019'), ('Time', '18:07 EDT'), ('Change', ''), ('Open', ''), ('High', ''), ('Low', ''), ('Volume', '')])
		OrderedDict([('Symbol', 'HEK'), ('Current Price', ''), ('Date', '6/28/2019'), ('Time', '18:07 EDT'), ('Change', ''), ('Open', ''), ('High', ''), ('Low', ''), ('Volume', '')])
		OrderedDict([('Symbol', 'HIIT'), ('Current Price', ''), ('Date', ''), ('Time', ''), ('Change', ''), ('Open', ''), ('High', ''), ('Low', ''), ('Volume', '')])
		OrderedDict([('Symbol', 'PRMW'), ('Current Price', '11.295'), ('Date', '3/16/2020'), ('Time', '15:12 EDT'), ('Change', '-2.0249996'), ('Open', '12.39'), ('High', '12.96'), ('Low', '11.095'), ('Volume', '2611014')])
		...
		'''
with open("samplecsv.csv","r") as fileobject:
	csvdictionaryreader = csv.DictReader(fileobject, delimiter=",")
	for eachcsvdictionaryreadersymbol in csvdictionaryreader:
		#The header row is the key for the dictionary
		print(eachcsvdictionaryreadersymbol["Symbol"])
		'''
		IMSC
		GWGWF
		RLE.V
		HEK
		HIIT
		PRMW
		...
		'''

#Writing CSV Files in Python
with open("tempcsv.csv","w", newline="") as fileobject:
	csvwriter = csv.writer(fileobject)
	csvwriter.writerow(["column1","column2","column3"])
	csvwriter.writerow(["one","two",'three'])
	for i in range(1,10):
		csvwriter.writerow(["rangeone","rangetwo",'rangethree'])
		'''
		column1,column2,column3
		one,two,three
		rangeone,rangetwo,rangethree
		rangeone,rangetwo,rangethree
		rangeone,rangetwo,rangethree
		...
		'''
with open("tempcsv.csv","w", newline="") as fileobject:
	columnnames = ["columnheader1","columnheader2","columnheader3"]
	csvdictwriter = csv.DictWriter(fileobject, fieldnames=columnnames)
	csvdictwriter.writeheader()
	csvdictwriter.writerow({"columnheader1":"one","columnheader3":"writerow order doesn't matter","columnheader2":"road wallpaper"})
	csvdictwriter.writerow({"columnheader1":"two","columnheader3":"writerow order doesn't matter I'm at the right","columnheader2":"write another row"})
	'''
	columnheader1,columnheader2,columnheader3
	one,road wallpaper,writerow order doesn't matter
	two,write another row,writerow order doesn't matter I'm at the right
	'''

#Reading a CSV file into a Python List
readfile = open("namesages.csv","r")
csvreader = csv.reader(readfile)
namesageslist = []
for eachcsvreader in csvreader:
	namesageslist.append(eachcsvreader)
print(namesageslist) #print [['bob', '65', 'green'], ['fred', '25', 'pink'], ['claire', '35', 'blue'], ['anna', '20', 'orange'], ['jill', '24', 'red'], ['alicia', '50', 'green']]
for eachnamesageslist in namesageslist:
	print(eachnamesageslist)
	'''
	['bob', '65', 'green']
	['fred', '25', 'pink']
	['claire', '35', 'blue']
	['anna', '20', 'orange']
	['jill', '24', 'red']
	['alicia', '50', 'green']
	'''
namesageslistcorrectdatatype = []
for correctdatatype in namesageslist:
	namesageslistcorrectdatatype.append([correctdatatype[0],int(correctdatatype[1]),correctdatatype[2]])
print(namesageslistcorrectdatatype) #print [['bob', 65, 'green'], ['fred', 25, 'pink'], ['claire', 35, 'blue'], ['anna', 20, 'orange'], ['jill', 24, 'red'], ['alicia', 50, 'green']]
namesageslisttryexcept = []
for blanklinesincsv in namesageslist:
	try:
		namesageslisttryexcept.append([blanklinesincsv[0],int(blanklinesincsv[1]),blanklinesincsv[2]])
	except:
		pass
readfile.close()

#Reading a CSV file into a Python Dictionary
openfile = open("namesages.csv","r")
csvreader = csv.reader(openfile)
peopledictionary = {}
for eachcsvreader in csvreader:
	peopledictionary[eachcsvreader[0]] = {"age":eachcsvreader[1],"color":eachcsvreader[2]}
openfile.close()
print(peopledictionary) #print {'bob': {'age': '65', 'color': 'green'}, 'fred': {'age': '25', 'color': 'pink'}, 'claire': {'age': '35', 'color': 'blue'}, 'anna': {'age': '20', 'color': 'orange'}, 'jill': {'age': '24', 'color': 'red'}, 'alicia': {'age': '50', 'color': 'green'}}
print(peopledictionary["bob"]) #print {'age': '65', 'color': 'green'}
print(peopledictionary["bob"]["color"]) #print green
for bonuskeys in peopledictionary.keys():
	print(bonuskeys) #print bob\n fred\n claire\n anna\n jill\n alicia

#
