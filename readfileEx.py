infile = open("/Users/brmoye/Documents/UNA/Fall 2022/CS470/baseball.txt", "r")

for line in infile:
    line = line.strip()
    data = line.split(" ")
    #[first, last, atBats, hits] = line.split(" ")
    print("First:", data[0])
    print("Last:", data[1])
    print("At Bats:", data[2])
    print("Hits:", data[3])
    print("Average:", "%.3f" %(int(data[3]) / int(data[2])))
    print()
    
infile.close()