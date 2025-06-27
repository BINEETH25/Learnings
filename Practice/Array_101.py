class Matrix:
    def __init__(self):
        pass # No need to store rows and cols, because we are not using them again
        
    def mat(self, rows, cols):
        
        Matrix_1 = [[0 for i in range(cols)] for j in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                Matrix_1[i][j] = i * cols + j + i
        
        return Matrix_1

math = Matrix()
print(math.mat(3,4))

