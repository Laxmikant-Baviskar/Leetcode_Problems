# 509. Fibonacci Number
# Problem : The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1.

class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        c = 0

        if n == 0 : return 0
        if n == 1 : return 1
        else:
            for i in range(2,n+1):
                c = a + b
                a = b
                b = c
            return c   


# Example 1:
# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

# Example 2:
# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

# Example 3:
# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.