'''
0115 ~ 0120 

Runtime: 50 ms, faster than 33.02% of Python3 online submissions for Occurrences After Bigram.
Memory Usage: 13.9 MB, less than 20.52% of Python3 online submissions for Occurrences After Bigram.
'''

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text_li = text.split()
        i = 0
        third_li = []
        while i < len(text_li):
            if text_li[i] == first:
                if i + 1 < len(text_li) and text_li[i + 1] == second:
                    if i + 2 < len(text_li):
                        third_li.append(text_li[i + 2])
            i += 1
        return third_li
            