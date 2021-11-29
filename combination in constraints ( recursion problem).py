
def findAllCombinations(A, x, n):
    if x > n:
        print(A)
        return
    for i in range(2*n):
        if A[i] == -1 and (i + x + 1) < 2*n and A[i + x + 1] == -1:
            A[i] = x
            A[i + x + 1] = x
            findAllCombinations(A, x + 1, n)
            A[i] = -1
            A[i + x + 1] = -1
 
if __name__ == '__main__':
 
    # given 