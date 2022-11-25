# 211283E
# LIU JIAJUN
# IT2153-06

from TestData import PrintRecord

class AdvancedSort:
    @staticmethod
    def ShellSort(records):

        sublistcount = len(records) // 2
        while sublistcount > 0:

            for startposition in range(sublistcount):
               AdvancedSort.gapInsertionSort(records, startposition, sublistcount)

            # print("After increments of size", sublistcount)

            # PrintRecord(records)

            sublistcount = sublistcount // 2
        
        PrintRecord(records) 

    @staticmethod
    def gapInsertionSort(records, start, gap):
        for i in range(start+gap, len(records), gap):

            currentvalue = records[i]
            position = i

            while position >= gap and records[position-gap].get_number_of_pax() > currentvalue.get_number_of_pax():
                records[position] = records[position-gap]
                position = position-gap

            records[position] = currentvalue

    @staticmethod
    def Cocktail_sort(records):
        for i in range(len(records) - 1, 0, -1):
            bubbled = False

            for j in range(i):
                if records[j].get_customer_name() > records[j + 1].get_customer_name():
                    records[j], records[j + 1] = records[j + 1], records[j]
                    bubbled = True
            
            for j in range(i, 0, -1):
                if records[j].get_customer_name() < records[j - 1].get_customer_name():
                    records[j], records[j - 1] = records[j - 1], records[j]
                    bubbled = True

            if not bubbled: 
                break

        PrintRecord(records)

   

    

        




























#     @staticmethod
#     def QuickSort(records):
#         AdvancedSort.QuickSortHelper(records,0,len(records)-1) 
#         PrintRecord(records)

#     @staticmethod
#     def QuickSortHelper(records,first,last):
#         if first < last:

#             splitpoint = AdvancedSort.partitionn(records,first,last)

#             AdvancedSort.QuickSortHelper(records,first,splitpoint-1)  
            
#             AdvancedSort.QuickSortHelper(records,splitpoint + 1,last)  

#     @staticmethod
#     def partitionn(records,first,last):
#         pivotvalue = records[first]

#         leftmark = first + 1
#         rightmark = last

#         done = False
#         while not done:
#             while leftmark <= rightmark and records[leftmark].get_number_of_pax() <= pivotvalue.get_number_of_pax():
#                 leftmark += 1

#             while records[rightmark].get_number_of_pax() >= pivotvalue.get_number_of_pax() and rightmark >= leftmark:
#                 rightmark -= 1

#             if rightmark < leftmark:
#                 done = True
#                 # temp = records[first]
#                 # records[first] = records[rightmark]
#                 # records[rightmark] = temp
#             else:
#                 # swap
#                 temp = records[leftmark]
#                 records[leftmark] = records[rightmark]
#                 records[rightmark] = temp

#         # 找到pivotvalue 的分割点
#         temp = records[first]
#         records[first] = records[rightmark]
#         records[rightmark] = temp

#         return rightmark



    
    