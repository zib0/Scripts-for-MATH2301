'''
Author: Zibo Wang
License: BY-NC-SA-4.0
Warshall's algorithm is a faster way to compute transitive closure Runs in O(n^3).
'''

import numpy as np


'''
Using Warshall's algorithm to find transitive closure of a matrix.
@param m: zero-one nxn matrix(adjacency matrix)
@return: the transitive closure of m
'''


def warshall(m):
    n = m.shape[0]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                m[i][j] = m[i][j] or (m[i][k] and m[k][j])
    return m


if __name__ == "__main__":

    # Please edit your adjacency matrix here.
    adj_mtx = np.array([[0, 1, 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1],
                        [0, 0, 1, 0]])

    print("The transitive closure is:")
    print(np.array_str(warshall(adj_mtx)))