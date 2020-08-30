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

#Python Accessing CSV Files -read and write-
with open("names.csv","r") as fileobject:
	readcsvfile = csv.reader(fileobject, delimiter=",")
	#print(readcsvfile) #print <_csv.reader object at 0x7f0ddab07208>
	for eachreadcsvfile in readcsvfile:
		#print(eachreadcsvfile) #print ['first_name', 'last_name', 'email']\n ['John', 'Doe', 'john-doe@bogusemail.com']\n . . .
		print(eachreadcsvfile[0]+", "+eachreadcsvfile[1]+", "+eachreadcsvfile[2]) #print first_name, last_name, email\n John, Doe, john-doe@bogusemail.com\n . . .
firstname = ["Blake","Denise"]
lastname = ["Bell","Davidson"]
email = ["bbell@bogusemail.com","ddavidson@bogusemail.com"]
with open("names.csv","a",newline="") as fileobject:
	#writecsvfile = csv.writer(fileobject, delimiter=",", quoting=csv.QUOTE_ALL) #quoting=csv.QUOTE_ALL to include the quotes
	writecsvfile = csv.writer(fileobject, delimiter=",", quoting=csv.QUOTE_NONE) #quoting=csv.QUOTE_NONE no quotes is default
	for indexnumber in range(0,len(firstname)):
		writecsvfile.writerow([firstname[indexnumber],lastname[indexnumber],email[indexnumber]])
with open("names.csv") as fileobject:
	dictionarycsvfile = csv.DictReader(fileobject, delimiter=",")
	for eachdictionarycsvfile in dictionarycsvfile:
		print(eachdictionarycsvfile["first_name"]+", "+eachdictionarycsvfile["last_name"]+", "+eachdictionarycsvfile["email"]) #print John, Doe, john-doe@bogusemail.com\n  Mary, Smith-Robinson, maryjacobs@bogusemail.com\n . . .

#Day 14 CSV Files with Python - Read- Write - Append
with open("data.csv","w+") as csvfileobject: #w+ read and write.  Overwrites existing file or creates new file.
	writecsvfile = csv.writer(csvfileobject)
	writecsvfile.writerow(["Title header","Description header","Column 3 header"])
	writecsvfile.writerow(["Row 1","Some description","Another"])
	writecsvfile.writerow(["Row 2","Some description","Bother"])
with open("data.csv","r+") as csvfileobject: #r+ read and write.
	readcsvfile = csv.reader(csvfileobject)
	for eachreadcsvfile in readcsvfile:
		print(eachreadcsvfile)
		'''
		['Title header', 'Description header', 'Column 3 header']
		['Row 1', 'Some description', 'Another']
		['Row 2', 'Some description', 'Bother']
		'''
with open("data.csv","a+") as csvfileobject: #a+ read and append.
	writecsvfile = csv.writer(csvfileobject)
	writecsvfile.writerow(["Row 3","More description","Cookie"])
	writecsvfile.writerow(["Row 4","Big description","Delta"])
with open("data.csv","r") as csvfileobject:
	dictionaryreadcsvfile = csv.DictReader(csvfileobject)
	print(dictionaryreadcsvfile) #print <csv.DictReader object at 0x7f8577ead518>
	print(type(dictionaryreadcsvfile)) #print <class 'csv.DictReader'>
	for eachdictionaryreadcsvfile in dictionaryreadcsvfile:
		print(eachdictionaryreadcsvfile)
		print(eachdictionaryreadcsvfile.keys())
		print(eachdictionaryreadcsvfile["Title header"])
		'''
		OrderedDict([('Title header', 'Row 1'), ('Description header', 'Some description'), ('Column 3 header', 'Another')])
		odict_keys(['Title header', 'Description header', 'Column 3 header'])
		Row 1
		OrderedDict([('Title header', 'Row 2'), ('Description header', 'Some description'), ('Column 3 header', 'Bother')])
		odict_keys(['Title header', 'Description header', 'Column 3 header'])
		Row 2
		...
		'''
		keyslist = eachdictionaryreadcsvfile.keys()
		for eachkeyslist in keyslist:
			print(eachdictionaryreadcsvfile[eachkeyslist])
			'''
			Row 1
			Some description
			Another
			Row 2
			Some description
			Bother
			...
			'''
	#print(len(dictionaryreadcsvfile)) #print TypeError: object of type 'DictReader' has no len()
with open("data.csv","a") as dictionaryappendcsvfile:
	headernames = ["Title header","Description header","Column 3 header"]
	dictionarywriter = csv.DictWriter(dictionaryappendcsvfile, fieldnames=headernames)
	dictionarywriter.writeheader() #write the header or fieldnames; in this case, headernames variable.
	dictionarywriter.writerow({"Title header":"Row 5", "Description header":"Append description","Column 3 header":"Eclaire"})

#Day 15 Functions to Dynamically Add Data to CSV with Python
def getlength(filename):
	with open(filename) as csvfile:
		reader = csv.reader(csvfile)
		readerlist = list(reader)
		print(len(readerlist)+1)
		return len(readerlist)+1
