class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        li = list(map(str, s.rstrip().split()))
        print(li)
        return len(li[-1])
