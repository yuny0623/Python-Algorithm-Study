'''
1001 ~ 1009 
Runtime: 65 ms, faster than 54.71% of Python3 online submissions for Flipping an Image.
Memory Usage: 13.9 MB, less than 65.76% of Python3 online submissions for Flipping an Image.

코멘트:
비트 반전으로 풀 수 있는 방법이 있을 것 같음. 
개선 가능? 
'''

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        new_image = [] 
        for i in range(len(image)):
            temp = []
            for j in range(len(image[0])):
                temp.append(abs(image[i][j] - 1))
            new_image.append(temp[::-1])
        print(new_image)
        return new_image 


'''
비트 반전으로 푼 솔루션: 
Runtime: 64 ms, faster than 56.69% of Python3 online submissions for Flipping an Image.
Memory Usage: 13.9 MB, less than 65.76% of Python3 online submissions for Flipping an Image.
'''
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        new_image = [] 
        for i in range(len(image)):
            temp = []
            for j in range(len(image[0])):
                temp.append(int(not int(image[i][j])))
            new_image.append(temp[::-1])
        print(new_image)
        return new_image 

'''
reverse append 안해도 되는 솔루션 :
Runtime: 107 ms, faster than 8.14% of Python3 online submissions for Flipping an Image.
Memory Usage: 13.9 MB, less than 20.55% of Python3 online submissions for Flipping an Image.

코멘트: 근데 이게 가장 시간이 느림. 
'''
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        new_image = [] 
        for i in range(len(image)):
            temp = []
            for j in range(len(image[0])-1, -1, -1):
                temp.append(abs(image[i][j] - 1))
            new_image.append(temp)
        print(new_image)
        return new_image 