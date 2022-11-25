# 211283E
# LIU JIAJUN
# IT2153-06

from tabulate import tabulate
from BookingRecords import BookingRecords

def GenerateTestData():
    td = []
    
    # Each record has: Package Name, Customer Name, number of pax and Package Cost per pax

    td.append(BookingRecords(1,'Sea Breeze & Champagne Package','Emma',10,388))
    td.append(BookingRecords(2,'Fairmont Singapore Mancation','Olivia',2,408))
    td.append(BookingRecords(3,'Craft and Cook Staycation Package','Charlotte',3,288))
    td.append(BookingRecords(4,'Marina Bay Sands Sandsational Staycation Package','Hannah',3,328))
    td.append(BookingRecords(5,'Reflections of Raffles Package','Alyssa',2,258))
    td.append(BookingRecords(6,'All-Inclusive Datecation Package','Grace',1,238))
    td.append(BookingRecords(7,'Play Line Friends Themed Staycation Package','Eric',2,198))
    td.append(BookingRecords(8,'Glamping Under the Stars Package','Lucas',3,198))
    td.append(BookingRecords(9,'Permier Package','Naruto',2,158))
    td.append(BookingRecords(10,'Executive Room','Sasuke',2,166))

    td.append(BookingRecords(11,'Executive Room','Sasuke',2,167))
    td.append(BookingRecords(12,'Executive Room','Sasuke',2,168))


    return td
    
def PrintRecord(records):
    all_data = [["ID","Package Name","Customer Name","No Of Pax", "Package Cost Per Pax"]]
    for i in range(len(records)):
        # print()
        # print("ID:{}".format(records[i].get_ID()))
        # print("Package Name: {}".format(records[i].get_package_name()))
        # print("Customer Name: {}".format(records[i].get_customer_name()))
        # print("Number of pax: {}".format(records[i].get_number_of_pax()))
        # print("Package Cost per pax: {}".format(records[i].get_package_cost()))
        # print()

        all_data.append([records[i].get_ID(),
                        records[i].get_package_name(),
                        records[i].get_customer_name(),
                        records[i].get_number_of_pax(),
                        records[i].get_package_cost()
                        ])

    table1 = tabulate(all_data)
    print(table1)

