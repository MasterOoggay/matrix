from copy import deepcopy

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.matrix = self.matrixFormatieren()
        self.solutions = []

    def AddRows(self, row1, row2, position):
        """row 1 - row 2 results in new row 2 with given position equals zero \n
            x = row1[position]/row2[position] \n
            II new = I - II*x"""
        row1, row2 = self.matrix[row1], self.matrix[row2]

        #if the position is 0 already, do not proceed
        if row2[position-1] != 0.0:
            #get factor
            num = row1[position-1]/row2[position-1]

            #multiply rows with faktor and then subtract
            for i in range(0, len(row2)):
                row2[i] = row1[i] - row2[i]*num

        return row2

    def DiagonalMatrix(self):
        """Converts the matrix into a diagonal matrix with every number under the main diagonal equals zero"""
        new_matrix = deepcopy(self.matrix)
        for i in range(0, len(new_matrix)):
            for num in range(i+1, len(new_matrix)):
                if new_matrix[num][i] != 0.0:
                    new_matrix[num] = self.AddRows(i, num, i+1)

        for i in range(len(new_matrix)):
            pass

        return new_matrix

    def SolveMatrix(self):
        """Solves the matrix using the Gauss Algorithm, prints solutions and returns solutions in list"""
        new_matrix = self.DiagonalMatrix()
        solutions = []

        for i in range(0, len(new_matrix)):
            copy_matrix = deepcopy(new_matrix)
            solution = copy_matrix[-1-i][-2-i]
            del copy_matrix[-1-i][-2-i]
            for j in range(0, len(copy_matrix[-1-i])-1):
                copy_matrix[-1-i][-1] -= copy_matrix[-1-i][j]
            solution_other_side = copy_matrix[-1-i][-1]
            solutions.insert(0, round(solution_other_side/solution, 3))

            for row in new_matrix:
                row[-2-i] = row[-2-i]*solutions[0]
        
        self.solutions = solutions

        for i in range(len(solutions)):
            print(f"x{i+1} = {solutions[i]}")

        return solutions

    def matrixFormatieren(self):
        """Macht alle Zahlen in der Matrix zu floats"""
        matrix = []
        for item in self.matrix:
            matrix.append([round(float(i), 4) for i in item])

        return matrix
