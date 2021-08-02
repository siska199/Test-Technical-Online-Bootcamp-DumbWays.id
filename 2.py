"""
Program transpose matriks
"""
import numpy as np
def arr_trans(mul_arr):
    arrMul_new = np.zeros((len(arr[1]),len(arr)))
    for i in range(len(arr[1])):
        for j in range(len(arr)):
            arrMul_new[i][j] = arr[j][i]
    return (arrMul_new)

arr = [[2,3,4],
        [4,5,6],
        [7,8,9],
        [1,2,3],
        [5,6,7]]

print("Array sebelum di transpose: {}".format(arr))
print("Array setelah di transpose: {}".format(arr_trans(arr)))
