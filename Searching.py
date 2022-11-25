# 211283E
# LIU JIAJUN
# IT2153-06
from Update import Update
from typing import List
from BookingRecords import BookingRecords 
from tabulate import tabulate
class Searching:
    # Search record by Customer Name using Linear Search and update record
    @staticmethod
    def UnorderedLinearSearch(records:List[BookingRecords]):
        print("UnOrdered Linear search")
        alist = []
        customer_name = input("Enter Customer Name To Search: ").upper()
        all_data = [["ID","Package Name","Customer Name","No Of Pax", "Package Cost Per Pax"]]
        for i in range(len(records)):
            # print(i)
            if records[i].get_customer_name().upper() == customer_name:
                all_data.append([records[i].get_ID(),records[i].get_package_name(),records[i].get_customer_name(),records[i].get_number_of_pax(),records[i].get_package_cost()])

                alist.append(records[i])

        if len(alist) > 0:
            table = tabulate(all_data)
            print(table)

        Update.update(alist)
                
    @staticmethod
    def OrderedLinearSearch(records: List[BookingRecords]):        
        print("Ordered Linear search")
        alist = []
        customer_name = input("Enter Customer Name To Search: ").upper()
        all_data = [["ID","Package Name","Customer Name","No Of Pax", "Package Cost Per Pax"]]
        for i in range(len(records)):
            # print(i)
            if records[i].get_customer_name().upper() == customer_name:
                all_data.append([records[i].get_ID(),records[i].get_package_name(),records[i].get_customer_name(),records[i].get_number_of_pax(),records[i].get_package_cost()])

                alist.append(records[i])
                
            # How if it is sorted?

            else:
                if records[i].get_customer_name().upper() > customer_name:
                    break

        if len(alist) > 0:
            table = tabulate(all_data)
            print(table)

        Update.update(alist)

        # In the best case, only one comparison is needed to know that the target element 
        # is not in the list. In a word, only when the target element does not exist in the list, 
        # ordering the elements will improve the efficiency of the sequential search
        

    # Must be a sorted list
    # Search record by Package Name using Binary Search and update record
    @staticmethod
    def BinarySearch(records: List[BookingRecords]):

        print("Binary search")
        first = 0
        last = len(records) - 1
        found = False
        package_name = input("Enter Package Name To Search: ")
        alist = []
        # table header
        all_data = [["ID","Package Name","Customer Name","No Of Pax", "Package Cost Per Pax"]]

        while first <= last and not found:
            midpoint = (first + last) // 2
            if records[midpoint].get_package_name().upper() == package_name.upper():
                first_occurrence = midpoint
                last_occurrence = midpoint

                found = True
                alist.append(records[midpoint])

                while first_occurrence != first and records[first_occurrence - 1].get_package_name().upper() == package_name.upper():
                        first_occurrence -= 1
                        alist.append(records[first_occurrence])

                while last_occurrence != last and records[last_occurrence + 1].get_package_name().upper() == package_name.upper():
                        last_occurrence += 1
                        alist.append(records[last_occurrence])

                for i in alist:
                    all_data.append([i.get_ID(),i.get_package_name(),i.get_customer_name(),i.get_number_of_pax(),i.get_package_cost()])

            elif package_name.upper() < records[midpoint].get_package_name().upper():
                    last = midpoint - 1
    
            elif package_name.upper() > records[midpoint].get_package_name().upper():
                    first = midpoint + 1
                    
        if len(alist) > 0:
            table1 = tabulate(all_data)
            print(table1)

        Update.update(alist)

    # List records range from $X to $Y. e.g $100-200
    @staticmethod
    def RangeSearch(records: List[BookingRecords]):
        try:
            all_data = [["ID","Package Name","Customer Name","No Of Pax", "Package Cost Per Pax"]]
            range = input("Enter records range from $X to $Y. e.g $100-200: ")
            r = range.split("-")
            start = int(r[0])
            end = int(r[1])

            if start > end:
                start = int(r[1])
                end = int(r[0])
            
            for i in records:
                if i.get_package_cost() >= start and i.get_package_cost() <= end:
                    all_data.append([i.get_ID(),i.get_package_name(),i.get_customer_name(),i.get_number_of_pax(),i.get_package_cost()])
            
            if len(all_data[1]) == 0:
                print("No result found")
            else:
                table1 = tabulate(all_data)
                print(table1)
        except:
                print("Invalid Input, Please Try Again")



