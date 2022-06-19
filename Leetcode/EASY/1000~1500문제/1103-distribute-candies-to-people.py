'''
0253 ~ 0306 

Runtime: 74 ms, faster than 25.90% of Python3 online submissions for Distribute Candies to People.
Memory Usage: 14 MB, less than 8.54% of Python3 online submissions for Distribute Candies to People.
'''

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        p = [0] * num_people
        candy = 1
        i = 0 
        while i < num_people and candies > 0:
            if candies > candy: 
                candies -= candy
            else: 
                candy = candies
                candies = 0
            p[i] += candy 
            candy += 1
            i += 1
            if i%num_people == 0:
                i = 0 
                
        return p 
            

