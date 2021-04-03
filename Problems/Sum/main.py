file = open('sums.txt', 'r')
print(*[(sum(map(int, line.split()))) for line in file], sep='\n')
file.close()
