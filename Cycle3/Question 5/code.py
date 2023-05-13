from tkinter import *
from tkinter import ttk

from numpy import delete
from car_class import *
from tkinter import filedialog
import pickle

#Constants
scr = Tk()
scr.geometry("990x400+40+50")
scr.configure(bg = "#202225")
scr.title("Vehicle Sale Data")
text= Label(scr, font=('Poppins',15,'bold'),text="VEHICLE DATA",bg="#202225",fg="white")
text.pack()
CarData = VehicleCollection() 
DataFrame = LabelFrame(scr,text="Datas",bg = "#2f3136",fg="white")
DataFrame.pack(expand="yes",side=RIGHT)
CarDisplay = ttk.Treeview(DataFrame)

def data_screen_frame():
    count=0
    CarDisplay['columns'] = ("EngNo","Model","Type","Mileage","Vendor","RegNo","Owner")
    CarDisplay.column("#0",width=0,minwidth=3)
    CarDisplay.column("EngNo",anchor = W,minwidth=10,width=50)
    CarDisplay.column('Model',anchor = W,minwidth=10,width=50)
    CarDisplay.column('Type',anchor = W,minwidth=10,width=50)
    CarDisplay.column('Mileage',anchor = W,minwidth=20,width=50)
    CarDisplay.column('Vendor',anchor = W,minwidth=20,width=50)
    CarDisplay.column('RegNo',anchor = W,minwidth=20,width=50)
    CarDisplay.column('Owner',anchor = W,minwidth=20,width=50)
    #setting the headings
    CarDisplay.heading("#0",text = " ",anchor=W )
    CarDisplay.heading("EngNo",text = "Engine No.",anchor = W)
    CarDisplay.heading("Model",text = "Model",anchor = W)
    CarDisplay.heading("Type",text ="Type",anchor = W)
    CarDisplay.heading("Mileage",text = "Mileage",anchor = W)
    CarDisplay.heading("Vendor",text = "Vendor",anchor = W)
    CarDisplay.heading("RegNo",text = "Reg. No.",anchor = W)
    CarDisplay.heading("Owner",text = "Owner",anchor = W)
    List_of_cars = CarData.vehicle_list
    for i in List_of_cars:
        show_Values = tuple(i)
        CarDisplay.insert(parent = "",index = 'end',values=show_Values)
    CarDisplay.pack()
#Creating a frame for the Input details
In_Frame = LabelFrame(scr,text = "Input",bg = "#2f3136",fg="white")
In_Frame.pack(fill="x",expand="yes",padx = 20)
In_EngNo = StringVar(None)
#Creating Labels and respective entry boxes
In_EngNo_Label = Label(In_Frame,text = "Engine No",bg='#2f3136',fg="white")
In_EngNo_Label.grid(row = 0,column=0,padx=10,pady=10)
In_EngNo = Entry(In_Frame)
In_EngNo.grid(row=0,column=1,padx=10,pady=10)

In_Model_Label = Label(In_Frame,text = "Model",bg='#2f3136',fg="white")
In_Model_Label.grid(row = 1,column=0,padx=10,pady=10)
In_Model = Entry(In_Frame)
In_Model.grid(row=1,column=1,padx=10,pady=10)

In_Type_Label = Label(In_Frame,text = "Type",bg='#2f3136',fg="white")
In_Type_Label.grid(row = 2,column=0,padx=10,pady=10)
In_Type = Entry(In_Frame)
In_Type.grid(row=2,column=1,padx=10,pady=10)

In_Mileage_Label = Label(In_Frame,text = "Mileage",bg='#2f3136',fg="white")
In_Mileage_Label.grid(row = 0,column=2,padx=10,pady=10)
In_Mileage = Entry(In_Frame)
In_Mileage.grid(row=0,column=3,padx=10,pady=10)

In_Vendor_Label = Label(In_Frame,text = "Vendor",bg='#2f3136',fg="white")
In_Vendor_Label.grid(row = 1,column=2,padx=10,pady=10)
In_Vendor = Entry(In_Frame)
In_Vendor.grid(row=1,column=3,padx=10,pady=10)

In_Regno_Label = Label(In_Frame,text = "Reg No",bg='#2f3136',fg="white")
In_Regno_Label.grid(row = 2,column=2,padx=10,pady=10)
In_RegNo = Entry(In_Frame)
In_RegNo.grid(row=2,column=3,padx=10,pady=10)

In_Owner_Label = Label(In_Frame,text = "Owner",bg='#2f3136',fg="white")
In_Owner_Label.grid(row = 4,column=0,padx=10,pady=10)
In_Owner = Entry(In_Frame)
In_Owner.grid(row=4,column=1,padx=10,pady=10)

def clear_inputs():
    #To clear the inputs on screen
    In_EngNo.delete(0,END)
    In_Model.delete(0,END)
    In_Type.delete(0,END)
    In_Mileage.delete(0,END)
    In_Vendor.delete(0,END)
    In_RegNo.delete(0,END)
    In_Owner.delete(0,END)

