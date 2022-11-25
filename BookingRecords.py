# 211283E
# LIU JIAJUN
# IT2153-06

class BookingRecords:
    # Each record has: Package Name, Customer Name, number of pax and Package Cost per pax
    def __init__(self, ID, PackageName,CustomerName,NumberOfPax, PackageCost):
        self._ID = ID
        self._package_name = PackageName
        self._customer_name = CustomerName
        self._number_of_pax = NumberOfPax
        self._package_cost = PackageCost

    # getter and setters here
    # Set
    def set_ID(self,ID):
        self._ID = ID

    def set_package_name(self,PackageName):
        self._package_name = PackageName

    def set_customer_name(self,CustomerName):
        self._customer_name = CustomerName

    def set_number_of_pax(self,NumberOfPax):
        self._number_of_pax = NumberOfPax

    def set_package_cost(self, PackageCost):
        self._package_cost = PackageCost

    # Get
    def get_ID(self):
        return self._ID
        
    def get_package_name(self):
        return self._package_name

    def get_customer_name(self):
        return self._customer_name

    def get_number_of_pax(self):
        return self._number_of_pax
    
    def get_package_cost(self):
        return self._package_cost