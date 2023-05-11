import pickle
import tabulate

class VehicleAttributes:
    _keyList = ["id", "ownerName", "vendor", "model", "type", "registrationNumber", "engineNumber", "mileage"]
    _dataBase = dict.fromkeys(_keyList, None)

class Vehicles(VehicleAttributes):
    __listOfVehicles = []
    __id = 0

    def addEntries(self):
        option = 1
        while option == 1:
            self.__id += 1
            entryList = []
            entryList.append(self.__id)
            entryList.append(input("Owner Name : "))
            entryList.append(input("Vendor Name : "))
            entryList.append(input("Model Name : "))
            entryList.append(input("Type : "))
            entryList.append(int(input("Registration Number : ")))
            entryList.append(int(input("Engine Number : ")))
            entryList.append(float(input("Mileage : ")))

            for i, key in zip(entryList, self._dataBase):
                self._dataBase[key] = i
            self.__listOfVehicles.append(self._dataBase.copy())
            option = int(input("Do you want to add more entries\n1.Add\n2.Exit\n"))

    def deleteEntries(self):
        found = False
        searchKey = int(input("Enter your ID : "))
        for i in range(len(self.__listOfVehicles)):
            if self.__listOfVehicles[i]['id'] == searchKey:
                found = True
                del self.__listOfVehicles[i]
                break
        if not found:
            print("Invalid Id")

    def modifyEntries(self):
        found = False
        searchKey = int(input("Enter your ID : "))
        for i in self.__listOfVehicles:
            if i['id'] == searchKey:
                found = True
                print("Choose the attribute you want to change")
                print("1.Owner Name\n2.Vendor Name\n3.Model Name")
                print("4.Type\n5.Registration Number\n6.Engine Number")
                print("7.Mileage")
                option = int(input())
                if option == 1:
                    i['ownerName'] = input("Owner Name : ")
                elif option == 2:
                    i['vendor'] = input("Vendor Name : ")
                elif option == 3:
                    i['model'] = input("Model Name : ")
                elif option == 4:
                    i['type'] = input("Type : ")
                elif option == 5:
                    i['registrationNumber'] = int(input("Registration Number : "))
                elif option == 6:
                    i['engineNumber'] = int(input("Engine Number : "))
                elif option == 7:
                    i['mileage'] = float(input("Mileage : "))
        if not found:
            print("Invalid Key")

    def display(self, *args):
        header = ['Id', 'Owner', 'Vendor', 'Model', 'Type', 'Registration Number', 'Engine Number', 'Mileage']
        if len(args) == 0:
            rows = [x.values() for x in self.__listOfVehicles]
            print(tabulate.tabulate(rows, header, tablefmt='grid'))
        elif len(args) == 2:
            print("\n", args[0])
            rows = [x.values() for x in args[1]]
            print(tabulate.tabulate(rows, header, tablefmt='grid'))

    def sortMileage(self):
        sortedList = sorted(self.__listOfVehicles, key=lambda i: i['mileage'])
        self.display("Mileage Sorted List", sortedList)

    def createFile(self):
        pickle.dump(self.__listOfVehicles, open("vehicleDetails.pkl", "wb"))

    def filterAttributes(self):
        print("Choose the attribute which you want to filter\n1.Owner Name")
        print("2.Vendor\n3.Model Name\n4.Type\n5.Mileage")
        option = int(input("Option : "))
        filteredList = []
        if option == 1:
            filterKey = input("Enter the name you want to filter")
            filteredList = [i for i in self.__listOfVehicles if i['ownerName'] == filterKey]
            self.display("Filtered List", filteredList)
        elif option == 2:
            filterKey = input("Enter the name you want to filter")
            filteredList = [i for i in self.__listOfVehicles if i['vendor'] == filterKey]
            self.display("Filtered List", filteredList)
        elif option == 3:
            filterKey = input("Enter the name you want to filter")
            filteredList = [i for i in self.__listOfVehicles if i['model'] == filterKey]
            self.display("Filtered List", filteredList)
        elif option == 4:
            filterKey = input("Enter the name you want to filter")
            filteredList = [i for i in self.__listOfVehicles if i['type'] == filterKey]
            self.display("Filtered List", filteredList)
        elif option == 5:
            filterKey = float(input("Enter the name you want to filter"))
            filteredList = [i for i in self.__listOfVehicles if i['mileage'] == filterKey]
            self.display("Filtered List", filteredList)

    def loadFile(self, filePath):
        self.__listOfVehicles = pickle.load(open(filePath, "rb"))
        idList = [self.__listOfVehicles[i]['id'] for i in range(len(self.__listOfVehicles))]
        self.__id = max(idList)

def main():
    vehicleObject = Vehicles()
    if int(input("1.Add Entries\n2.Load Pickle\n")) == 1:
        vehicleObject.addEntries()
    else:
        filePath = input("Enter the file name : ")
        vehicleObject.loadFile(filePath)
    vehicleObject.display()
    mainLoopOption = 1
    while mainLoopOption == 1:
        print("1.Add Entries\n2.Modify Attributes\n3.Delete Attributes\n4.Display Entries")
        print("5.Sort According to Mileage\n6.Filter Attributes\n7.Create Pickle File\n8.Exit")
        choice = int(input())
        if choice == 1:
            vehicleObject.addEntries()
        elif choice == 2:
            vehicleObject.modifyEntries()
        elif choice == 3:
            vehicleObject.deleteEntries()
        elif choice == 4:
            vehicleObject.display()
        elif choice == 5:
            vehicleObject.sortMileage()
        elif choice == 6:
            vehicleObject.filterAttributes()
        elif choice == 7:
            vehicleObject.createFile()
        elif choice == 8:
            break
        mainLoopOption = int(input("\n1.Continue\n2.Exit"))

main()