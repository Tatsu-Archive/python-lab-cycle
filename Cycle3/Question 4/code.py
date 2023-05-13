import pickle, tabulate
import pandas as pd
from fpdf import FPDF

# Class for Vehicle
class Vehicle: 
    def __init__(self, engine_no, model, owner_name, vehicle_type, mileage, vendor, registration_no):
        self.engine_no = engine_no
        self.model = model
        self.owner_name = owner_name
        self.vehicle_type = vehicle_type
        self.mileage = mileage
        self.vendor = vendor
        self.registration_no = registration_no

    def __str__(self):
        s = "{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(self.engine_no, self.model, self.owner_name, self.vehicle_type, self.mileage, self.vendor, self.registration_no)
        print(s)

# Class for Vehicle Collection
class VehicleCollection:
    def __init__(self):
        self.vehicle_list = []
    # Function to add vehicle to the list
    def add_vehicle(self, vehicle):
        self.vehicle_list.append(vehicle)
    # Function to delete vehicle from the list
    def delete_vehicle(self, registration_no):
        for i in self.vehicle_list:
            if i.registration_no == registration_no:
                self.vehicle_list.remove(i)
    # Function to modify vehicle in the list
    def modify_vehicle(self, registration_no, new_vehicle):
        for i in self.vehicle_list:
            if i.registration_no == registration_no:
                self.vehicle_list.remove(i)
                self.vehicle_list.append(new_vehicle)
    # Function to display vehicle list
    def display(self):
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format('Engine No', 'Model', 'Owner Name', 'Vehicle Type', 'Mileage', 'Vendor', 'Registration No'))
        for vehicle in self.vehicle_list:
            vehicle.__str__()
            print()
    # Function to sort vehicle list by mileage
    def sort_by_mileage(self):
        self.vehicle_list.sort(key=lambda x: x.mileage)
    # Function to store vehicle list as pickle file
    def store_pickle(self):
        with open('vehicle.pickle', 'wb') as f:
            pickle.dump(self.vehicle_list, f)
    # Function to load vehicle list from pickle file
    def load_pickle(self):
        with open('vehicle.pickle', 'rb') as f:
            self.vehicle_list = pickle.load(f)
    # Function to filter vehicle list
    def filter(self, attribute, value):
        filtered_list = []
        for i in self.vehicle_list:
            if attribute == 'engine_no':
                if i.engine_no == value:
                    filtered_list.append(i)
            elif attribute == 'model':
                if i.model == value:
                    filtered_list.append(i)
            elif attribute == 'owner_name':
                if i.owner_name == value:
                    filtered_list.append(i)
            elif attribute == 'vehicle_type':
                if i.vehicle_type == value:
                    filtered_list.append(i)
            elif attribute == 'mileage':
                if i.mileage == value:
                    filtered_list.append(i)
            elif attribute == 'vendor':
                if i.vendor == value:
                    filtered_list.append(i)
            elif attribute == 'registration_no':
                if i.registration_no == value:
                    filtered_list.append(i)
        return filtered_list
    # Function to export vehicle list as pdf
    def export_pdf(self, filtered_list):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Vehicle Details", ln=1, align='C')
        pdf.cell(200, 10, txt="{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format('Engine No', 'Model', 'Owner Name', 'Vehicle Type', 'Mileage', 'Vendor', 'Registration No'), ln=2, align='C')
        for i in filtered_list:
            pdf.cell(200, 10, txt="{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(i.engine_no, i.model, i.owner_name, i.vehicle_type, i.mileage, i.vendor, i.registration_no), ln=3, align='C')
        pdf.output("vehicle.pdf")

# Main function
def main():
    vehicle_collection = VehicleCollection()
    while True:
        print("Vehicle Collection"
                "\n1. Add Vehicle"
                "\n2. Delete Vehicle"
                "\n3. Modify Vehicle"
                "\n4. Display Vehicle"
                "\n5. Sort by Mileage"
                "\n6. Store as pickle file"
                "\n7. Load from pickle file"
                "\n8. Filter"
                "\n9. Export as pdf"
                "\n10. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            engine_no = int(input("Enter engine no: "))
            model = input("Enter model: ")
            owner_name = input("Enter owner name: ")
            vehicle_type = input("Enter vehicle type: ")
            mileage = float(input("Enter mileage: "))
            vendor = input("Enter vendor: ")
            registration_no = int(input("Enter registration no: "))
            vehicle = Vehicle(engine_no, model, owner_name, vehicle_type, mileage, vendor, registration_no)
            vehicle_collection.add_vehicle(vehicle)
        elif choice == 2:
            registration_no = int(input("Enter registration no of vehicle to be deleted: "))
            vehicle_collection.delete_vehicle(registration_no)
        elif choice == 3:
            registration_no = int(input("Enter registration no of vehicle to be modified: "))
            engine_no = int(input("Enter engine no: "))
            model = input("Enter model: ")
            owner_name = input("Enter owner name: ")
            vehicle_type = input("Enter vehicle type: ")
            mileage = float(input("Enter mileage: "))
            vendor = input("Enter vendor: ")
            registration_no = int(input("Enter registration no: "))
            new_vehicle = Vehicle(engine_no, model, owner_name, vehicle_type, mileage, vendor, registration_no)
            vehicle_collection.modify_vehicle(registration_no, new_vehicle)
        elif choice == 4:
            vehicle_collection.display()
            print()
        elif choice == 5:
            vehicle_collection.sort_by_mileage()
        elif choice == 6:
            vehicle_collection.store_pickle()
        elif choice == 7:
            vehicle_collection.load_pickle()
        elif choice == 8:
            attribute = input("Enter attribute to be filtered: ")
            value = input("Enter value to be filtered: ")
            filtered_list = vehicle_collection.filter(attribute, value)
            vehicle_collection.export_pdf(filtered_list)
        elif choice == 9:
            vehicle_collection.export_pdf(vehicle_collection.vehicle_list)
        elif choice == 10:
            exit()
        else:
            print("Invalid choice")
# Calling main function
main()