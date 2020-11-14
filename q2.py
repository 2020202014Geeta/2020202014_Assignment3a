from sys import argv
month = [31,29,31,30,31,30,31,31,30,31,30,31]
monthConv={"Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,"Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12}

def checkLeapYear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                oddDays = 1
            else:
                oddDays = 0
        else:
            oddDays = 1
    else:
        oddDays = 0
    return oddDays

def addLeapDays(y1,y2):
    days = 0
    i = y1 + 1
    while i < y2:
        if(checkLeapYear(i)):
            days = days + 366
        else:
            days = days + 365
        i = i + 1
    return days  

def finDaysAfterM1(i,lastMonth,y1):
    daysAftrM1 = 0
    while i <= lastMonth:
        if i==2:
            daysAftrM1 = daysAftrM1 + month[i-1]
            if checkLeapYear(y1)==0:   #if not a leap year subtract one
                daysAftrM1 = daysAftrM1 - 1
        else:
            daysAftrM1 = daysAftrM1 + month[i-1]
        i = i + 1
    return daysAftrM1  

def daysInY1(m1,m2,y1,y2):
    oddDays = 0
    daysAftrM1 = 0
    if m1==2 and checkLeapYear(y1)==0:   #if not a leap year subtract one 
        oddDays = oddDays -1
    if y1==y2:
        lastMonth = m2 - 1 
    else:
        lastMonth = 12
    i = m1 + 1
    daysAftrM1 = finDaysAfterM1(i,lastMonth,y1)
    return oddDays + daysAftrM1 

def daysInY2(m1,m2,y1,y2):
    daysBefM2 = 0
    if y1==y2:
        return daysBefM2   # has checked in Y1 already

    i = 1
    while i < m2:
        if i==2:
            daysBefM2 = daysBefM2 + month[i-1]
            if checkLeapYear(y2)==0:   #if not a leap year subtract one
                daysBefM2 = daysBefM2 - 1
        else:
            daysBefM2 = daysBefM2 + month[i-1]
        i = i + 1
    return daysBefM2 

# Driver's code
file=open("date_calculator.txt")
infoInFile=file.readlines()
str1=""
str2=""
dates=[]
userDateForm = argv[1]
if userDateForm[0]=='d':
    for i in range(0,len(infoInFile)):
        str1=""
        infoInFile[i]=infoInFile[i].replace("\n","")
        date=""
        months=""
        year=""
        array123=infoInFile[i].split(" ")
        if(len(array123)>2):
            for j in range(0,2):
                if array123[1][j].isnumeric()==True:
                    date=date+str(array123[1][j])
            months=str(monthConv.get(array123[2][0:3]))
            year=str(array123[3])
            str1=date+'/'+months+'/'+year
    
        else:
            str1=array123[1].replace(".","/").replace("-", "/")
        dates.append(str1)
else:
    for i in range(0,len(infoInFile)):
        str1=""
        infoInFile[i]=infoInFile[i].replace("\n","")
        date=""
        months=""
        year=""
        array123=infoInFile[i].split(" ")
        if(len(array123)>2):
            for j in range(0,2):
                if array123[2][j].isnumeric()==True:
                    date=date+str(array123[2][j])
            months=str(monthConv.get(array123[1][0:3]))
            year=str(array123[3])
            str1=date+'/'+months+'/'+year
        else:
            str1=array123[1].replace(".","/").replace("-", "/")
            str2=str1.split("/")
            date=str2[1]
            month=str2[0]
            year=str2[2]
            str1=date+'/'+months+'/'+year
        dates.append(str1)    
            

date1 = str(dates[0])
date2 = str(dates[1])
 

#dd/mm/yyyy
brokenDate1 = date1.split("/")
brokenDate2 = date2.split("/")

dd1=int(brokenDate1[0])
dd2=int(brokenDate2[0])

mm1=int(brokenDate1[1])
mm2=int(brokenDate2[1])

yy1=int(brokenDate1[2])
yy2=int(brokenDate2[2])   

leapDays = addLeapDays(yy1,yy2)
daysInYear1 = daysInY1(mm1,mm2,yy1,yy2)        # atfer mm1
daysInYear2 = daysInY2(mm1,mm2,yy1,yy2)        # before mm2 if not in the same year else 0
if mm1 == mm2 and yy1 == yy2:
    if dd1 == dd2:
        daysInY12 = 0
    else:
        daysInY12 = dd2 - dd1
else:
    daysInY12 = month[mm1-1]-dd1 + dd2

days= daysInYear1 + daysInY12 + leapDays + daysInYear2
#print(leapDays)
#print(daysInYear1)
#print(daysInYear2)
#print(month[mm1-1]-dd1)
#print(month[mm1-1]-dd1 + dd2)
#print(daysInY12)
#print (days)
fOut=open("output.txt","w+")
if days == 1:
    meta = "Day"
else:
    meta = "Days"
fOut.write("Date Difference: " + str(days) + " " + meta)
fOut.close()