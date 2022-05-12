'''
1010 ~ 1042  

경우의 수를 꼼꼼하게 따져야함. 

Runtime: 308 ms, faster than 11.07% of Python3 online submissions for Can Place Flowers.
Memory Usage: 14.5 MB, less than 31.07% of Python3 online submissions for Can Place Flowers.

코멘트:
코드가 난잡한데 더 깔끔하게 가능하려나. 
'''
import re
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n ==0:
            return True
        plant = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and i == 0 and i + 1 < len(flowerbed) and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                plant += 1
                continue
            if i > 0 and flowerbed[i - 1] == 0 and flowerbed[i] == 0 and i + 1 < len(flowerbed) and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                plant += 1
                continue
            if flowerbed[i] == 0 and i == len(flowerbed) - 1 and flowerbed[i - 1] == 0:
                flowerbed[i] == 1
                plant += 1
                continue
        print(flowerbed)
        print("plant:{0}, n:{1}".format(plant, n))
        return plant >= n 


'''
조금 더 깔끔한 코드: 
Runtime: 261 ms, faster than 26.54% of Python3 online submissions for Can Place Flowers.
Memory Usage: 14.3 MB, less than 95.40% of Python3 online submissions for Can Place Flowers.
'''
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        plant = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and i == 0 and i + 1 < len(flowerbed) and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                plant += 1
            elif i > 0 and flowerbed[i - 1] == 0 and flowerbed[i] == 0 and i + 1 < len(flowerbed) and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                plant += 1
            elif flowerbed[i] == 0 and i == len(flowerbed) - 1 and flowerbed[i - 1] == 0:
                flowerbed[i] == 1
                plant += 1

        return plant >= n 