def appendata(filename, name, email):
	fieldnames = ["id","name","email"]
	nextid = getlength(filename)
	with open(filename,"a") as appendcsvfile:
		dictionaryappend = csv.DictWriter(appendcsvfile, fieldnames=fieldnames)
		dictionaryappend.writeheader() #write the header or fieldnames; in this case, headernames variable.
		dictionaryappend.writerow({"id":nextid,"name":name,"email":email})
appendata("datanames.csv","Justin","hello@teamcfe.com")

#Day 16 Edit CSV with Python - Part 2
import shutil
from tempfile import NamedTemporaryFile
def getlength(filename):
	with open(filename) as csvfile:
		reader = csv.reader(csvfile)
		readerlist = list(reader)
		print(len(readerlist)+1)
		return len(readerlist)+1
def appendata(filename, name, email):
	fieldnames = ["id","name","email"]
	nextid = getlength(filename)
	with open(filename,"a") as appendcsvfile:
		dictionaryappend = csv.DictWriter(appendcsvfile, fieldnames=fieldnames)
		dictionaryappend.writeheader() #write the header or fieldnames; in this case, headernames variable.
		dictionaryappend.writerow({"id":nextid,"name":name,"email":email})
#appendata("datanames.csv","Justin","hello@teamcfe.com")
filename = "datanames.csv"
temp_file = NamedTemporaryFile(delete=False)
with open(filename, "rb") as csvfile, temp_file:
	reader = csv.DictReader(csvfile)
	fieldnames = ["id","name","email","amount","sent"]
	writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
	writer.writeheader()
	for row in reader:
		print(row)
		writer.writerow({"id":row["id"], "name":row["name"], "email": row["email"], "amount":"1293.23", "sent":""})
	shutil.move(temp_file.name, filename)

#Long Intro tutorial starts at 826 Python for Beginners Reading - Manipulating CSV Files
import csv
csvfile = open("Google Stock Market Data - google_stock_data.csv.csv")
csvfileobject = csv.reader(csvfile)
openpricelist = []
for eachcsvfileobject in csvfileobject:
	print(eachcsvfileobject)
	print("open column second position first index "+eachcsvfileobject[1])
	'''
	['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
	open column second position first index Open
	['8/19/2014', '585.002622', '587.342658', '584.002627', '586.862643', '978600', '586.862643']
	open column second position first index 585.002622
	'''
	openpricelist.append(eachcsvfileobject[1])
csvfile.close()
print(openpricelist) #print ['Open', '585.002622', '576.11258', '577.862619', '576.182596', '567.312567', '564.522567', '569.992585', '563.562536', '568.00257', '561.782569', '570.052564', '569.042592', '570.402584', '580.602616', '586.55265', '588.752653', '588.072688', '590.402686', '596.452725', . . . 

#Reading CSV Files With Python-s csv Module
import csv
with open("Google Stock Market Data - google_stock_data.csv.csv") as csvfileobject:
	csvreader=csv.reader(csvfileobject, delimiter=",")
	linecount = 0
	for eachcsvreader in csvreader:
		if linecount == 0:
			print("Column names are "+(", ".join(eachcsvreader))) #print Column names are Date, Open, High, Low, Close, Volume, Adj Close
			linecount = 1
		else:
			print("Open price column 2 "+eachcsvreader[1]+" Close price column 5 "+eachcsvreader[4])
			'''
			Open price column 2 585.002622 Close price column 5 586.862643
			Open price column 2 576.11258 Close price column 5 582.162619
			Open price column 2 577.862619 Close price column 5 573.482626
			...
			'''
with open("Google Stock Market Data - google_stock_data.csv.csv") as csvfileobjectdictionary:
	csvdictionaryreader=csv.DictReader(csvfileobjectdictionary, delimiter=",")
	linecount = 0
	for eachcsvdictionaryreader in csvdictionaryreader:
		print(eachcsvdictionaryreader)
		print("Columns "+ ", ".join(eachcsvdictionaryreader))
		print("Date "+ eachcsvdictionaryreader["Date"])
		print("Open "+ eachcsvdictionaryreader["Open"])
		print("Close "+ eachcsvdictionaryreader["Close"])
		'''
		OrderedDict([('Date', '8/19/2014'), ('Open', '585.002622'), ('High', '587.342658'), ('Low', '584.002627'), ('Close', '586.862643'), ('Volume', '978600'), ('Adj Close', '586.862643')])
		Columns Date, Open, High, Low, Close, Volume, Adj Close
		Date 8/19/2014
		Open 585.002622
		Close 586.862643
		OrderedDict([('Date', '8/18/2014'), ('Open', '576.11258'), ('High', '584.512631'), ('Low', '576.002598'), ('Close', '582.162619'), ('Volume', '1284100'), ('Adj Close', '582.162619')])
		Columns Date, Open, High, Low, Close, Volume, Adj Close
		Date 8/18/2014
		Open 576.11258
		Close 582.162619
		OrderedDict([('Date', '8/15/2014'), ('Open', '577.862619'), ('High', '579.382595'), ('Low', '570.522603'), ('Close', '573.482626'), ('Volume', '1519100'), ('Adj Close', '573.482626')])
		Columns Date, Open, High, Low, Close, Volume, Adj Close
		Date 8/15/2014
		Open 577.862619
		Close 573.482626
		...
		'''

