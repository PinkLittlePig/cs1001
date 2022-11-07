def count(areasList, laureatesList):
    countList = [0]*len(areasList)
    for laureate in laureatesList:
        areaIndex = areasList.index(laureate[2])
        countList[areaIndex] += 1
    areasCount = zip(areasList, countList)
    return areasCount

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