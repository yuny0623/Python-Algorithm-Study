from sys import stdin, stdout

for _ in range(int(input())):
    s = stdin.readline()
    stdout.write(s[0].upper() + s[1:])
    