def add_to_entry_box():
    clear_inputs()
    #Select the record number
    sel_record = CarDisplay.focus()
    #Selecting values of the record
    rec_values = CarDisplay.item(sel_record,'values')
    #outputting to entry box
    In_EngNo.insert(0,rec_values[0])
    In_Model.insert(0,rec_values[1])
    In_Type.insert(0,rec_values[2])
    In_Mileage.insert(0,rec_values[3])
    In_Vendor.insert(0,rec_values[4])
    In_RegNo.insert(0,rec_values[5])
    In_Owner.insert(0,rec_values[6])

def Delete_record():
    sel_record = CarDisplay.focus()
    rec_values = CarDisplay.item(sel_record,'values')
    #To Remove Data from screen
    to_delete = CarDisplay.selection()[0]
    CarDisplay.delete(to_delete)
    #To remove from CarData
    CarData.Delete_car(rec_values[5])



def Add_the_record():
    add_data = (In_EngNo.get(),In_Model.get(),In_Type.get(),
        int(In_Mileage.get()),In_Vendor.get(),In_RegNo.get(),In_Owner.get())
    
    to_Add_Car = Vehicle(In_EngNo.get(),In_Model.get(),In_Type.get(),int(In_Mileage.get())
        ,In_Vendor.get(),In_RegNo.get(),In_Owner.get())
    CarData.add_vehicle(to_Add_Car)
    CarDisplay.insert(parent = "",index = 'end',values=add_data)
    clear_inputs

def Load_File():
    scr.filename = filedialog.askopenfilename(initialdir="/",
        title="Select Pickle File",filetypes=(("pickle files","*.dat"),#
                      ("All Files","*.*")))
    CarData.load_pickle(scr.filename)
    for i in CarData.vehicle_list:
        show_Values = tuple(i)
        CarDisplay.insert(parent = "",index = 'end',values=show_Values)
    
def Save_File():
    scr.filename = filedialog.askopenfilename(initialdir="/",
        title="Select pickle File",filetypes=(("File to save","data.dat"),#
                           ("All Files","*.*")))    
    CarData.store_pickle(scr.filename)

def Sort_mileage():
    #Sorting object data by Mileage
    CarData.sort_by_mileage()
    #Deleting items on window
    for data in CarDisplay.get_children():
        CarDisplay.delete(data)
    for i in CarData.vehicle_list:
        show_Values = tuple(i)
        CarDisplay.insert(parent = "",index = 'end',values=show_Values)
def Save_as_pdf():
    scr.filename = filedialog.askopenfilename(initialdir="/",
        title="Select Pdf File",filetypes=(("pdf files","*.pdf"),("All Files","*.*"))) 
    CarData.export_pdf(scr.filename)

def Buttons_Frame():
    ButtonFrame = LabelFrame(scr,text = "Options",bg = "grey")
    ButtonFrame.pack()

    AddRec_button = Button(ButtonFrame,text = "Add",command=Add_the_record,#
                              activebackground='#2f3136',bg='grey',fg="white")
    AddRec_button.grid(row=0,column=0,padx=10,pady=10)

    Modify_button = Button(ButtonFrame,text = "Modify",#
                               activebackground='#2f3136',bg='grey',fg="white")
    Modify_button.grid(row=1,column=0,padx=10,pady=10)

    Open_button = Button(ButtonFrame,text = "Open File",command=Load_File,#
                               activebackground='#2f3136',bg='grey',fg="white")
    Open_button.grid(row=2,column=0,padx=10,pady=10)

    Sort_button = Button(ButtonFrame,text = "Sort by Mileage",command=Sort_mileage,#
                                 activebackground='#2f3136',bg='grey',fg="white")
    Sort_button.grid(row=0,column=1,padx=10,pady=10)

    Delete_button = Button(ButtonFrame,text = "Delete Entry",command=Delete_record,#
                                    activebackground='#2f3136',bg='grey',fg="white")
    Delete_button.grid(row=1,column=1,padx=10,pady=10)

    Save_button = Button(ButtonFrame,text = "Save Data",command=Save_File,#
                                   activebackground='#2f3136',bg='grey',fg="white")
    Save_button.grid(row=2,column=1,padx=10,pady=10)

    Report_button = Button(ButtonFrame,text = "Save PDF",command=Save_as_pdf,#
                                         activebackground='#2f3136',bg='grey',fg="white")
    Report_button.grid(row=0,column=3,padx=10,pady=10)

    Show_button = Button(ButtonFrame,text = "Show Selection",command=add_to_entry_box,#
                    activebackground='#2f3136',bg='grey',fg="white")
    Show_button.grid(row=1,column=3,padx=10,pady=10)

    Clear_Button = Button(ButtonFrame,text = "Clear",command=clear_inputs,#
                                     activebackground='#2f3136',bg='grey',fg="white")
    Clear_Button.grid(row=2,column=3,padx=10,pady=10)

Buttons_Frame()
data_screen_frame() 
scr.mainloop()