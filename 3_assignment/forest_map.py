 

def distance(forestLayout, initialBreadcrumbs):
    minColumn = 0
    for row in range(len(forestLayout)):
        for column in range(minColumn, len(forestLayout[row])):
            print(forestLayout[row][column])
            if forestLayout[row][column] == "E":
                return initialBreadcrumbs
            elif forestLayout[row][column] == " ":
                forestLayout[row][column] = "*"
                initialBreadcrumbs -= 1
                minColumn = column
            else:
                break
               
def crumbsLeft(breadcrumbsLeft):
    if breadcrumbsLeft < 0:
        print("Not enough breadcrumbs for the trip.")
    elif breadcrumbsLeft == 0:
        print("Phew, just enough breadcrumbs for the trip.")
    else:
        print(f"{breadcrumbsLeft} breadcrumb(s) are left.")

def main():
    forestPath = [
        [' ',' ',' ','X','X'],
        ['X','X',' ',' ','X'],
        ['X','X','X',' ','X'],
        [' ','X','X',' ',' '],
        [' ','X','X','X',' '],
        [' ',' ','X','X',' '],
        [' ',' ','X','X','E']
    ]

    breadcrumbs = int(input("Enter number of breadcrumbs: "))
    
    print(distance(forestPath, breadcrumbs))
    print(forestPath)


if __name__ == "__main__":
    main()