from random import randint

def diagonal_differnece(arr):
    n_columns = len(arr[0])
    p = 0
    s = 0

    # Sum the elements of the primary diagonal
    for i in range (n_columns):
        p += arr[i][i]

    # Sum the elements of the secondary diagonal 
    for i in range(n_columns, 0, -1):
        s += arr[i-1][n_columns-i]   
    
    # Difference between the sums of primary and secondary diagonal 
    A = p - s
    return abs(A)

if __name__ == "__main__":
    n_columns= 3
    n_lines= 3
    arr = []

    for i in range(n_lines):
        line =[]
        for j in range(n_columns):
            n = randint(0,10)
            line.append(n)
        arr.append(line)

    print(diagonal_differnece(arr))