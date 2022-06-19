'''
0310 ~ 0319 

Runtime: 36 ms, faster than 76.38% of Python3 online submissions for Defanging an IP Address.
Memory Usage: 13.8 MB, less than 47.72% of Python3 online submissions for Defanging an IP Address.
'''
class Solution:
    def defangIPaddr(self, address: str) -> str:
        new_ip  = []
        for c in address:
            if c.isdigit():
                new_ip.append(c)
            else:
                new_ip.append("[")
                new_ip.append(c)
                new_ip.append("]")
        return ''.join(new_ip) 


