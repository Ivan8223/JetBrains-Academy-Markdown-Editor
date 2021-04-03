file = open('test.txt', 'r')
print(*[line[0] for line in file], sep='\n')
file.close()
