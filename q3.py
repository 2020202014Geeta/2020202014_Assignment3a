forMinConv = { "9": 0, "10": 1, "11": 2, "12": 3, "1": 4, "2": 5, "3": 6, "4": 7, "5": 8 }
interValS = []
interValE = []

def amPM(timeH):
    if timeH >= 2:
        return "PM"
    else:
        return "AM"

def minInHour(timeMin):
    if timeMin > 3:
        return (timeMin - 3)
    else:
        return (9 + timeMin)

#convert the time
def converBackTime(freeSlotsIntervS,freeSlotsIntervE,intervalToRec):
    i = 0
    length = len(freeSlotsIntervS)
    while i < length:
        hourS = int(freeSlotsIntervS[i]/60)
        minutS = int(freeSlotsIntervS[i] % 60)
        lastS = amPM(hourS)
        if hourS > 3:
            hourS = hourS - 3
        else:
            hourS = 9 + hourS

        hourE = int(freeSlotsIntervE[i]/60)
        minutE = int(freeSlotsIntervE[i] % 60)
        lastE = amPM(hourE)   
        if hourE > 3:
            hourE = hourE - 3
        else:
            hourE = 9 + hourE
        strSlot = str(hourS) + ":" + str(minutS).zfill(2) + lastS + " - " +  str(hourE) + ":" + str(minutE).zfill(2) + lastE
        intervalToRec.append(strSlot)
     #   print(intervalToRec)
        i = i + 1

# finds free slot of both employee
def fillFreeSlots(sepTimeMetaEmp,startE,endE,freeSEmp,freeEEmp):
    remvBrackFromTimeEmp=sepTimeMetaEmp[1].split("]}}")[0]
    extractTimeEmp=remvBrackFromTimeEmp.replace(", ",",").replace(" - ","-").replace("'","").split(",")
    
    for i in extractTimeEmp:
        eachTime = i.split("-")

        temp1=eachTime[0].split(":")
        hourSInMin= ( forMinConv[temp1[0]] ) * 60 + int(temp1[1][0:2])
        startE.append(hourSInMin)

        temp2=eachTime[1].split(":")
        hourEInMin= ( forMinConv[temp2[0]] ) * 60 + int(temp2[1][0:2])
        endE.append(hourEInMin)

    prevEndTime = 0
    for i in range(0,len(startE)):
        if startE[i] > prevEndTime:
            freeSEmp.append(prevEndTime)
            freeEEmp.append(startE[i])
            prevEndTime = endE[i]
        else:
            prevEndTime = endE[i]
    if prevEndTime < 480:
        freeSEmp.append(prevEndTime)
        freeEEmp.append(480)

def mergeInterval(startEm1,endEm1,startEm2,endEm2):
    len1 = len(startEm1)
    len2 = len(startEm2)
    i = 0
    j = 0
    while i < len1 and j <len2:
        if startEm2[j] >= startEm1[i]:
            if startEm2[j] <= endEm1[i]:
                interValS.append( startEm2[j] )
                if endEm2[j] == endEm1[i]:
                    interValE.append(endEm1[i]) 
                    i = i + 1
                    j = j + 1
                elif endEm2[j] > endEm1[i]:
                    interValE.append(endEm1[i]) 
                    i = i + 1
                else:
                    interValE.append(endEm2[j])
                    j = j + 1 
            else:
                i = i + 1
        else:
            if startEm1[i] <= endEm2[j]:
                interValS.append( startEm1[i] )
                if endEm1[i] == endEm2[j]:
                    interValE.append(endEm2[j]) 
                    i = i + 1
                    j = j + 1
                elif endEm1[i] > endEm2[j]:
                    interValE.append(endEm2[j]) 
                    j = j + 1
                else:
                    interValE.append(endEm1[i])
                    i = i + 1 
            else:
                j = j + 1
     
# Driver's code
fd1=open("employee1.txt")
temp1 = fd1.read()
sEmp1 = temp1.split(":[")
metaData1 = sEmp1[0].replace("': {",":").split(":")
empName1 = metaData1[0].replace("{'","")
date = metaData1[1].replace("{'","")
#print(date)
#print(empName1)

fd2=open("employee2.txt")        
temp2 = fd2.read()
sEmp2 = temp2.split(":[")
metaData2 = sEmp2[0].replace("': {",":").split(":")
empName2 = metaData2[0].replace("{'","")
#print(empName2)

startE1=[]
endE1=[]
startE2=[]
endE2=[]
freeStE1=[]
freeEndE1=[]
freeStE2=[]
freeEndE2=[]
freeSlotFinal=[]
intervalToPrint1=[]
intervalToPrint2=[]

fillFreeSlots(sEmp1,startE1,endE1,freeStE1,freeEndE1)
fillFreeSlots(sEmp2,startE2,endE2,freeStE2,freeEndE2)

mergeInterval(freeStE1,freeEndE1,freeStE2,freeEndE2)

meetSlot = float(input())  
key = int(meetSlot*60)
converBackTime(freeStE1,freeEndE1,intervalToPrint1)
converBackTime(freeStE2,freeEndE2,intervalToPrint2)

i = 0
flag = 0
while i < len(interValS):
    diff = (interValE[i]-interValS[i])
    if key <= diff:
        hourS = int(interValS[i]/60)
        minutS = int(interValS[i] % 60)
        lastS = amPM(hourS)       
        hourS = minInHour(hourS)       
        if key == diff:
            hourE = int(interValE[i]/60)
            minutE = int(interValE[i] % 60)
            lastE = amPM(hourE)            
            hourE = minInHour(hourE)           
            strSlot = str(hourS) + ":" + str(minutS).zfill(2) + lastS + " - " +  str(hourE) + ":" + str(minutE).zfill(2) + lastE
        else:
            hourE = int((interValS[i] + key)/60)    
            lastE = amPM(hourE)        
            hourE = minInHour(hourE)
            minutE = int((interValS[i] + key)%60)
            strSlot = str(hourS) + ":" + str(minutS).zfill(2) + lastS + " - " +  str(hourE) + ":" + str(minutE).zfill(2) + lastS
        flag = 1           
        break
    i = i + 1


if flag == 0:
    finalSlot = "no slot available"              
else:
    finalSlot = "{" + date + " : ['" + strSlot + "']}"

fOut=open("output.txt","w+")
fOut.write("Available slot\n")
fOut.write(empName1 + ": " + str(intervalToPrint1)+"\n")
fOut.write(empName2 + ": " + str(intervalToPrint2)+"\n\n")
fOut.write("Slot Duration: " + str(meetSlot) + " hour\n")
fOut.write( finalSlot )
fOut.close()