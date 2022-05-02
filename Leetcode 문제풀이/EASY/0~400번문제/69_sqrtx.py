class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i = 0
        while True:
            if i**2 < x:
                i += 1
            elif i**2 == x:
                return i 
            else:
                return i - 1
                