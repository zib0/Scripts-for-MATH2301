'''
Author: Zibo Wang
License: BY-NC-SA-4.0
This file is for counting number of paths of length l from f to t.
'''

import numpy as np

'''
@param m: the input adjacency matrix that you are using
@param l: the length of path you are looking for
@param f: the vertex from
@param t: the vertex to
@return the number of paths of length l from f to t.
'''
def count_paths(m, l, f, t):
    result = np.linalg.matrix_power(m, l)
    return result[f-1][t-1]


if __name__ == "__main__":
    # Please edit your adjacency matrix here.
    adj_mtx = ([0,1,0,0],
               [0,0,1,0],
               [0,0,0,1],
               [0,0,1,0])

    print(count_paths(adj_mtx, 2, 1, 3))