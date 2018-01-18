import sys

start = int(sys.argv[1])
n = int(sys.argv[2])
avg = int(sys.argv[3]) / n

for i in range(n):
    start += avg
    print(start, end='\t')
print()