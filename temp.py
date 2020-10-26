import json
fd = open("org.json") 
tree = json.load(fd) 
fd.close()
searchParent1 = input()
searchParent2 = input()

def updateNameToId():
    ID = int("001")
    length = len(tree)-1
    i = 0
    while i <= length:
        tempList = tree[('L'+ str(i))]
        for node in tempList:
            node["name"]=ID
            ID = ID + 1
        i = i + 1


def makeParentList(parentList,toFind):
    check =0
    complete=0
    length = len(tree)-1
    while length >= 0:
        tempList = tree[('L'+ str(length))]
        check = 0
        for node in tempList:
            if node["name"]==toFind:
                parentList.append(toFind)
                if node.get("parent")!= None:
                    toFind = node["parent"]
                else:
                    complete = 1
                check = 1
                break
        if complete == 1:
            break
        length = length - 1

#Driver code
parentList1 = []
parentList2 = []

updateNameToId()
makeParentList(parentList1,searchParent1)
makeParentList(parentList2,searchParent2)

flag = 0
i = 0
for pInL1 in parentList1:
    if i==0:
        i = i + 1
        continue
    j = 0
    for pInL2 in parentList2:
        if j == 0:
            j = j + 1
            continue
        if pInL1==pInL2:
            flag=1
            break
        j = j + 1
    if(flag==1):
        break
    i = i + 1

if(flag==0):
    print("No Leader Found")
else:
    print(pInL1)
    OpForE1 = pInL1 + " is " + str(i) + " levels above " + searchParent1
    OpForE2 = pInL2 + " is " + str(j) + " levels above " + searchParent2
    print(OpForE1)
    print(OpForE2)