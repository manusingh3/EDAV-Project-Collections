outputBase = 'sotus/sotu_' # output.1.txt, output.2.txt, etc.
sotuFile = open("sotus/contents.txt", 'w')
i = 1
j=0
f = open('SoU-1790-2006.txt', 'r')
for line in f:
    row = line.strip()
    if row is  "":
        continue
    if '***' not in row:
        if i == 1:
            sotuFile.write(str(j)+','+row + "\n")
            j = j+1
        else:
            sotuFile.write(row + "\n")
    else:
        sotuFile.close()
        sotuFile = open(outputBase + str(i)+".txt", 'w')
        i = i+1

    