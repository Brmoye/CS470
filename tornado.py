infile = open("tornado.txt", "r")
dataList = []

for line in infile:
    dataList.append(line.rstrip()) 
infile.close()

print("F3 Tornadoes in Alabama since 2000", end="\n\n")

print(" YEAR            COUNTY                 FAT. INJ.")

for tornado in dataList:
    data = tornado.split(",")
    if int(data[0])>=2000 and data[2]=="F3":
        print("%5s"%data[0], "%-30s"%data[1], "%5s"%data[3], "%5s"%data[4])
        