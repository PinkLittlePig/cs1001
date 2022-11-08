##
# Given a list of laureates prints a list of how many laureates where
# won in each area in order
##

# Given a list of areas and a list of laureates creates a
# list in the form [[area, amount won], ...] and returns it
def count(areasList, laureatesList):
    # Creates a list of zeros and each zero is the count for a coresponsing area
    countList = [0]*len(areasList)
    for laureate in laureatesList:
        # Gets the index in the area list of the current laureats area
        areaIndex = areasList.index(laureate[2])
        # Adds 1 to the value in the count list based on the index gotten above
        countList[areaIndex] += 1
    # Combines each value in the areas list with one in the count list
    # in the order they show up 
    areasCount = zip(areasList, countList)
    return areasCount

# Prints a formated list of the number of laureates
# in each area given a list in the form of [[area, amount won], ...]
def printList(areasCount):
    for area in areasCount:
        print("{:>30} {}".format(area[0], area[1]))

def sortByAmount(areasCount):
    pass

def main():
    nobelAreas = ["Chemistry","Physics","Literature","Peace","Economics", "Physiology or Medicine"]
    nobelWinners = [
        ["Albert Einstein",1921,"Physics"],
        ["Marie Curie",1903,"Physics"],
        ["Bertrand Russell",1950,"Literature"],
        ["Barbara McClintock",1983,"Physiology or Medicine"],
        ["Nelson Mandela",1993,"Peace"],
        ["Marie Curie",1911,"Chemistry"],
        ["Amartya Sen",1998,"Economics"]
    ] 
    
    areasCount = count(nobelAreas, nobelWinners)
    areasCount = sortByAmount(areasCount)
    printList(areasCount)

if __name__ == "__main__":
    main()