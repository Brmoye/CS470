# Brian Moye
# September 7, 2022
# CS 470 - Assignment 5
# Search and display a csv file, in this case of Netflix shows and movies

# Read the file and add each line to a list
def init():
    infile = open("netflix_titles.csv", "r")
    fileList = []
    
    for line in infile:
        fileList.append(line.rstrip()) 
    infile.close()
    
    return fileList

def menu():
    print("\nPlease select an option below:")
    print("1. Search\n2. Display number of TV Shows\n3. View all\n4. Exit")

# Display the list of Netflix shows in a neat format
def displayList(dataList):
    header = dataList[0].split(",")
    print("{:^8s}".format(header[0]), "{:8s}".format(header[1]), "{:^60s}".format(header[2]), "{:10s}".format(header[3]), "{:^14s}".format(header[4]), "{:^6s}".format(header[5]), "{:11s}".format(header[6]))

    for index in range(1, len(dataList)):
        data = dataList[index].split(",")
        print("{:8s}".format(data[0]), "{:8s}".format(data[1]), "{:<60s}".format(data[2]), "{:10s}".format(data[3]), "{:^14s}".format(data[4]), "{:^6s}".format(data[5]), "{:11s}".format(data[6]))

# Search the list of shows and movies
def search(dataList, searchData):
    returnData = []
    returnData.append(dataList[0])
    for index in range(1, len(dataList)):
        data = dataList[index].split(",")
        for i in range(0, len(data)):
            if searchData in data[i].strip().lower():
                returnData.append(dataList[index])
    return returnData
    
def main():
    dataList = init()
    print("\nNetflix Shows\Movies:")
    while (True):
        menu()
        userInput = input("Selection: ").strip()
        try:
            userInput = int(userInput)
        except ValueError:
            print("You must enter an integer.")

        if userInput == 1:
            displayList(search(dataList, input("Enter search paramater: ").strip().lower()))
        elif userInput == 2:
            print("\nThere are", len(search(dataList, "tv show")), "TV Shows in this data set.")
        elif userInput == 3:
            displayList(dataList)
        elif userInput == 4:
            break
        else:
            print("Please select an option from the menu.")
    
    
main()