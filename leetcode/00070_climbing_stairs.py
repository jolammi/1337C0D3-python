"""
https://leetcode.com/problems/climbing-stairs
"""
import unittest

class Solution:
    """
    By writing out some of the first outputs we can see that this is a kind of
    Fibonacci series: 1 2 3 5 8 13...
    The current answer can be formed by summing the last 2 previous
    answers. My solution is kind of dirty as I calculate the previous steps
    and then just sum the last two together.
    """
    def climbStairs(self, n: int) -> int:
        if n in [1, 2, 3]:
            return n
        outputs = []
        for idx, num in enumerate(range(1,n)):
            if num == 1 or num == 2:
                outputs.append(num)
                continue
            else:
                outputs.append(outputs[idx-1]+outputs[idx-2])
        return outputs[-1] + outputs[-2]

class TestSolution(unittest.TestCase):
    def test_answers(self) -> None:
        sol = Solution()
        self.assertEqual(sol.climbStairs(1), 1)
        self.assertEqual(sol.climbStairs(2), 2)
        self.assertEqual(sol.climbStairs(3), 3)
        self.assertEqual(sol.climbStairs(5), 8)
        self.assertEqual(sol.climbStairs(20), 10946)
        self.assertEqual(sol.climbStairs(45), 1836311903)