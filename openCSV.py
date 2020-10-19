# Programa deve contemplar no mínimo:
# - leitura de arquivos .csv, com um configuração inicial do "Tabuleiro"; (exemplo em anexo: sudoku_E1.csv
# - Mostrar se tiver uma ou mais soluções para a configuração inicial;
#     + tentar todas as possibilidades.
# - Tempo que levou para encontrar a solução.
#
# 0,8,0,0,0,0,9,0,0
# 0,7,5,3,6,0,0,8,0
# 0,0,0,0,4,0,0,0,0
# 6,5,0,0,0,2,3,0,0
# 0,0,0,4,5,0,0,0,0
# 2,0,9,0,0,0,0,0,0
# 0,0,0,0,0,7,5,0,0
# 0,0,0,0,1,3,6,0,0
# 1,0,0,0,0,0,0,0,2
import csv
import time
start_time = time.time()  # start timer to measure run time

with open("sudoku.csv") as f:
    s = f.read()  # add trailing new line character
stringSDK = (repr(s.replace("\n", ",")))
repr(stringSDK.replace(",", ""))

# Forming the Puzzle Grid


def form_grid(stringSDK):
    global grid
    print('Problema original')
    for i in range(0, len(stringSDK), 9):
        row = stringSDK[i:i+9]
        temp = []
        for block in row:
            temp.append(int(block))
        grid.append(temp)
    printGrid()

# Function to print the grid


def printGrid():
    global grid
    for row in grid:
        print(row)

# Function to check if a digit can be placed in the given block


def possible(row, col, digit):
    global grid
    for i in range(0, 9):
        if grid[row][i] == digit:
            return False
    for i in range(0, 9):
        if grid[i][col] == digit:
            return False
    square_row = (row//3)*3
    square_col = (col//3)*3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[square_row+i][square_col+j] == digit:
                return False
    return True


def solve():
    global grid
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for digit in range(1, 10):
                    if possible(row, col, digit):
                        grid[row][col] = digit
                        solve()
                        grid[row][col] = 0  # Backtrack step
                return
    print('\nProblema resolvido')
    printGrid()


stringSDK = "000090000762000000000800300000009200030000007804005001100000070000100004290007005"
grid = []
form_grid(stringSDK)
solve()
print("Tempo de execução: %s segundos" % (time.time() - start_time))
