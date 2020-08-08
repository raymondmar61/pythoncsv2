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