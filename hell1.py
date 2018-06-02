def isSquare(A):
    return len(A)==len(A[0])

def isDiagonal(A):
    zero = '0'
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(i,j,A[i][j])
            if i!=j:
                print(1)
                if A[i][j]!=zero:
                    print(2)
                    return False
    return True

def isToeplitz(A):
# Check that given matrix is Toeplitz.
# Toeplitz matrix is a matrix with a(i,j)=a(i+1,j+1)
# A Toeplitz matrix is not necessarily square.
    for i in range(len(A)-1):
        for j in range(len(A[0])-1):
            if A[i][j] != A[i+1][j+1]:
                return False
    return True

def isHankel(A):
# Check that given matrix is Hankel.
# Hankel matrix is a matrix with a(i,j)=a(i-1,j-1)
# A Hankel matrix is square matrix.
    if not isSquare(A): return False
    for i in range(2, len(A)):
        for j in range(len(A[0])-1):
            if A[i][j] != A[i-1][j+1]:
                return False
    return True
    return 0 

def getMatrix():
# Read matrix from stdin
# Matrix format: first two rows - number of rows and number of collums
# Next rows is a matrix rows. Delimiter is a space symbol
# stdin data example of 2x3 matrix:
##    2
##    3
##    1 2 3
##    2 3 4

    n = input() # read rows number
    m = input() # read collums number
    ## !!! Check that it is int, than convert it to int
    n = int(n)
    m = int(m)

    A = [0] * n  # initialize matrix rows with zeros 

    for i in range(n): # read matrix
        A[i] = input().split()
        
    return A

def matrixToPrint(A):
# print matrix to stdout
    str = ""
    for i in range(len(A)):
        for j in range(len(A[0])):
            str
            print(A[i][j]+" ", end='')
        print()
    return 0

AA = getMatrix()
print("Matrix: \n",  matrixToPrint(AA))
print("square: ", isSquare(AA))
print("Toeplitz: ", isToeplitz(AA))
print("Hankel: ", isHankel(AA))
print("Diagonal: ", isDiagonal(AA))
for i in range(10):
    print(i)

