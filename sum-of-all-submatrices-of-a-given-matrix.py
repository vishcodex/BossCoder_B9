# Given a NxN 2-D matrix, the task to find the sum of all the submatrices.

n = 3

def matrixSum(arr) :
    sum = 0

    for i in range(n):
        for j in range(n):
            top_left = (i + 1) * (j + 1)
            print(top_left)
            bottom_right = (n - i) * (n - j)
            print(f"top_left : {top_left}, bottom right : {bottom_right}")
            sum += (top_left * bottom_right *
                                  arr[i][j])
    return sum







if __name__ == "__main__" :
    arr = [[ 1, 1, 1 ],
           [ 1, 1, 1 ],
           [ 1, 1, 1 ]];
 
    print(matrixSum(arr))