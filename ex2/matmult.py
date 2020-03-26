# Program to multiply two matrices using nested loops


import random

N = 250




def create_matrix(N):
    # NxN matrix
    X = []
    for i in range(N):
        X.append([random.randint(0,100) for r in range(N)])

    return X



def create_larger_matrix(N):
    # Nx(N+1) matrix
    Y = []
    for i in range(N):
        Y.append([random.randint(0,100) for r in range(N+1)])

    return Y



def create_empty_matrix(N):
    # result is Nx(N+1)
    result = []
    for i in range(N):
        result.append([0] * (N+1))
    return result




def multiply_matrices(X,Y, result):
    # iterate through rows of X
    for i in range(len(X)):
        # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]

    return result



def print_matrix(result):
    for r in result:
        print(r)



def __main__(N):
    X= create_matrix(N)
    Y= create_larger_matrix(N)
    result = create_empty_matrix(N)
    result= multiply_matrices(X,Y, result)
    print_matrix(result)


# call main program 
__main__(N)





