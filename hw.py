file = 'nya.txt'

with open(file, 'r') as f:
    for i in f:
        print(i)
    f.close()