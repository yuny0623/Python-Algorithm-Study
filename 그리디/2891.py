'''
1257 
~
0154 
'''

N, S, R = map(int, input().split())
broken = list(map(int, input().split()))
spare = list(map(int, input().split()))

answer = S

# ascending sort
broken.sort()
spare.sort()

# check if possible to start
for i in range(S):
	if not spare:
		# no more extra kayaks
		break
	for j in range(R):
		# find kayak..
		if broken[i] == spare[j] or broken[i] == spare[j] + 1 or broken[i] == spare[j] - 1:
			answer -= 1
			spare[j] = -1 # used kayak
			break
			
print(answer)