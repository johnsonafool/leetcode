from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        # find primary diagonal first
        p = 0
        s = 0
        for i in range(len(mat)):
            v = mat[i][i]
            p += v

        # find sec diagonal
        i = 1
        for j in range(len(mat)):
            # check for the index
            if len(mat) - i == j:
                i += 1
                continue
            v = mat[len(mat) - i][j]
            s += v
            i += 1

        return p + s
