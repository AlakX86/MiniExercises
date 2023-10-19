# Dada una lista de lista representando una matriz n*n:
# Define una rutina que devuelve True si la entrada es una matriz indentidad
# y False en otro caso.

# Una matriz identidad es una matriz cuadrada en la que todos los elementos
# en la diagonal principal son 1 y el resto de elementos fuera de la
# diagonal principal son 0. 
# (Una matriz cuadrada es una matriz con el numero de filas
# igual al numero de columnas)
def check_square(matrix):
    num_rows = len(matrix)
    for row in matrix:
        if len(row) != num_rows:
            return False
    return True

def is_identity_matrix(matrix):
    assert check_square(matrix) == True, "Must be square"
    for row in range(len(matrix)):
        for num in range(len(matrix)):
            if matrix[row][num] != 0 and matrix[row][num] != 1:
                return False
            if matrix[row][row] == 1:
                continue
            elif matrix[row][num] == 0 and matrix[row].count(1) == 1:
                continue
            else:
                return False
    return True



# Casos test:

matrix1 = [[1,0,0,0],
           [0,1,0,0],
           [0,0,1,0],
           [0,0,0,1]]
print(is_identity_matrix(matrix1))
#>>>True

matrix2 = [[1,0,0],
           [0,1,0],
           [0,0,0]]

print(is_identity_matrix(matrix2))
#>>>False

matrix3 = [[2,0,0],
           [0,2,0],
           [0,0,2]]
print(is_identity_matrix(matrix3))

#>>>False


matrix4 = [[0,1,0,0],
            [0,0,1,0],
            [0,0,0,1],
            [1,0,0,0]]
print(is_identity_matrix(matrix4))

#>>>False

matrix6 = [[1,0,0,0],  
           [0,1,0,2],  
           [0,0,1,0],  
           [0,0,0,1]]

print(is_identity_matrix(matrix6))
#>>>False

matrix7 = [[1, -1, 1],
           [0, 1, 0],
           [0, 0, 1]]
print(is_identity_matrix(matrix7))
#>>>False           


# casos test que no satisfacen la precondicion de que la matriz sea cuadrada (assert):

matrix4 = [[1,0,0,0],
           [0,1,1,0],
           [0,0,0,1]]

#print(is_identity_matrix(matrix4))
#>>>False

matrix5 = [[1,0,0,0,0,0,0,0,0]]

#print(is_identity_matrix(matrix5))
#>>>False           