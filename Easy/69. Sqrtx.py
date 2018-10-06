'''
Implement int sqrt(int x).
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:
Input: 4
Output: 2

Example 2:
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
'''


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x
        while left <= right:
            mid = (right + left) // 2
            sq = mid * mid
            if sq < x:
                left = mid + 1
            elif sq > x:
                right = mid - 1
            else:
                return mid
        return right

    def mySqrt1(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        left, right = 1, x // 2
        while left <= right:
            mid = left + (right - left) // 2
            if mid > x // mid:
                right = mid - 1
            else:
                left = mid + 1

        return left - 1




if __name__ == "__main__":
    print(Solution().mySqrt(10))