#Python 3 Programming Tutorial - Reading from a CSV spreadsheet
import csv
with open("Google Stock Market Data - google_stock_data.csv.csv") as csvfileobject:
	readcsv = csv.reader(csvfileobject, delimiter=",")
	#print(readcsv) #print <_csv.reader object at 0x7f75e100c208>
	for eachreadcsv in readcsv:
		print("Print first column Date "+eachreadcsv[0])		
		print("Print first column Date and sixth column Volume "+eachreadcsv[0]+ " "+eachreadcsv[5])
		'''
		Print first column Date Date
		Print first column Date and sixth column Volume Date Volume
		Print first column Date 8/19/2014
		Print first column Date and sixth column Volume 8/19/2014 978600
		Print first column Date 8/18/2014
		Print first column Date and sixth column Volume 8/18/2014 1284100
		Print first column Date 8/15/2014
		Print first column Date and sixth column Volume 8/15/2014 1519100
		...
		'''
with open("Google Stock Market Data - google_stock_data.csv.csv") as csvfileobject:
	readcsv = csv.reader(csvfileobject, delimiter=",")
	datelist = []
	closepricelist = []
	for datescloseprices in readcsv:
		datecolumn = datescloseprices[0]
		closepricecolumn = datescloseprices[4]
		datelist.append(datecolumn)
		closepricelist.append(closepricecolumn)
	print(datelist) #print ['Date', '8/19/2014', '8/18/2014', '8/15/2014', '8/14/2014', . . .
	print(closepricelist) #print ['Close', '586.862643', '582.162619', '573.482626', '574.652582', . . .

#How to Sort CSV files and lists in Python
import csv
import operator
sample = open("data.csv","r")
csvfile = csv.reader(sample, delimiter=",")
sortfile = sorted(csvfile,key=operator.itemgetter(0)) #sort by first column
for eachline in sortfile:
	print(eachline)
	'''
	['Row 1', 'Some description', 'Another']
	['Row 2', 'Some description', 'Bother']
	['Row 3', 'More description', 'Cookie']
	['Row 4', 'Big description', 'Delta']
	['Row 5', 'Append description', 'Eclaire']
	['Title header', 'Description header', 'Column 3 header']
	['Title header', 'Description header', 'Column 3 header']
	'''
sample.close()
sample = open("data.csv","r")
csvfile = csv.reader(sample, delimiter=",")
sortfile = sorted(csvfile,key=operator.itemgetter(1)) #sort by second column
for eachline in sortfile:
	print(eachline)
	'''
	['Row 5', 'Append description', 'Eclaire']
	['Row 4', 'Big description', 'Delta']
	['Title header', 'Description header', 'Column 3 header']
	['Title header', 'Description header', 'Column 3 header']
	['Row 3', 'More description', 'Cookie']
	['Row 1', 'Some description', 'Another']
	['Row 2', 'Some description', 'Bother']
	'''
sample.close()
alistofnumbertuples = [(5,6),(7,1),(3,2)]
sortnumbers = sorted(alistofnumbertuples,key=operator.itemgetter(0))
print(sortnumbers) #print [(3, 2), (5, 6), (7, 1)]
for eachsortnumbers in sortnumbers:
	print(eachsortnumbers)
	'''
	(3, 2)
	(5, 6)
	(7, 1)
	'''

#Prepare Twitter CSV project review write csv and basic Python
import csv
with open("temptwitter.csv",'w') as fileobject:
	csvwriter = csv.writer(fileobject)
	for i in range(1,10):
		multipleurls = "https://www.innovateinfinitely.com, https://www.google.com, https://www.yahoo.com, https://www.reddit.com"
		csvwriter.writerow([i,multipleurls])
multipleurlslist = ["https://www.innovateinfinitely.com", "https://www.google.com", "https://www.yahoo.com", "https://www.reddit.com"]
print(multipleurlslist) #print ['https://www.innovateinfinitely.com', 'https://www.google.com', 'https://www.yahoo.com', 'https://www.reddit.com']
notmultipleurlslist = ", ".join(multipleurlslist)
print(notmultipleurlslist) #print https://www.innovateinfinitely.com, https://www.google.com, https://www.yahoo.com, https://www.reddit.com
notmultipleurlslistnospace = ",".join(multipleurlslist)
print(notmultipleurlslistnospace) #print https://www.innovateinfinitely.com,https://www.google.com,https://www.yahoo.com,https://www.reddit.com