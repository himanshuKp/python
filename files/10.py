n = [0]*12;
print(n)
for i in range(1,13):
    n[i-1] = i * 12

print(n)

outfile = open("multiples_of_12.txt", "w")
for j in range(1,13):
    outfile.write(str(j) + " * 12 = " + str(n[j-1]) + "\n")
outfile.close()