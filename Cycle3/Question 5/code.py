from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfile
from tkinter.messagebox import showinfo
from tkinter.ttk import Style, Treeview
import pickle

vehicle_list = []
vehicle_attributes = ["owner_name", "vendor", "model", "vehicle_type", "registration_number", "engine_number", "mileage"]
vehicle_details = dict.fromkeys(vehicle_attributes, None)

def add_vehicle():
    global vehicle_list
    treeview.insert(parent='', index='end', text="", values=(owner_name.get(), vendor.get(), model.get(), vehicle_type.get(), registration_number.get(), engine_number.get(), mileage.get()))
    vehicle_details['owner_name'] = owner_name.get()
    vehicle_details['vendor'] = vendor.get()
    vehicle_details['model'] = model.get()
    vehicle_details['vehicle_type'] = vehicle_type.get()
    vehicle_details['registration_number'] = int(registration_number.get())
    vehicle_details['engine_number'] = int(engine_number.get())
    vehicle_details['mileage'] = float(mileage.get())
    vehicle_list.append(vehicle_details.copy())

def filter_vehicles():
    global vehicle_list
    if (owner_name.get() or vendor.get() or model.get() or vehicle_type.get() or mileage.get()):
        for item in treeview.get_children():
            treeview.delete(item)
    else:
        showinfo(title="Error", message="Give a Filter Key")
    if (owner_name.get()):
        filter_key = owner_name.get()
        for vehicle in vehicle_list:
            if vehicle['owner_name'] == filter_key:
                treeview.insert(parent='', index='end', text="", values=(vehicle['owner_name'], vehicle['vendor'], vehicle['model'], vehicle['vehicle_type'], vehicle['registration_number'], vehicle['engine_number'], vehicle['mileage']))
    elif (vendor.get()):
        filter_key = vendor.get()
        for vehicle in vehicle_list:
            if vehicle['vendor'] == filter_key:
                treeview.insert(parent='', index='end', text="", values=(vehicle['owner_name'], vehicle['vendor'], vehicle['model'], vehicle['vehicle_type'], vehicle['registration_number'], vehicle['engine_number'], vehicle['mileage']))
    elif (model.get()):
        filter_key = model.get()
        for vehicle in vehicle_list:
            if vehicle['model'] == filter_key:
                treeview.insert(parent='', index='end', text="", values=(vehicle['owner_name'], vehicle['vendor'], vehicle['model'], vehicle['vehicle_type'], vehicle['registration_number'], vehicle['engine_number'], vehicle['mileage']))
    elif (vehicle_type.get()):
        filter_key = vehicle_type.get()
        for vehicle in vehicle_list:
            if vehicle['vehicle_type'] == filter_key:
                treeview.insert(parent='', index='end', text="", values=(vehicle['owner_name'], vehicle['vendor'], vehicle['model'], vehicle['vehicle_type'], vehicle['registration_number'], vehicle['engine_number'], vehicle['mileage']))
    elif (mileage.get()):
        filter_key = float(mileage.get())
        for vehicle in vehicle_list:
            if vehicle['mileage'] == filter_key:
                treeview.insert(parent='', index='end', text="", values=(vehicle['owner_name'], vehicle['vendor'], vehicle['model'], vehicle['vehicle_type'], vehicle['registration_number'], vehicle['engine_number'], vehicle['mileage']))

def delete_vehicle():
   # Get selected item to Delete
    selection = treeview.selection()[0] 
    treeview.delete(selection)

def load_vehicles():
        # Clear the treeview list items
    for item in treeview.get_children():
        treeview.delete(item)

    # Clear the vehicle list
    global vehicle_list
    vehicle_list.clear()

    # Load vehicles from file
    try:
        filename = askopenfilename(defaultextension=".pkl", filetypes=[("Pickle Files", "*.pkl")])
        with open(filename, "rb") as file:
            vehicle_list = pickle.load(file)

        # Populate treeview with loaded data
        for vehicle in vehicle_list:
            treeview.insert(parent='', index='end', text="", values=(vehicle['owner_name'], vehicle['vendor'], vehicle['model'], vehicle['vehicle_type'], vehicle['registration_number'], vehicle['engine_number'], vehicle['mileage']))

    except Exception as e:
        showinfo(title="Error", message="Failed to load file: " + str(e))

def save_vehicles():
    # Get the file to save vehicles
    file = asksaveasfile(defaultextension=".pkl", filetypes=[("Pickle Files", "*.pkl")])
    if file:
        try:
            pickle.dump(vehicle_list, file)
            showinfo(title="Success", message="Vehicles saved successfully.")
        except Exception as e:
            showinfo(title="Error", message="Failed to save vehicles: " + str(e))

# Create GUI
root = Tk()
root.geometry("800x500")
root.title("Vehicle Management System")

# Create Style
style = Style()
style.configure("Treeview", rowheight=25)
style.configure("Treeview.Heading", font=("Arial", 12))

# Create Treeview
treeview = Treeview(root, columns=vehicle_attributes, show="headings")
treeview.heading("owner_name", text="Owner Name")
treeview.heading("vendor", text="Vendor")
treeview.heading("model", text="Model")
treeview.heading("vehicle_type", text="Vehicle Type")
treeview.heading("registration_number", text="Registration Number")
treeview.heading("engine_number", text="Engine Number")
treeview.heading("mileage", text="Mileage")
treeview.pack(side=LEFT, fill=BOTH, expand=True)

# Create Scrollbar
scrollbar = Scrollbar(root, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)
treeview.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=treeview.yview)

# Create Entry Fields
owner_name_label = Label(root, text="Owner Name: ")
owner_name_label.pack()
owner_name = Entry(root, width=30)
owner_name.pack()

vendor_label = Label(root, text="Vendor: ")
vendor_label.pack()
vendor = Entry(root, width=30)
vendor.pack()

model_label = Label(root, text="Model: ")
model_label.pack()
model = Entry(root, width=30)
model.pack()

vehicle_type_label = Label(root, text="Vehicle Type: ")
vehicle_type_label.pack()
vehicle_type = Entry(root, width=30)
vehicle_type.pack()

registration_number_label = Label(root, text="Registration Number: ")
registration_number_label.pack()
registration_number = Entry(root, width=30)
registration_number.pack()

engine_number_label = Label(root, text="Engine Number: ")
engine_number_label.pack()
engine_number = Entry(root, width=30)
engine_number.pack()

mileage_label = Label(root, text="Mileage: ")
mileage_label.pack()
mileage = Entry(root, width=30)
mileage.pack()

# Create Buttons
add_button = Button(root, text="Add Vehicle", command=add_vehicle)
add_button.pack()

filter_button = Button(root, text="Filter Vehicles", command=filter_vehicles)
filter_button.pack()

delete_button= Button(root, text="Delete Vehicle", command=delete_vehicle)
delete_button.pack()

clear_button = Button(root, text="Clear List", command=clear_list)
clear_button.pack()

load_button = Button(root, text="Load Vehicles", command=load_vehicles)
load_button.pack()

save_button = Button(root, text="Save Vehicles", command=save_vehicles)
save_button.pack()

root.mainloop()
