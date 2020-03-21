# This code allows the user to input 2 integers at the start (to specify the dimensions of a door mat)
# Mat size must be N x M (N is an odd natural number, and M is 3 times N)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |.- characters
#
# Based on the user input, 1st integer is the number of rows, and 2nd integer is the number of columns


if __name__ == '__main__':
    rowsCol = input()
    rowStr, colStr = rowsCol.split()
    rows = int(rowStr)
    cols = int(colStr)

    matRow = ""
    matList = []

    for i in range(rows):
        # print(matRow + "\n")
        matRow = ""
        for j in range(cols):
            matRow += '-'
        matList.append(matRow)

    # print(matList)

    # WELCOME row
    welcomeRow = int(rows/2)
    welcomeIndex = int((cols/2) - 3)
    matList[welcomeRow] = matList[welcomeRow][:welcomeIndex] + "WELCOME" + matList[welcomeRow][:(welcomeIndex)]

    # Modular Logo
    modLogo = ".|." 
    midRow = int(rows/2)
    # print(midRow)

    # print(len(modLogo))
    for i in range(0, midRow, 1):
        numModLogo = i + (i + 1)
        matList[i] = modLogo * numModLogo

    for i in range(0, midRow, 1):
        matList[i] = matList[i].center(cols, "-")

    # matList[0] = matList[0].center(cols, "-")
    # matList[1] = matList[1].center(cols, "-")
    # matList[2] = matList[2].center(cols, "-")

    for j in range((midRow + 1), rows, 1):
        matList[j] = matList[rows-j-1]

    # matList[4] = matList[2]
    # matList[5] = matList[1]
    # matList[6] = matList[0]

    for i in range(0, len(matList), 1):
        print(matList[i])
