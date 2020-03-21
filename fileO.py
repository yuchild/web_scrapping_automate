f = open('Exercise Files/inputFile.txt', 'r')
passFile = open('Exercise Files/PassFile.txt', 'w')
failFile = open('Exercise Files/FailFile.txt', 'w')
for line in f:
    line_split = line.split()
    if line_split[2] == 'P':
        passFile.write(line)
    else:
        failFile.write(line)
f.close()
passFile.close()
failFile.close()