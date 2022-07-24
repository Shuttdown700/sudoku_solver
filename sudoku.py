# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 17:33:13 2020

@author: shuttdown
"""
import random
import ast

def createBlankBoard():
    blankBoard = []
    for j in range(9):
        row = []
        for i in range(9):
            row.append("0")
        blankBoard.append(row)
    return blankBoard

#blankBoard = createBlankBoard()

def readRow(board, rowNumber):
    row = ""
    for column in range(9):
        row += str(board[rowNumber-1][column])
    return row

#rowNumber = 1
#row = readRow(easyBoard, rowNumber)

def readColumn(board, columnNumber):
    column = ""
    for row in range(9):
        column += board[row-1][columnNumber-1]
    return column

#columnNumber = 1
#column = readColumn(easyBoard, columnNumber)

def readBlock(board, rowNumber, columnNumber):
#    point = board[rowNumber-1][columnNumber-1]
    rowIndex = rowNumber - 1
    columnIndex = columnNumber - 1
    if 0 <= rowIndex <= 2:
        rowRange = [1,2,3]
    if 3 <= rowIndex <= 5:
        rowRange = [4,5,6]
    if 6 <= rowIndex <= 8:
        rowRange = [7,8,9]
    if 0 <= columnIndex <= 2:
        columnIndexRange = [0,1,2]
    if 3 <= columnIndex <= 5:
        columnIndexRange = [3,4,5]
    if 6 <= columnIndex <= 8:
        columnIndexRange = [6,7,8]
    rowList = []
    for i in range(len(rowRange)):
        row = readRow(board, rowRange[i])
        rowList.append(row)
    cutRowList = []
    for i in range(len(rowList)):
        cutRow = ""
        for j in range(len(rowList[i])):
            if j in columnIndexRange:
                cutRow += rowList[i][j]
        cutRowList.append(cutRow)
    block = []
    blockString = ""
    for i in range(len(cutRowList)):
        chunk = cutRowList[i]
        blockChunk = []
        for j in range(len(chunk)):
            blockChunk.append(chunk[j])
            blockString += chunk[j]
        block.append(blockChunk)
    return block, blockString
    
#rowNumber = 1
#columnNumber  = 2
#block, blockString = readBlock(easyBoard, rowNumber, columnNumber)      

def readBlock_fromCandidateBoard(board, rowNumber, columnNumber):
#    point = board[rowNumber-1][columnNumber-1]
    rowIndex = rowNumber - 1
    columnIndex = columnNumber - 1
    if 0 <= rowIndex <= 2:
        rowRange = [1,2,3]
    if 3 <= rowIndex <= 5:
        rowRange = [4,5,6]
    if 6 <= rowIndex <= 8:
        rowRange = [7,8,9]
    if 0 <= columnIndex <= 2:
        columnIndexRange = [0,1,2]
    if 3 <= columnIndex <= 5:
        columnIndexRange = [3,4,5]
    if 6 <= columnIndex <= 8:
        columnIndexRange = [6,7,8]
    rowList = []
    for i in range(len(rowRange)):
        row = readRow(board, rowRange[i])
        row = row.split("]")
        newRow = []
        for j in range(len(row)):
            modRow = []
            for k in range(len(row[j])):
                if row[j][k] != "'" and row[j][k] != "[" and row[j][k] != "]" and row[j][k] != "," and row[j][k] != " ":
                    modRow.append(row[j][k])
            newRow.append(modRow)
        rowList.append(row)
    cutRowList = []
    for i in range(len(rowList)):
        cutRow = ""
        for j in range(len(rowList[i])):
            if j in columnIndexRange:
                cutRow += rowList[i][j]
        cutRowList.append(cutRow)
    block = []
    blockString = ""
    for i in range(len(cutRowList)):
        chunk = cutRowList[i]
        blockChunk = []
        for j in range(len(chunk)):
            blockChunk.append(chunk[j])
            blockString += chunk[j]
        block.append(blockChunk)
    return block, blockString

def findPossibleSolutions(board, rowNumber, columnNumber):
    point = board[rowNumber-1][columnNumber-1]
    if point != "0":
        possibleSolutions = ['F']
    else:
        numbersList = ["1","2","3","4","5","6","7","8","9"]
        spentNumbers = []
        block, blockString = readBlock(board, rowNumber, columnNumber)   
        column = readColumn(board, columnNumber)
        row = readRow(board, rowNumber)
        for i in range(9):
            if row[i] not in spentNumbers and row[i] != "0":
                spentNumbers.append(row[i])
            if column[i] not in spentNumbers and column[i] != "0":
                spentNumbers.append(column[i])
            if blockString[i] not in spentNumbers and blockString[i] != "0":
                spentNumbers.append(blockString[i])
        spentNumbers.sort()
        possibleSolutions = []
        for i in range(9):
            if numbersList[i] not in spentNumbers:
                possibleSolutions.append(numbersList[i])
    return possibleSolutions
        
#rowNumber = 1
#columnNumber  = 2      
#possibleSolutions = findPossibleSolutions(easyBoard, rowNumber, columnNumber)                  

def inputNewValuesIntoBoard(board, value, rowNumber, columnNumber):
    rowIndex = rowNumber - 1
    columnIndex = columnNumber - 1
    board[rowIndex][columnIndex] = value
    return board

    
def createPossibleSolutionsBoard(board):
    candidateBoard = createBlankBoard()
    for rowNumber in range(1,10):
        for columnNumber in range(1,10):
            possibleSolutions = findPossibleSolutions(board, rowNumber, columnNumber)                  
            candidateBoard = inputNewValuesIntoBoard(candidateBoard, possibleSolutions, rowNumber, columnNumber)
    return candidateBoard

def readCandidateColumn(candidateBoard, columnNumber):
    columnIndex = columnNumber - 1
    candidateColumn = []
    for i in range(9):
        for j in range(9):
            if j == columnIndex:
                candidateColumn.append(candidateBoard[i][j])
    return candidateColumn

def readCandidateRow(candidateBoard, rowNumber):
    rowIndex = rowNumber - 1
    candidateRow = []
    for i in range(9):
        for j in range(9):
            if i == rowIndex:
                candidateRow.append(candidateBoard[i][j])
    return candidateRow

def determineBlock(rowNumber, columnNumber):
    if 1 <= rowNumber <= 3:
        rowCode = "a"
    if 4 <= rowNumber <= 6:
        rowCode = "b"    
    if 7 <= rowNumber <= 9:
        rowCode = "c"
    if 1 <= columnNumber <= 3:
        columnCode = "a"
    if 4 <= columnNumber <= 6:
        columnCode = "b"    
    if 7 <= columnNumber <= 9:
        columnCode = "c"
    combo = rowCode+columnCode
    if combo == "aa":
        rowIndex = [0,1,2]
        columnIndex = [0,1,2]
    if combo == "ab":
        rowIndex = [0,1,2]
        columnIndex = [3,4,5]
    if combo == "ac":
        rowIndex = [0,1,2]
        columnIndex = [6,7,8]
    if combo == "ba":
        rowIndex = [3,4,5]
        columnIndex = [0,1,2]
    if combo == "bb":
        rowIndex = [3,4,5]
        columnIndex = [3,4,5]
    if combo == "bc":
        rowIndex = [3,4,5]
        columnIndex = [6,7,8]
    if combo == "ca":
        rowIndex = [6,7,8]
        columnIndex = [0,1,2]
    if combo == "cb":
        rowIndex = [6,7,8]
        columnIndex = [3,4,5]
    if combo == "cc":
        rowIndex = [6,7,8]
        columnIndex = [6,7,8]
    return rowIndex, columnIndex

def readCandidateBlock(candidateBoard, rowIndexRange, columnIndexRange):
    candidateBlock = []
    for i in range(9):
        for j in range(9):
            if i in rowIndexRange and j in columnIndexRange:
               candidateBlock.append(candidateBoard[i][j])
    return candidateBlock


def findSingluarSolutions(candidateBoard, rowNumber, columnNumber):
    rowIndex = rowNumber - 1
    columnIndex = columnNumber - 1
    point = candidateBoard[rowIndex][columnIndex]
    if point[0] != 'F':
        candidateRow = readCandidateRow(candidateBoard, rowNumber)
        candidateColumn = readCandidateColumn(candidateBoard, columnNumber)
        rowIndexRange, columnIndexRange = determineBlock(rowNumber, columnNumber)
        candidateBlock = readCandidateBlock(candidateBoard, rowIndexRange, columnIndexRange)
        rowCandidates = []
        solution = "None"
        for i in range(len(candidateRow)):
            for j in range(len(candidateRow[i])):
                if candidateRow[i][j] not in rowCandidates and i != columnIndex and candidateRow[i][j] !='F':
                    rowCandidates.append(candidateRow[i][j])
        for i in range(len(point)):
            if point[i] not in rowCandidates:
                solution = point[i]                   
        if solution == "None":
            columnCandidates = []
            for i in range(len(candidateColumn)):
                for j in range(len(candidateColumn[i])):
                    if candidateColumn[i][j] not in columnCandidates and i != rowIndex and candidateColumn[i][j] !='F':
                        columnCandidates.append(candidateColumn[i][j])
            for i in range(len(point)):
                if point[i] not in columnCandidates:
                    solution = point[i]
        if solution == "None":
            repeatTracker = 0
            blockCandidates = []
            for i in range(len(candidateBlock)):
                if candidateBlock[i] == point:
                    repeatTracker += 1
                else:
                    for j in range(len(candidateBlock[i])):
                        if candidateBlock[i][j] not in blockCandidates and candidateBlock[i][j] !='F':
                            blockCandidates.append(candidateBlock[i][j])
            if repeatTracker > 1:
                solution = "None"
            else:
                for i in range(len(point)):
                    if point[i] not in blockCandidates:
                        solution = point[i]
    else:
        solution = 'F'
    return solution

def inputSolution(board, solution, rowNumber, columnNumber):
    rowIndex = rowNumber - 1
    columnIndex = columnNumber - 1
    board[rowIndex][columnIndex] = solution
    return board

def makeGuess(candidateBoard):
    candidateList = []
    indexList = []
    for i in range(len(candidateBoard)):
        for j in range(len(candidateBoard[i])):
            if candidateBoard[i][j] != ['F']:
                candidateList.append(candidateBoard[i][j])
                indexList.append([i,j])
    randomIndex = random.randint(0,len(candidateList)-1)
    randomCandidate = candidateList[randomIndex]
    index = indexList[randomIndex]
    guess = randomCandidate[random.randint(0,len(randomCandidate)-1)]
    rowNumber = index[0] + 1
    columnNumber = index[1] + 1
    return guess, rowNumber, columnNumber

def checkInvalid(candidateBoard):
    invalid = False
    for i in range(len(candidateBoard)):
        for j in range(len(candidateBoard[i])):
            if len(candidateBoard[i][j]) == 0:
                invalid = True
    return invalid

def solveSudoku(board):
    print("Starting solver...")
    check = "Bad"
    og_board_string = str(board)
    while check == "Bad":
    #    board = hardestBoard
        solutionCount = 0
        runCycles = 0
        consecRunCycles = 0
        while solutionCount < 81 and consecRunCycles < 30:
            candidateBoard = createPossibleSolutionsBoard(board)
            invalid = checkInvalid(candidateBoard)
            if invalid == True:
                print("Invalid -- Restarting Path")
                board = ast.literal_eval(og_board_string)
                candidateBoard = createPossibleSolutionsBoard(board)
                consecRunCycles = 0
            lastSolutionCount = solutionCount
            runCycles += 1
            solutionCount = 0
            for rowNumber in range(1,10):
                for columnNumber in range(1,10):
                    solution = findSingluarSolutions(candidateBoard, rowNumber, columnNumber)
                    if solution == 'F':
                        solutionCount += 1
                    if solution != 'F' and solution != 'None':
                        board = inputSolution(board, solution, rowNumber, columnNumber)
                        consecRunCycles = 0
            if lastSolutionCount == solutionCount:
                guess, rowNumber, columnNumber = makeGuess(candidateBoard)
                board = inputSolution(board, guess, rowNumber, columnNumber)
                candidateBoard = createPossibleSolutionsBoard(board)
                consecRunCycles += 1
                print("Stall met -- Guess Made")
            print("{} % complete".format(float(round((solutionCount/81)*100,2))))
        check = checkCorrectness(board)
        if check == "Bad":
            board = ast.literal_eval(og_board_string)
#    print("The solved board")
#    print(board)
    return board

def checkCorrectness(finishedBoard):
    checkCounter = 0
    for rowNumber in range(1,10):
        for columnNumber in range(1,10):
            row = readRow(finishedBoard, rowNumber)
            rowList = list(row)
            rowList.sort()
            column = readColumn(finishedBoard, columnNumber)
            columnList = list(column)
            columnList.sort()
            block, blockString = readBlock(finishedBoard, rowNumber, columnNumber)
            blockStringList = list(blockString)
            blockStringList.sort()
            if rowList == columnList == blockStringList == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                checkCounter += 1
            else:
                pass
#                print("Error at row {}, column {}".format(rowNumber,columnNumber))
    if checkCounter == 81:
        print("Board is verified to be correct!")
        check = "Good"
    else:
        print("Board is not verified. An error may be present...")
        check = "Bad"
    return check

easyBoard = [["0","0","9","0","3","2","0","8","5"],
             ["5","3","8","0","6","4","0","0","9"],
             ["1","6","2","0","9","0","0","3","0"],
             ["0","0","3","0","2","7","0","0","0"],
             ["0","5","4","6","0","0","1","0","0"],
             ["6","0","7","0","1","5","3","4","0"],
             ["3","0","0","8","0","1","9","0","6"],
             ["7","0","0","3","0","0","8","5","0"],
             ["0","9","1","0","0","0","4","7","0"]]

mediumBoard = [["8","0","0","1","3","5","0","7","0"],
               ["0","2","0","0","4","0","8","3","0"],
               ["0","6","0","7","0","8","0","4","0"],
               ["0","0","0","4","7","0","9","0","8"],
               ["2","4","0","0","8","0","0","0","0"],
               ["0","3","8","0","0","0","0","0","5"],
               ["0","8","0","6","0","4","1","0","0"],
               ["9","0","0","0","0","7","2","0","4"],
               ["0","0","5","8","1","0","0","0","6"]]

hardBoard = [["4","0","5","0","7","0","0","2","0"],
             ["2","7","0","0","0","0","1","0","8"],
             ["0","0","0","2","0","0","3","0","0"],
             ["0","0","7","0","0","5","2","0","3"],
             ["1","9","0","0","0","0","8","0","5"],
             ["0","0","0","6","0","0","0","9","0"],
             ["0","4","0","0","0","2","0","0","0"],
             ["0","1","0","0","9","0","4","3","7"],
             ["3","0","0","0","0","4","0","1","2"]]

expertBoard = [["5","0","0","9","0","0","6","0","0"],
               ["0","0","9","2","0","0","8","3","0"],
               ["0","0","0","0","1","0","0","4","0"],
               ["0","9","6","0","0","2","0","0","0"],
               ["0","0","0","0","0","6","0","8","4"],
               ["0","1","0","0","0","5","3","0","6"],
               ["0","6","2","0","7","0","0","0","5"],
               ["3","0","0","5","0","0","0","2","0"],
               ["0","0","0","0","0","0","0","0","0"]]

hardestBoard = [["8","0","0","0","0","0","0","0","0"],
                ["0","0","3","6","0","0","0","0","0"],
                ["0","7","0","0","9","0","2","0","0"],
                ["0","5","0","0","0","7","0","0","0"],
                ["0","0","0","0","4","5","7","0","0"],
                ["0","0","0","1","0","0","0","3","0"],
                ["0","0","1","0","0","0","0","6","8"],
                ["0","0","8","5","0","0","0","1","0"],
                ["0","9","0","0","0","0","4","0","0"]]

#finishedBoard = solveSudoku(hardBoard)
    

    
    
                
                

                
                
    
            
    
    