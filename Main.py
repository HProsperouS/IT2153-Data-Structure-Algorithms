# 211283E
# LIU JIAJUN
# IT2153-06
from Sorting import Sorting # Sorting algoithms
from Searching import Searching #Searching algorithms
from TestData import GenerateTestData , PrintRecord #Printinhg and import the list of data
from AdvancedSorting import AdvancedSort # Bonus features 

def DisplayAll(records):
    print("Display all records")
    PrintRecord(records)

def BubbleSortByCustomer(records):
    print("Bubble Sort by customer name")
    Sorting.BubbleSort(records)

def SelectionSortByPackage(records):
    print("Selection Sort by package")
    Sorting.SelectionSort(records)
    PrintRecord(records)

def InsertionSortByPackageCost(records):
    print("Insertion Sort by package")
    Sorting.InsertionSort(records)

def OrderedLinearSearchByCustomer(records):
    print("Linear Search by customer name")
    Sorting.BubbleSort(records)
    Searching.OrderedLinearSearch(records)

def UnOrderedLinearSearchByCustomer(records):
    print("Linear Search by customer name")
    Searching.UnorderedLinearSearch(records)

def BinarySearchByPackage(records):
    print("Binary Search by package name")
    Sorting.SelectionSort(records)
    Searching.BinarySearch(records)

def RangeSearchByCost(records):
    Searching.RangeSearch(records)

def ShellSortByNumberOfPax(records):
    print("Shell Sort by number of pax")
    AdvancedSort.ShellSort(records)

def CocktailSortByCustomer(records):
    print("Cocktail Sort by customer name")
    AdvancedSort.Cocktail_sort(records)


if __name__ == '__main__':
    records = []
    records = GenerateTestData()

    # Menu Code
    while True:
        try:
            print()
            print('Select the program (1-7) to run: ')
            print('1. Display all records')
            print('2. Sort record by Customer Name using Bubble sort')
            print('3. Sort record by Package Name using Selection sort')
            print('4. Sort record by Package Cost using Insertion sort')
            print('5. Search record by Customer Name using Ordered Linear Search and update record')
            print('6. Search record by Customer Name using Unordered Linear Search and update record')
            print('7. Search record by Package Name using Binary Search and update record')
            print('8. List records range from $X to $Y. e.g $100-200')
            print('9. Sort record by Number Of Pax using Shell sort')
            print('10. Sort record by Customer Name using Cocktail sort')
            print('Ctrl-D Exit Application')
            print()

            selection = input("Enter between 1-7 or ctrl-D to exit: ")

            if selection == '1':
                DisplayAll(records)
            elif selection == '2':
                BubbleSortByCustomer(records)
            elif selection == '3':
                SelectionSortByPackage(records)
            elif selection == '4':
                InsertionSortByPackageCost(records)
            elif selection == '5':
                OrderedLinearSearchByCustomer(records)
            elif selection == '6':
                UnOrderedLinearSearchByCustomer(records)
            elif selection == '7':
                BinarySearchByPackage(records) 
            elif selection == '8':
                RangeSearchByCost(records)
            elif selection == '9':
                ShellSortByNumberOfPax(records)
            elif selection == '10':
                CocktailSortByCustomer(records)
            else:
                print()
                print("Please enter correct choice")
                print()

        except EOFError:
            print()
            print("Bye. See you again")
            break