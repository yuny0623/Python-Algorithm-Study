'''
0608 ~ 0618 
'''

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = []
        rowNum = rowIndex + 1
        for i in range(rowNum):
            row = [None for i in range(i + 1)]
            row[0], row[-1] = 1, 1
            
            for j in range(1, len(row) - 1):
                row[j] = result[i - 1][j - 1] + result[i - 1][j]
            
            result.append(row)
            
        return result[rowIndex]