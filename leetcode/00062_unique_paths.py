"""
https://leetcode.com/problems/unique-paths/
"""
import unittest
class Solution:
    """
    I began to do this by creating a matrix of m and n. Every number indicates
    the amount of possible moves with current values of m and n, for example
    3 possible moves when m=2 and n=3.
    What I did here was that I calculated the first values by hand.
    Then I realized that there is a pattern:
    1 1 1 1
    1 2 3 4
    1 3 6
    1 4
    So the value in point m,n can be calculated by summing m-1,n and m,n-1.
    I calculate a full square matrix based on the bigger value between m and n,
    and return the value from the coordinate if it is already calculated.
    This approach is nasty as hell, but my goal was to do it without any help
    from anywhere, and that I did. It's not the prettiest, fastest or most
    efficient, but it's my own beloved baby.
    """
    def uniquePaths(self, m: int, n: int) -> int:
        # m or n being 1 results in just one possible path
        if m == 1 or n == 1:
            return 1
        if m == 2:
            return n
        if n == 2:
            return m
        bigger = max(m,n)
        matrix = [[0]*bigger for _ in range(bigger)]

        for i in range(0, bigger):
            for j in range(0, bigger):
                # only change values if they haven't been changed before
                if matrix[i][j] == 0:
                    if i == 0 or j==0:
                        matrix[i][j] = 1
                    if j == 1:
                        matrix[i][j] = i+1
                    if i == 1:
                        matrix[i][j] = j+1
                # when the first row of 1's is doone, we can begin to calculate
                # the rest
                if (j >= 1) and (i >= 1):
                    matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
            try:
                if matrix[m-1][n-1] != 0:
                    return matrix[m-1][n-1]
            except IndexError:
                continue

    def printmtrx(self, matrix):
        """Print out the matrix for debug purposes"""
        print("\n".join([str(i) for i in matrix]))

class TestSolution(unittest.TestCase):
    def test_answers(self) -> None:
        sol = Solution()
        self.assertEqual(sol.uniquePaths(1,1), 1)
        self.assertEqual(sol.uniquePaths(2,1), 1)
        self.assertEqual(sol.uniquePaths(1,3), 1)
        self.assertEqual(sol.uniquePaths(2,2), 2)
        self.assertEqual(sol.uniquePaths(3,2), 3)
        self.assertEqual(sol.uniquePaths(7, 3), 28)
        self.assertEqual(sol.uniquePaths(3,3), 6)
        self.assertEqual(sol.uniquePaths(100,100),
            22750883079422934966181954039568885395604168260154104734000)
