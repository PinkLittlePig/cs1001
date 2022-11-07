def getColumn(matrix, columnIndex):
    column = []
    for row in matrix:
        column.append(row[columnIndex])
    return column

def computeAllRanges(shuttleTypes, ratings):
    print("{:<20} {:<20}".format('Shuttle Types', 'Range of Ratings'))
    for shuttleTypeIndex in range(len(ratings)):
        ratingRange = max(ratings[shuttleTypeIndex]) - min(ratings[shuttleTypeIndex])
        print("{:<20} {:<20}".format(shuttleTypes[shuttleTypeIndex], ratingRange))

def computeAverage(ratings, columnNumber):
    columnRatings = getColumn(ratings, columnNumber)
    lowestRating = min(columnRatings)
    columnRatings.remove(lowestRating)
    averageRating = sum(columnRatings)/len(columnRatings)
    return averageRating

def main():
    shuttleTypes = ["Racer", "Everyday", "Emergency", "Heavy Duty", "Light"]
    shuttleMakers = ["Jupishut", "Shuttlejup", "Shuttlesrjup", "Jupnride", \
        "Riderjup", "Shuttlejrides", "Shuttajup"]
    ratings = [[80,90,55,65,80,65,70],
        [65,45,85,80,80,80,75],
        [90,60,90,90,40,45,75],
        [75,55,95,95,65,95,90],
        [80,90,75,65,75,60,80]]

    computeAllRanges(shuttleTypes, ratings)

    print("{:<20} {:<20}".format('Shuttle Maker', 'Average Rating'))
    for shuttleMakerIndex in range(len(shuttleMakers)):
        averageRating = computeAverage(ratings, shuttleMakerIndex)
        print("{:<20} {:<20}".format(shuttleMakers[shuttleMakerIndex], averageRating))

if __name__ == "__main__":
    main()