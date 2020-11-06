import json
fd = open("org.json") 
tree = json.load(fd) 
fd.close()

userInput = input().split(" ")
searchParent = []
noOfEmpSearch = (int)(userInput[0])
i = 1
while i<=noOfEmpSearch:
    searchParent.append(userInput[i]) 
    i = i + 1  
levelList=[]

def makeParentList(parentList,toFind):
    check =0
    flag = 0
    complete=0
    length = len(tree)-1
    while length >= 0:
        tempList = tree[('L'+ str(length))]
        check = 0
        for node in tempList:
            if node["name"]==toFind:
                parentList.append(toFind)
                if flag==0:
                    flag = 1
                    levelList.append(length)
                if node.get("parent")!= None:
                    toFind = node["parent"]
                else:
                    complete = 1
                check = 1
                break
        if complete == 1:
            break
        length = length - 1
#print(levelList)
def fun1(leader):
    for i in range(0,len(tree)):
        tempList = tree[('L'+ str(i))]
        for node in tempList:
            if node["name"]==leader:
                return i
            
                
#Driver code
parentList = []
for spT in searchParent:
    tempList = []
    makeParentList(tempList,spT)
    parentList.append(tempList)   

levelLeader=0
flag=0
leader=" "

for i in range(1,len(parentList[0])):
    count = 0
    for j in range(1,len(parentList)):
        if parentList[0][i] in parentList[j] and parentList[0][i] != parentList[j][0]:
            count = count + 1
            if(count == noOfEmpSearch-1):
                leader = parentList[0][i]
                flag = 1
                break
    if flag == 1:
        break

levelLeader=fun1(leader)

if flag==1:    
    print(leader)        
    for i in range(0,noOfEmpSearch):
        print(leader+" is "+ str(levelList[i]-levelLeader) +" levels above "+searchParent[i])
else:
    print("leader not found!")