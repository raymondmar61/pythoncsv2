import csv
with open("testcsvwrite.csv", "w", newline="") as fileobject:
    csvwriter = csv.writer(fileobject)
    csvwriter.writerow(["column1header", "column2header", "column3header"])
    csvwriter.writerow(["one", "1", "I"])
    csvwriter.writerow(["two", "2", "II"])
    csvwriter.writerow(["three", "3", "III"])
    for i in range(1, 10):
        csvwriter.writerow(["rangeone", i, i * 10])


with open("testininblog.csv", "w", newline="") as fileobject:
    csvwriter = csv.writer(fileobject, delimiter="\t")
    csvwriter.writerow(["Title", "URL", "Date", "Time", "Timeampm"])

title = "Daylight Standard, Time '08"
url = "https://ininblog.blogspot.com/2008/11/daylight-standard-time-08.html"
date = "2008-11-02"
time = "01:07"
timeampm = "1:07 AM"

with open("testininblog.csv", "a", newline="") as fileobject:
    csvwriter = csv.writer(fileobject, delimiter="\t")
    csvwriter.writerow([title, url, date, time, timeampm])


with open("testforloop.csv", "w", newline="") as fileobject:
    csvwriter = csv.writer(fileobject, delimiter="\t")
    csvwriter.writerow(["column1header", "column2header", "column3header", "column4header", "column5header"])

for i in range(1, 10):
    print(i)
    j = i + 1
    k = i + 2
    with open("testforloop.csv", "a", newline="") as fileobject:
        csvwriter = csv.writer(fileobject, delimiter="\t")
        csvwriter.writerow([i * 1, i * 5, i * 10, i * 20, i * 50])
        csvwriter.writerow([j * 1, j * 5, j * 10, j * 20, j * 50])
        csvwriter.writerow([k * 1, k * 5, k * 10, k * 20, k * 50])
