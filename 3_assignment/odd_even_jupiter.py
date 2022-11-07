##
# 
##

# Given a name as a sting gets the sum of all the letters
# ASCII values and returns it
def getSum(name):
    asciiSum = 0
    for letter in name:
        asciiSum += ord(letter)
    return asciiSum

# Given a list of names updates the names by adding a 0 or 1
# at the end of each name based on the sum of the ASCII values
# of each name
def updateList(nameList):
    for nameIndex in range(len(nameList)):
        if getSum(nameList[nameIndex]) % 2:
            # Odd 
            nameList[nameIndex] += "1"
        else:
            # Even
            nameList[nameIndex] += "0"

# Given a list of names counts and prints the number of odd and even names
# based on what number each name has at the end of it.
def countOddEven(nameList):
    odds = 0
    for name in nameList:
        if name[-1] == "1":
            odds += 1

    evens = len(nameList) - odds
    print(f"There are {evens} Jupians in the even group.")
    print(f"There are {odds} Jupians in the odd group.")

def main():
    jupians = ["Zubajup","Bubajup","Pubajup","Yubajup","Rubajup",\
        "Subajup","Tubajup","Uubajup","Qubajup","Nubajup"]
    
    updateList(jupians)
    print(jupians)
    
    countOddEven(jupians)

if __name__ == "__main__":
    main()