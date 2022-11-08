##
# Orders a list of postal codes then prints them with codes starting with the same
# letter printed on the same line
##

def mergeLists(values, low, middle, high):
    leftCurrent = low
    rightCurrent = middle + 1
    while leftCurrent <= middle and rightCurrent <= high:
        if values[leftCurrent] <= values[rightCurrent]:
            


def mergeSort(values, low, high):
    if low < high:
        middle = (low+high)//2
        mergeSort(values, low, middle)
        mergeSort(values, middle+1, high)
        mergeLists(values, low, middle, high)


def main():
    postal_codes = ['A1A 1A1', 'B3K 5X5', 'V9A 7N2', 'A0Z 6P7', 'H0H 0H0', 'A1B 1T0']