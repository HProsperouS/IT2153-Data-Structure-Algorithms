# 211283E
# LIU JIAJUN
# IT2153-06

class Update:
    @staticmethod
    def update(alist):
        if len(alist) == 0:
                print("Your Input is not found")
        else:
            update = input("Do you like update the record? (Y/N): ")
            if update.upper() == "Y" and len(alist) > 1:
                found = False
                while True:
                    try:
                        ID = int(input("Enter the id to update: "))
                        break
                    except ValueError:
                        print("Invalid Input, Please enter an integer")

                for i in alist:
                    if i.get_ID() == ID:
                        found = True 
                        while True:
                            try:
                                package_name = input("Enter new package name: ").lower()
                                p_name = package_name.capitalize()
                                i.set_package_name(p_name)
                                break
                            except ValueError:
                                print("Invalid Input!!! Please Try Again")
                        while True:
                            try:
                                customer_name = input("Enter new customer name: ").lower()
                                c_name = customer_name.capitalize()
                                i.set_customer_name(c_name)
                                break
                            except ValueError:
                                print("Invalid Input!!! Please Try Again")
                        while True:
                            try:
                                i.set_number_of_pax(int(input("Enter new number of pax: ")))
                                break
                            except ValueError:
                                print("Invalid Input!!! Please Try Enter ")
                        while True:
                            try:
                                i.set_package_cost(int(input("Enter new package cost: ")))
                                break
                            except ValueError:
                                print("Invalid Input!!! Please Try Enter")

                        print("You have updated the data successfully") 

                if not found:
                    print("The ID did't exist! Please try again")

            elif update.upper() == "Y" and len(alist) == 1:
                i = alist[0]
                while True:
                    try:
                        package_name = input("Enter new package name: ")
                        p_name = package_name.capitalize()
                        i.set_package_name(p_name)
                        break
                    except ValueError:
                        print("Invalid Input!!! Please Try Again")

                while True:
                    try:
                        customer_name = input("Enter new customer name: ")
                        c_name = customer_name.capitalize()
                        i.set_customer_name(c_name)
                        break
                    except ValueError:
                        print("Invalid Input!!! Please Try Again")

                while True:
                    try:
                        i.set_number_of_pax(int(input("Enter new number of pax: ")))
                        break
                    except ValueError:
                        print("Invalid Input!!! Please Try Enter ")

                while True:
                    try:
                        i.set_package_cost(int(input("Enter new package cost: ")))
                        break
                    except ValueError:
                        print("Invalid Input!!! Please Try Enter")

                print("You have updated the data successfully") 

            else:
                print("You chose to not update")