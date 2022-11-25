# 211283E
# LIU JIAJUN
# IT2153-06

from typing import List 
# Very impoortant, got color !!!!
from BookingRecords import BookingRecords
from TestData import PrintRecord
from termcolor import colored

class Sorting:
    @staticmethod 
    def BubbleSort(records: List[BookingRecords]):
        print('bubble sorting')
        n = len(records)
        for i in range(n-1,0,-1):
            swapped = False
            for j in range(i):
                if records[j].get_customer_name() > records[j+1].get_customer_name():
                    # switch position
                    temp = records[j]
                    records[j] = records[j+1]
                    records[j+1] = temp
                    swapped = True

            if not swapped:
                break
    
        PrintRecord(records)

    @staticmethod
    def SelectionSort(records: List[BookingRecords]):
        n = len(records)
        for i in range(n-1,0,-1):
            # print(i)
            positionofMax = 0
            for j in range(1,i+1):
                # print("j: ",j)
                if records[j].get_package_name() > records[positionofMax].get_package_name():
                    positionofMax = j

            temp = records[i]
            records[i] = records[positionofMax]
            records[positionofMax] = temp 
    

            
    @staticmethod
    def InsertionSort(records: List[BookingRecords]):
        n = len(records)
        for i in range(1,n):
            currentvalue = records[i]
            position = i

            while position > 0 and currentvalue.get_package_cost() < records[position-1].get_package_cost():
                records[position] = records[position-1]
                position = position - 1
            
            records[position] = currentvalue

        PrintRecord(records)

            