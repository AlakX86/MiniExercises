# Define una rutina que devuelve True si una matrix es
# atisimetrica y False en otro caso. 
# Una matrix n*n es antisimetrica si se verifica que 
# sus elementos mantienen la relación:
# matrix[row][num] = - matrix[num][row] 
# para cada row=0,1,...,n-1 y para cada num=0,1,...,n-1.
def check_square(matrix):
    num_rows = len(matrix)
    for row in matrix:
        if len(row) != num_rows:
            return False
    return True

def is_antisimetric_matrix(matrix):
    assert check_square(matrix) == True, "Must be square"
    for row in range(len(matrix)):
        for num in range(len(matrix)):
            if matrix[row][num] != -matrix[num][row]:
                return False
            else:
                continue
    return True

# Casos Test:

print(is_antisimetric_matrix([[0, 1, 2], 
                     [-1, 0, 3], 
                     [-2, -3, 0]]))
#>>> True

print(is_antisimetric_matrix([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]))
#>>> True

print(is_antisimetric_matrix([[0, 1, 2], 
                     [-1, 0, -2], 
                     [2, 2,  3]]))
#>>> False

print(is_antisimetric_matrix([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]]))
#>>> False

# casos test que no satisfacen la precondicion de que la matrix sea cuadrada (assert)

matriz4 = [[1,0,0,0],
           [0,1,1,0],
           [0,0,0,1]]

#print(is_antisimetric_matrix(matriz4))
#>>>False

matriz5 = [[1,0,0,0,0,0,0,0,0]]

#print(is_antisimetric_matrix(matriz5))
#>>>False 