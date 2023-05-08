import collections
class Solution:
    def matrixReshape(self, mat, r, c):
            if len(mat) == 0 or r*c != len(mat)*len(mat[0]):
                return mat
            res = [[None for _ in range(c)] for _ in range(r)]
            q = collections.deque()
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    q.append(mat[i][j])
            for i in range(r):
                for j in range(c):
                    res[i][j] = q.popleft()
            return res


if __name__ == '__main__':
    mat = [[1,2],[3,4]]
    r = 1
    c = 4
    expected_output = [[1,2,3,4]]

    test = Solution()
    assert(test.matrixReshape(mat,r,c) == expected_output)