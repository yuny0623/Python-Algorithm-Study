'''
0627 
~
0759
'''
import copy 

x, y = map(str, input().split())

x = list(x)
y = list(y)
# print("x, y: ",x, y) 

# 최소값 
min_value_x = x[:]
for i in range(len(x)):
    if x[i] == '6':
        min_value_x[i] = '5'
min_value_y = y[:]
for i in range(len(y)):
    if y[i] == '6':
        min_value_y[i] = '5'

# 최대값 
max_value_x = x[:]
for i in range(len(x)):
    if x[i] == '5':
        max_value_x[i] = '6'
max_value_y = y[:] 
for i in range(len(y)):
    if y[i] == '5':
        max_value_y[i] = '6'

# print("min_value_x, min_value_y: ", min_value_x, min_value_y)
# print("max_value_x, max_value_y: ", max_value_x, max_value_y)


sa = ''
for i in range(len(min_value_x)):
    sa += min_value_x[i]
min_value_x = sa 

sb = ''
for i in range(len(min_value_y)):
    sb += min_value_y[i]
min_value_y = sb

sc = ''
for i in range(len(max_value_x)):
    sc += max_value_x[i]
max_value_x = sc 

sd = ''
for i in range(len(max_value_y)):
    sd += max_value_y[i]
max_value_y = sd 

# print()
# print()
# print(type(min_value_x))
# print(type(min_value_y))
# print(type(max_value_y))
# print(type(max_value_y))

result_min = int(min_value_x) + int(min_value_y)
result_max = int(max_value_x) + int(max_value_y)

print(result_min, result_max)
# print((int(min_value_x) + int(min_value_y)),(int(max_value_x) + int(max_value_y)))
