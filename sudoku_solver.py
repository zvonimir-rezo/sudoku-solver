
class Sudoku:
    def __init__(self, matrix, solution=None):
        self.matrix = matrix
        self.solution = solution

    def print_nicely_and_return(self):
        for i in self.matrix:
            print(i)
        print()
        return self.matrix

    def is_possible(self, row, col, n):
        for i in range(9):
            if self.matrix[row][i] == n or self.matrix[i][col] == n:
                return False
        square_x = row // 3 * 3
        square_y = col // 3 * 3
        for i in range(square_x, square_x + 3):
            for j in range(square_y, square_y + 3):
                if self.matrix[i][j] == n:
                    return False
        return True

    def backtrack(self):
        for i in range(9):
            for j in range(9):
                if self.matrix[i][j] == 0:
                    for n in range(1, 10):
                        if self.is_possible(i, j, n):
                            self.matrix[i][j] = n
                            if not self.backtrack():
                                self.matrix[i][j] = 0
                            else:
                                return True
                    return False
        self.solution = self.print_nicely_and_return()
        return True
