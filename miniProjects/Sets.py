######################################### Task ################################################
# You have a non-empty set, and you have to execute commands given in lines.
# The commands will be pop, remove and discard. 


####################################  Input Format  #########################################

# The first line contains integer n
# , the number of elements in the set s.
# The second line contains n space separated elements of set s. All of the elements are non-negative integers, less than or equal to 9.
# The third line contains integer N, the number of commands.
# The next N lines contains either pop, remove and/or discard commands followed by their associated value.

setSize = int(input())
strInput = input()

inputList = []
inputList = strInput.split(" ")
for i in range(0, len(inputList)):
    inputList[i] = int(inputList[i])

s = set()
s = set(inputList)

commandNum = int(input())
commandList = []

for j in range(0, commandNum):
    commands = input()
    commandList.append(commands)

for i in range(0, commandNum):
    if commandList[i].startswith('p'):
        s.pop()
    if commandList[i].startswith('r'):
        removeComm = commandList[i].split(" ")
        removeComm[1] = int(removeComm[1])
        s.remove(removeComm[1])
    if commandList[i].startswith('d'):
        discardComm = commandList[i].split(" ")
        discardComm[1] = int(discardComm[1])
        s.discard(discardComm[1])

sumS = sum(s)

print(sumS)


    