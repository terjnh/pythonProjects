### Task : Given a 2D-array of student names and their scores, calculate the average score of each student, and then find the maximum average score (rounded down to nearest integer - use 'math.floor') among all students. ###


import math

arr = [["Bobby", 65], 
       ["Charles", 90], 
       ["Charles", 30], 
       ["Debbie", 40],
       ["Earle", 40],
       ["Debbie", 100]]

dScores = {}
for i in range(len(arr)):
    if arr[i][0] in dScores:
        dScores.get(arr[i][0]).append(arr[i][1])
    else:
        dScores[arr[i][0]] = [arr[i][1]]

# print(dScores.get(arr[0][0]).append(20))
print(dScores)

## Iterate through dScores to calculate average score of each student
avgList = []
for student, scores in dScores.items():
    individualSum = 0
    for i in scores:
        individualSum += i
    studentAvg = math.floor(individualSum / len(scores))
    avgList.append(studentAvg) 

print("Highest average score: {}".format(max(avgList)))
