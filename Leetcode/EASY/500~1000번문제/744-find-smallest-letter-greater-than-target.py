'''
0225 ~ 0232
Runtime: 119 ms, faster than 74.01% of Python3 online submissions for Find Smallest Letter Greater Than Target.
Memory Usage: 14.2 MB, less than 91.13% of Python3 online submissions for Find Smallest Letter Greater Than Target.

코멘트:
쉬운 문제임. 
'''

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # 0226
        letters = sorted(letters)
        for i in letters:
            if ord(i) > ord(target):
                return i 
        return letters[0]
       
    
      
     
   
  
   

