from operator import itemgetter

if __name__ == '__main__':

    students = []
    inputNum = int(input())

    for i in range(inputNum):
        name = input()
        score = float(input())
        students.append([name, score])


    # sort students alphabetically
    students.sort(key=lambda x: x[0])

    # print(students)

    # sort students by score
    students.sort(key=lambda x: x[1], reverse=True)
    # print(students)

    lowestScore = 1000000000.0
    secondLowest = 1000000000.0
    for i in range(0, len(students), 1):
        if(students[i][1] < lowestScore):
            lowestScore = students[i][1]
    
    students.sort(key=lambda x: x[1])
    for i in range(0, len(students), 1):
        if(students[i][1] > lowestScore):
            secondLowest = students[i][1]
            break


    listSecondLowest = []
    for i in range(0, len(students), 1):
        if(students[i][1] == secondLowest):
            listSecondLowest.append(students[i][0])

    print(listSecondLowest)
    listSecondLowest.sort(key=lambda x: x[0])

    for i in range(0, len(listSecondLowest), 1):
        print(listSecondLowest[i])




    