filename = "squared_numbers.txt"

outfile = open(filename, 'w')

for number in range (1, 11):
    squared = number * number
    outfile.write(str(squared) + '\n')
    
outfile.close()

infile = open(filename, 'r')
print(infile.read()[:11])
infile.close()