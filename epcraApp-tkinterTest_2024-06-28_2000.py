# -*- coding: utf-8 -*-
"""
Company:  NA
Title:  EPCRA Chemical Inventory Tracking App
Author:  K. Navagh, MS, ASP, CSP
Date created:  Tue Jun 11 17:44:53 2024
Date last updated:  2024-06-26

Summary:  Expansion of previous attempt at developing a comprehensive program
          for tracking the maximum onsite quantity of chemicals during a given
          year, tabulating the maximum onsite quantity of each chemical
          constituent by CAS number and flagging the quantities of constituents
          that require reporting to the EPA/DEC/emergency responders per the
          chemical list located in 40 CFR Part 355, Appendix A & B.  The file
          of reportable chemicals was taken from the website below.  The two
          appendices were translated into CSV files and processed with an R
          script to assess differences between the two appendices.  No
          differences were found.
          https://www.ecfr.gov/current/title-40/chapter-I/subchapter-J/part-355/
Update notes:  2024-06-26; have working GUI in program with popup box for
               confirming entries.  Still a problem with attempting to submit
               data without entering anything into the entry fields.  Working
               on correcting this now.  Still unsure about how to structure
               the functions in the Window class; just stuck all function in
               the __init__ function.  Want to break these out to separate
               functions for elegance.  Must think about function that compiles
               CAS data for all chemicals..  Unsure why float multiplying
               creates extended 90.899999 value for 900*10.1.
               Was able to create a separate function for populating the window
               initialized in __init__ but couldn't create a separate function
               for .grid_remove() frames and recalling popBlankWindow(); the
               code would get stuck in a loop and restart the kernal.  I also
               tried pulling on_select() and submitData() out into separate
               functions, but I couldn't call the entry widgets out of the
               frame they were bound in; that is I passed center_frame_right as
               an argument to the alternate function but I couldn't call the
               cas1NumEntry.get() using center_frame_right.cas1NumEntry.get();
               I may be able to get it to work if I passed each widget as an
               argument individually but that may be excessive.  I may also be
               able to bind them to the root, but I got confused passing the
               root between functions and rebinding it to self.  I'll try that
               again later.  Finally the epcraProc class is not really an
               object, it's just a library. Maybe I don't need a class for
               this.  I'll leave it for now to enable scalability.  One last
               thing; should probably integrate way to wipe text in fields
               away when the Next button is clicked.  Can do this with binding
               string to entry boxes.  Didn't need to do this for pulling data
               into the dict; attaching string objects into dict was making a
               dict of objects.  It was easier to use .get() from the widget
               itself.  Will bing strings that can be reset later.
Update notes:  2024-06-28; bound all widgets to root and pulled all functions
               out of popBlankWindow() function.  Passing self.root and
               rebinding it to self in alternate function worked well.  Had to
               use some lambda commands for expanding onclick event calling to
               functions while passing multiple arguments.  Got it to work.
               Was thinking about creating an array of widget objects in root
               along with array of strings so I can loop over array to grid
               and remove widgets, but that might make the code unnecessarily
               complicated.  Maybe later.
               
"""

# loading message
print("Loading... please wait")

# import packages, including tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import pandas as pandas
pandas.options.mode.chained_assignment = None
from pathlib import Path
from datetime import datetime
import os

# define main function
def main():
    
    # initialize route path
    dataDirUpdatefiles=Path("""C:/Users/kelna/Documents/pythonTest/datafiles/updatefiles""")
    dataDirDbfiles=Path("""C:/Users/kelna/Documents/pythonTest/datafiles/!PERM""")
    
    # initialize root and pass to Window class
    root = tk.Tk()
    window1 = Window(root, "EPCRA Chemical Tracking App", 675, 550, dataDirUpdatefiles, dataDirDbfiles)

    return None

# declare class/object for popup window
class Window:

    # define essential function
    def __init__(self, root, title, width, height, dataDirUpdatefiles, dataDirDbfiles):

        # declare self.root parameters
        self.root = root
        self.root.title(title)
        self.root.geometry('{}x{}'.format(width, height))
        
        # binding variables to the root
        self.root.width=width
        self.root.height=height
        self.root.dataDirUpdatefiles=dataDirUpdatefiles
        self.root.dataDirDbfiles=dataDirDbfiles

        # create frame rows
        self.root.top_frame = tk.LabelFrame(self.root, text="Enter information for newly received chemicals", width=width, height=20, pady=3)
        self.root.center_frame = tk.Frame(self.root, width=width, height=(height-70), padx=3, pady=3)
        self.root.btm_frame = tk.Frame(self.root, width=width, height=50, padx=8, pady=8)

        # declare layout for frame rows
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # grid top frame
        self.root.top_frame.grid(row=0, sticky="ew")

        # layout center_frame
        self.root.center_frame.grid_rowconfigure(1, weight=1)
        self.root.center_frame.grid_columnconfigure(2, weight=1)

        # populate window
        self.popBlankWindow(self.root)

        # run loop
        self.root.mainloop()

    # define function to populate window; this is the majority of the class
    def popBlankWindow(self,root):

        # bind root in function specific self
        self.root=root

        # load epcra data
        #
        # load base epcra inventory file
        filesArr = os.listdir(self.root.dataDirUpdatefiles)
        filesArr.sort(reverse=True)
        fileToOpen=self.root.dataDirUpdatefiles/filesArr[0]
        epcradat=pandas.read_csv(fileToOpen,sep=",",index_col=False)

        # grid center and bottom frame
        self.root.center_frame.grid(row=1, sticky="nsew")
        self.root.btm_frame.grid(row=2, sticky="se")

        # layout center_frame
        self.root.center_frame.grid_rowconfigure(1, weight=1)
        self.root.center_frame.grid_columnconfigure(2, weight=1)

        # add 2 frames in center
        self.root.center_frame.center_frame_left = tk.Frame(self.root.center_frame, width=350, height=(self.root.height-70), padx=3, pady=3)
        self.root.center_frame.center_frame_right = tk.Frame(self.root.center_frame, width=(self.root.width-350), height=(self.root.height-70), padx=3, pady=3)
        self.root.center_frame.center_frame_left.grid(row=1,column=1,sticky="nw")
        self.root.center_frame.center_frame_right.grid(row=1,column=2,sticky="nw")

        # layout center_frame_left
        self.root.center_frame.center_frame_left.grid_rowconfigure(12, weight=1)
        self.root.center_frame.center_frame_left.grid_columnconfigure(1, weight=1)

        # layout center_frame_right
        self.root.center_frame.center_frame_right.grid_rowconfigure(20, weight=1)
        self.root.center_frame.center_frame_right.grid_columnconfigure(2, weight=1)

        # layout btm_frame
        self.root.btm_frame.grid_rowconfigure(1, weight=1)
        self.root.btm_frame.grid_columnconfigure(2, weight=1)

        # declare widgets for center frame
        #
        # label widgets
        label1 = tk.Label(self.root.center_frame.center_frame_left, text="Chemical name: ")

        # combobox widgets
        comboBoxChem_values=list(epcradat.chemName.unique())
        comboBoxChem_values.sort()
        comboBoxChem_values.append("Not listed")
        self.root.comboBoxChem_selection=tk.StringVar(self.root)
        comboBoxChem=ttk.Combobox(self.root.center_frame.center_frame_left, textvariable=self.root.comboBoxChem_selection, values=comboBoxChem_values)
        comboBoxChem.name="cb1"
        comboBoxChem.bind("<<ComboboxSelected>>", lambda event: self.on_select(event,self.root,epcradat))

        # call to function for other widgets
        self.deckWidgets(self.root,epcradat)

        # grid first widgets (rest to be grid in on_select function)
        label1.grid(row=0, sticky="nw")
        comboBoxChem.grid(row=1, sticky="nw")
        
        # declare buttons for btm_frame
        submit_btn=tk.Button(self.root.btm_frame, text="Submit", width=10, command=lambda: self.submitData(self.root,epcradat))
        next_btn=tk.Button(self.root.btm_frame, text="Next Entry", width=10, command=lambda: self.depopFrame(self.root))
        
        # grid buttons
        submit_btn.grid(row=0, column=0, sticky="e")
        next_btn.grid(row=0, column=1, sticky="e")
        
        return None

    # function for declaring widgets for right frame
    def deckWidgets(self,root,epcradat):
        
        # bind root
        self.root=root

        # define functions to check values in entry fields
        def validate_int(char):
            if char!="":
                try:
                    int(char)
                except ValueError:
                    return False
                else:
                    return True
        def validate_float(char1,char2):
            if char1!="" and char2!="":
                try:
                    float(char1)
                except ValueError:
                    return False
                else:
                    return True

        # declare widgets for center frame
        #
        # label widgets
        self.root.center_frame.center_frame_right.label5 = tk.Label(self.root.center_frame.center_frame_right, text="Enter the chemical name below exactly as it appears in the SDS: ")
        self.root.center_frame.center_frame_right.label5b = tk.Label(self.root.center_frame.center_frame_right, text="SOME CHEMICAL NAME")
        self.root.center_frame.center_frame_right.label6 = tk.Label(self.root.center_frame.center_frame_right, text="Units: ")
        self.root.center_frame.center_frame_right.label6b = tk.Label(self.root.center_frame.center_frame_right, text="SOME UNITS")
        self.root.center_frame.center_frame_right.label7 = tk.Label(self.root.center_frame.center_frame_right, text="Onsite quantity before receiving: ")
        self.root.center_frame.center_frame_right.label8 = tk.Label(self.root.center_frame.center_frame_right, text="Quantity received: ")

        self.root.center_frame.center_frame_right.spacer4=tk.Label(self.root.center_frame.center_frame_right,text="")
        self.root.center_frame.center_frame_right.spacer5=tk.Label(self.root.center_frame.center_frame_right,text="")
        self.root.center_frame.center_frame_right.spacer6=tk.Label(self.root.center_frame.center_frame_right,text="")
        self.root.center_frame.center_frame_right.spacer7=tk.Label(self.root.center_frame.center_frame_right,text="")

        self.root.center_frame.center_frame_right.label9 = tk.Label(self.root.center_frame.center_frame_right, text="Enter all CAS numbers listed exactly as they are in the Chemical Composition section of the SDS.")
        self.root.center_frame.center_frame_right.spacer8=tk.Label(self.root.center_frame.center_frame_right,text="")

        self.root.center_frame.center_frame_right.label10 = tk.Label(self.root.center_frame.center_frame_right, text="CAS number:")
        self.root.center_frame.center_frame_right.label11 = tk.Label(self.root.center_frame.center_frame_right, text="Max of the % range for CAS:")

        self.root.center_frame.center_frame_right.cas1NumEntry_label=tk.Label(self.root.center_frame.center_frame_right, text=" ")
        self.root.center_frame.center_frame_right.cas1PercEntry_label=tk.Label(self.root.center_frame.center_frame_right, text=" ")

        self.root.center_frame.center_frame_right.cas2NumEntry_label=tk.Label(self.root.center_frame.center_frame_right, text=" ")
        self.root.center_frame.center_frame_right.cas2PercEntry_label=tk.Label(self.root.center_frame.center_frame_right, text=" ")

        self.root.center_frame.center_frame_right.cas3NumEntry_label=tk.Label(self.root.center_frame.center_frame_right, text=" ")
        self.root.center_frame.center_frame_right.cas3PercEntry_label=tk.Label(self.root.center_frame.center_frame_right, text=" ")

        self.root.center_frame.center_frame_right.cas4NumEntry_label=tk.Label(self.root.center_frame.center_frame_right, text=" ")
        self.root.center_frame.center_frame_right.cas4PercEntry_label=tk.Label(self.root.center_frame.center_frame_right, text=" ")

        self.root.center_frame.center_frame_right.cas5NumEntry_label=tk.Label(self.root.center_frame.center_frame_right, text=" ")
        self.root.center_frame.center_frame_right.cas5PercEntry_label=tk.Label(self.root.center_frame.center_frame_right, text=" ")

        # entry widgets
        self.root.center_frame.center_frame_right.chemNameEntryRec=tk.Entry(self.root.center_frame.center_frame_right,width=65)
        self.root.center_frame.center_frame_right.onsiteQuantEntryRec=tk.Entry(self.root.center_frame.center_frame_right, validate="key", validatecommand=(self.root.register(validate_int), "%S"))
        self.root.center_frame.center_frame_right.recvdQuantEntryRec=tk.Entry(self.root.center_frame.center_frame_right, validate="key", validatecommand=(self.root.register(validate_int), "%S"))

        self.root.center_frame.center_frame_right.cas1NumEntry=tk.Entry(self.root.center_frame.center_frame_right)
        self.root.center_frame.center_frame_right.cas1PercEntry=tk.Entry(self.root.center_frame.center_frame_right, validate="key", validatecommand=(self.root.register(validate_float), "%P", "%S"))

        self.root.center_frame.center_frame_right.cas2NumEntry=tk.Entry(self.root.center_frame.center_frame_right)
        self.root.center_frame.center_frame_right.cas2PercEntry=tk.Entry(self.root.center_frame.center_frame_right, validate="key", validatecommand=(self.root.register(validate_float), "%P", "%S"))

        self.root.center_frame.center_frame_right.cas3NumEntry=tk.Entry(self.root.center_frame.center_frame_right)
        self.root.center_frame.center_frame_right.cas3PercEntry=tk.Entry(self.root.center_frame.center_frame_right, validate="key", validatecommand=(self.root.register(validate_float), "%P", "%S"))

        self.root.center_frame.center_frame_right.cas4NumEntry=tk.Entry(self.root.center_frame.center_frame_right)
        self.root.center_frame.center_frame_right.cas4PercEntry=tk.Entry(self.root.center_frame.center_frame_right, validate="key", validatecommand=(self.root.register(validate_float), "%P", "%S"))

        self.root.center_frame.center_frame_right.cas5NumEntry=tk.Entry(self.root.center_frame.center_frame_right)
        self.root.center_frame.center_frame_right.cas5PercEntry=tk.Entry(self.root.center_frame.center_frame_right, validate="key", validatecommand=(self.root.register(validate_float), "%P", "%S"))

        # combobox widgets
        self.root.comboBoxUnitsRec_selection=tk.StringVar(self.root)
        self.root.center_frame.center_frame_right.comboBoxUnitsRec=ttk.Combobox(self.root.center_frame.center_frame_right, values=["Lbs","Gal","55gal Drums","Tons","Other"],textvariable=self.root.comboBoxUnitsRec_selection)
        self.root.center_frame.center_frame_right.comboBoxUnitsRec.name="cb3"
        self.root.center_frame.center_frame_right.comboBoxUnitsRec.bind("<<ComboboxSelected>>", lambda event: self.on_select(event,self.root,epcradat))

        return None

    # define function to get selection from combobox
    def on_select(self,event,root,epcradat):
 
        # bind root
        self.root=root
 
        # checking which combobox event is being handled
        if event.widget.name=="cb1":

            # if chem is selected, grid other widgets and destroy right frame widgets        
            if event.widget.get()!="Not listed":
        
                # destroy right frame widgets
                self.depopFrame(self.root)

                # adjust labels
                self.root.center_frame.center_frame_right.label5b.config(text=event.widget.get())
                unitsStr=epcradat.onsiteQuantUnits[epcradat.chemName==event.widget.get()].iloc[0]
                self.root.center_frame.center_frame_right.label6b.config(text=unitsStr)
                
                # adjust and grid the CAS widgets iteratively using a loop through the indices of the subset epcradat
                for indexlooper in range(len(epcradat.chemConstCas[epcradat.chemName==event.widget.get()])):
                    if(indexlooper==0):
                          self.root.center_frame.center_frame_right.cas1NumEntry_label.config(text=epcradat.chemConstCas[epcradat.chemName==event.widget.get()].iloc[indexlooper]) 
                          self.root.center_frame.center_frame_right.cas1PercEntry_label.config(text=epcradat.casPercent[epcradat.chemName==event.widget.get()].iloc[indexlooper])
                          self.root.center_frame.center_frame_right.cas1NumEntry_label.grid(row=15, column=0, sticky="nw")
                          self.root.center_frame.center_frame_right.cas1PercEntry_label.grid(row=15, column=1, sticky="nw")
                    if(indexlooper==1):
                          self.root.center_frame.center_frame_right.cas2NumEntry_label.config(text=epcradat.chemConstCas[epcradat.chemName==event.widget.get()].iloc[indexlooper]) 
                          self.root.center_frame.center_frame_right.cas2PercEntry_label.config(text=epcradat.casPercent[epcradat.chemName==event.widget.get()].iloc[indexlooper])
                          self.root.center_frame.center_frame_right.cas2NumEntry_label.grid(row=16, column=0, sticky="nw")
                          self.root.center_frame.center_frame_right.cas2PercEntry_label.grid(row=16, column=1, sticky="nw")
                    if(indexlooper==2):
                          self.root.center_frame.center_frame_right.cas3NumEntry_label.config(text=epcradat.chemConstCas[epcradat.chemName==event.widget.get()].iloc[indexlooper]) 
                          self.root.center_frame.center_frame_right.cas3PercEntry_label.config(text=epcradat.casPercent[epcradat.chemName==event.widget.get()].iloc[indexlooper])
                          self.root.center_frame.center_frame_right.cas3NumEntry_label.grid(row=17, column=0, sticky="nw")
                          self.root.center_frame.center_frame_right.cas3PercEntry_label.grid(row=17, column=1, sticky="nw")
                    if(indexlooper==3):
                          self.root.center_frame.center_frame_right.cas4NumEntry_label.config(text=epcradat.chemConstCas[epcradat.chemName==event.widget.get()].iloc[indexlooper]) 
                          self.root.center_frame.center_frame_right.cas4PercEntry_label.config(text=epcradat.casPercent[epcradat.chemName==event.widget.get()].iloc[indexlooper])
                          self.root.center_frame.center_frame_right.cas4NumEntry_label.grid(row=18, column=0, sticky="nw")
                          self.root.center_frame.center_frame_right.cas4PercEntry_label.grid(row=18, column=1, sticky="nw")
                    if(indexlooper==4):
                          self.root.center_frame.center_frame_right.cas5NumEntry_label.config(text=epcradat.chemConstCas[epcradat.chemName==event.widget.get()].iloc[indexlooper]) 
                          self.root.center_frame.center_frame_right.cas5PercEntry_label.config(text=epcradat.casPercent[epcradat.chemName==event.widget.get()].iloc[indexlooper])
                          self.root.center_frame.center_frame_right.cas5NumEntry_label.grid(row=19, column=0, sticky="nw")
                          self.root.center_frame.center_frame_right.cas5PercEntry_label.grid(row=19, column=1, sticky="nw")

                # grid right frame widgets
                self.root.center_frame.center_frame_right.label5.grid(row=0, column=0, columnspan=2, sticky="nw")
                self.root.center_frame.center_frame_right.label5b.grid(row=1, column=0, columnspan=2, sticky="nw")
                self.root.center_frame.center_frame_right.spacer4.grid(row=2, column=0, columnspan=2, sticky="nw")
                self.root.center_frame.center_frame_right.label6.grid(row=3, column=0, columnspan=2, sticky="nw")
                self.root.center_frame.center_frame_right.label6b.grid(row=4, column=0, columnspan=2, sticky="nw")
                self.root.center_frame.center_frame_right.spacer5.grid(row=5, column=0, columnspan=2, sticky="nw")
                self.root.center_frame.center_frame_right.label7.grid(row=6, column=0, columnspan=2, sticky="nw")
                self.root.center_frame.center_frame_right.onsiteQuantEntryRec.grid(row=7, column=0, columnspan=2, sticky="nw")
                self.root.center_frame.center_frame_right.spacer6.grid(row=8, column=0, columnspan=2, sticky="nw")
                self.root.center_frame.center_frame_right.label8.grid(row=9, column=0, columnspan=2, sticky="nw")
                self.root.center_frame.center_frame_right.recvdQuantEntryRec.grid(row=10, column=0, columnspan=2, sticky="nw")
                self.root.center_frame.center_frame_right.spacer7.grid(row=11, column=0, columnspan=2, sticky="nw")
                self.root.center_frame.center_frame_right.label9.grid(row=12, column=0, columnspan=2, sticky="nw")
                self.root.center_frame.center_frame_right.spacer8.grid(row=13, column=0, columnspan=2, sticky="nw")
                self.root.center_frame.center_frame_right.label10.grid(row=14, column=0, sticky="nw")
                self.root.center_frame.center_frame_right.label11.grid(row=14, column=1, sticky="nw")

            # if Not listed is selected, set up right frame widgets
            else:
        
                # destroy right frame widgets
                self.depopFrame(self.root)
        
                # grid right frame widgets
                self.root.center_frame.center_frame_right.label5.grid(row=0, column=0, columnspan=2, sticky="nw")
                self.root.center_frame.center_frame_right.chemNameEntryRec.grid(row=1, column=0, columnspan=2, sticky="nw")
                self.root.center_frame.center_frame_right.spacer4.grid(row=2, column=0, columnspan=2, sticky="nw")
                self.root.center_frame.center_frame_right.label6.grid(row=3, column=0, columnspan=2, sticky="nw")
                self.root.center_frame.center_frame_right.comboBoxUnitsRec.grid(row=4, column=0, columnspan=2, sticky="nw")
                self.root.center_frame.center_frame_right.spacer5.grid(row=5, column=0, columnspan=2, sticky="nw")
                self.root.center_frame.center_frame_right.label7.grid(row=6, column=0, columnspan=2, sticky="nw")
                self.root.center_frame.center_frame_right.onsiteQuantEntryRec.grid(row=7, column=0, columnspan=2, sticky="nw")
                self.root.center_frame.center_frame_right.spacer6.grid(row=8, column=0, columnspan=2, sticky="nw")
                self.root.center_frame.center_frame_right.label8.grid(row=9, column=0, columnspan=2, sticky="nw")
                self.root.center_frame.center_frame_right.recvdQuantEntryRec.grid(row=10, column=0, columnspan=2, sticky="nw")
                self.root.center_frame.center_frame_right.spacer7.grid(row=11, column=0, columnspan=2, sticky="nw")
                self.root.center_frame.center_frame_right.label9.grid(row=12, column=0, columnspan=2, sticky="nw")
                self.root.center_frame.center_frame_right.spacer8.grid(row=13, column=0, columnspan=2, sticky="nw")
                self.root.center_frame.center_frame_right.label10.grid(row=14, column=0, sticky="nw")
                self.root.center_frame.center_frame_right.label11.grid(row=14, column=1, sticky="nw")
                self.root.center_frame.center_frame_right.cas1NumEntry.grid(row=15, column=0, sticky="nw")
                self.root.center_frame.center_frame_right.cas1PercEntry.grid(row=15, column=1, sticky="nw")
                self.root.center_frame.center_frame_right.cas2NumEntry.grid(row=16, column=0, sticky="nw")
                self.root.center_frame.center_frame_right.cas2PercEntry.grid(row=16, column=1, sticky="nw")
                self.root.center_frame.center_frame_right.cas3NumEntry.grid(row=17, column=0, sticky="nw")
                self.root.center_frame.center_frame_right.cas3PercEntry.grid(row=17, column=1, sticky="nw")
                self.root.center_frame.center_frame_right.cas4NumEntry.grid(row=18, column=0, sticky="nw")
                self.root.center_frame.center_frame_right.cas4PercEntry.grid(row=18, column=1, sticky="nw")
                self.root.center_frame.center_frame_right.cas5NumEntry.grid(row=19, column=0, sticky="nw")
                self.root.center_frame.center_frame_right.cas5PercEntry.grid(row=19, column=1, sticky="nw")

        # checking which combobox event is being handled
        if event.widget.name=="cb3":
            self.root.center_frame.center_frame_right.label6.config(text="Units: " + event.widget.get())    
        
        return None

    # define function to capture all data, create dict and pass to other class
    # for processing when submit button is clicked
    def submitData(self,root,epcradat):

        # bind root
        self.root=root

        # logical to check if entry update or new entry is submit
        if(self.root.comboBoxChem_selection.get()=="Not listed"):

            # logical to check if data was entered
            if (self.root.center_frame.center_frame_right.onsiteQuantEntryRec.get()=="" or
                self.root.center_frame.center_frame_right.recvdQuantEntryRec.get()=="" or
                self.root.center_frame.center_frame_right.chemNameEntryRec.get()=="" or
                self.root.center_frame.center_frame_right.comboBoxUnitsRec_selection.get()==""):
                
                # message box
                mb.showinfo("Confirm entry","Chemical name, units, quantity onsite and\nquantity received must all be entered.")

            else:

                # gate check on CAS number entries
                casNumConfirmed=False

                # logical to check that CAS numbers were entered
                if(self.root.center_frame.center_frame_right.cas1NumEntry.get()=="" and
                   self.root.center_frame.center_frame_right.cas2NumEntry.get()=="" and
                   self.root.center_frame.center_frame_right.cas3NumEntry.get()=="" and
                   self.root.center_frame.center_frame_right.cas4NumEntry.get()=="" and
                   self.root.center_frame.center_frame_right.cas5NumEntry.get()=="" and
                   casNumConfirmed==False):

                    # message box confirming no CAS numbers
                    confRespCas1=mb.askyesno("Confirm entry","There were no CAS numbers entered.\nAre CAS numbers listed in the chemical composition section of the SDS?")
    
                    # logical checking on CAS numbers
                    if confRespCas1==False:
                        casNumConfirmed=True
                    if confRespCas1==True:
                        # message box
                        mb.showinfo("Confirm entry","Please input the CAS numbers from the SDS.")

                # logical checking on complete CAS entries
                if( (self.root.center_frame.center_frame_right.cas1NumEntry.get()!="" and self.root.center_frame.center_frame_right.cas1PercEntry.get()=="") or
                    (self.root.center_frame.center_frame_right.cas1NumEntry.get()=="" and self.root.center_frame.center_frame_right.cas1PercEntry.get()!="") or
                    (self.root.center_frame.center_frame_right.cas2NumEntry.get()!="" and self.root.center_frame.center_frame_right.cas2PercEntry.get()=="") or
                    (self.root.center_frame.center_frame_right.cas2NumEntry.get()=="" and self.root.center_frame.center_frame_right.cas2PercEntry.get()!="") or
                    (self.root.center_frame.center_frame_right.cas3NumEntry.get()!="" and self.root.center_frame.center_frame_right.cas3PercEntry.get()=="") or
                    (self.root.center_frame.center_frame_right.cas3NumEntry.get()=="" and self.root.center_frame.center_frame_right.cas3PercEntry.get()!="") or
                    (self.root.center_frame.center_frame_right.cas4NumEntry.get()!="" and self.root.center_frame.center_frame_right.cas4PercEntry.get()=="") or
                    (self.root.center_frame.center_frame_right.cas4NumEntry.get()=="" and self.root.center_frame.center_frame_right.cas4PercEntry.get()!="") or
                    (self.root.center_frame.center_frame_right.cas5NumEntry.get()!="" and self.root.center_frame.center_frame_right.cas5PercEntry.get()=="") or
                    (self.root.center_frame.center_frame_right.cas5NumEntry.get()=="" and self.root.center_frame.center_frame_right.cas5PercEntry.get()!="") ):

                        # message box
                        mb.showinfo("Confirm entry","Please input a CAS number AND a max % for each CAS entry.")

                else:
                    
                    # logical checking on complete CAS entries
                    if( (self.root.center_frame.center_frame_right.cas1NumEntry.get()!="" and self.root.center_frame.center_frame_right.cas1PercEntry.get()!="") or
                        (self.root.center_frame.center_frame_right.cas2NumEntry.get()!="" and self.root.center_frame.center_frame_right.cas2PercEntry.get()!="") or
                        (self.root.center_frame.center_frame_right.cas3NumEntry.get()!="" and self.root.center_frame.center_frame_right.cas3PercEntry.get()!="") or
                        (self.root.center_frame.center_frame_right.cas4NumEntry.get()!="" and self.root.center_frame.center_frame_right.cas4PercEntry.get()!="") or
                        (self.root.center_frame.center_frame_right.cas5NumEntry.get()!="" and self.root.center_frame.center_frame_right.cas5PercEntry.get()!="") ):
                        
                            casNumConfirmed=True

                if casNumConfirmed==True:

                    # gather all entries
                    casNumArr=[self.root.center_frame.center_frame_right.cas1NumEntry.get(),
                               self.root.center_frame.center_frame_right.cas2NumEntry.get(),
                               self.root.center_frame.center_frame_right.cas3NumEntry.get(),
                               self.root.center_frame.center_frame_right.cas4NumEntry.get(),
                               self.root.center_frame.center_frame_right.cas5NumEntry.get()]
                    casPercArr=[self.root.center_frame.center_frame_right.cas1PercEntry.get(),
                                self.root.center_frame.center_frame_right.cas2PercEntry.get(),
                                self.root.center_frame.center_frame_right.cas3PercEntry.get(),
                                self.root.center_frame.center_frame_right.cas4PercEntry.get(),
                                self.root.center_frame.center_frame_right.cas5PercEntry.get()]
                    df_chemName=[self.root.center_frame.center_frame_right.chemNameEntryRec.get()]*len(casNumArr)
                    df_onsiteQuantUnits=[self.root.comboBoxUnitsRec_selection.get()]*len(casNumArr)
                    df_onsiteQuant=[(int(self.root.center_frame.center_frame_right.onsiteQuantEntryRec.get())+int(self.root.center_frame.center_frame_right.recvdQuantEntryRec.get()))]*len(casNumArr)
                    df_onsiteQuant_date=["NA"]*len(casNumArr)
                    df_maxOnsiteQuant=[(int(self.root.center_frame.center_frame_right.onsiteQuantEntryRec.get())+int(self.root.center_frame.center_frame_right.recvdQuantEntryRec.get()))]*len(casNumArr)
                    df_maxOnsiteQuant_date=["NA"]*len(casNumArr)
                    df_casQuant=["NA"]*len(casNumArr)
                    df_ehsFlag=["NA"]*len(casNumArr)
                    df_reportFlag=["NA"]*len(casNumArr)
                    
                    # set up dict
                    df_dict={'chemName':df_chemName,
                            'onsiteQuantUnits':df_onsiteQuantUnits,
                            'onsiteQuant':df_onsiteQuant,
                            'onsiteQuant_date':df_onsiteQuant_date,
                            'maxOnsiteQuant':df_maxOnsiteQuant,
                            'maxOnsiteQuant_date':df_maxOnsiteQuant_date,
                            'chemConstCas':casNumArr,
                            'casPercent':casPercArr,
                            'casQuant':df_casQuant,
                            'ehsFlag':df_ehsFlag,
                            'reportFlag':df_reportFlag}
                    
                    # code for confirmatory popup box
                    popuptextNL=("Please confirm the information that you entered\n\n"+
                        "Chemical name: "+df_dict["chemName"][0]+"\n"+
                        "Units: "+df_dict["onsiteQuantUnits"][0]+"\n"+
                        "Onsite qty: "+str(self.root.center_frame.center_frame_right.onsiteQuantEntryRec.get())+"\n"+
                        "Recvd qty: "+str(self.root.center_frame.center_frame_right.recvdQuantEntryRec.get())+"\n\n"+
                        "CAS #1: "+df_dict["chemConstCas"][0]+"; Max CAS %: "+str(df_dict["casPercent"][0])+"\n"+
                        "CAS #2: "+df_dict["chemConstCas"][1]+"; Max CAS %: "+str(df_dict["casPercent"][1])+"\n"+
                        "CAS #3: "+df_dict["chemConstCas"][2]+"; Max CAS %: "+str(df_dict["casPercent"][2])+"\n"+
                        "CAS #4: "+df_dict["chemConstCas"][3]+"; Max CAS %: "+str(df_dict["casPercent"][3])+"\n"+
                        "CAS #5: "+df_dict["chemConstCas"][4]+"; Max CAS %: "+str(df_dict["casPercent"][4]))
                    confResp=mb.askyesno("Confirm entry",popuptextNL)
                    if confResp==True:
                    
                        # send dict to other class
                        EpcraProc(df_dict,epcradat,self.root.dataDirUpdatefiles,self.root.dataDirDbfiles)
                        mb.showinfo("Confirm entry","Entry has been saved.")
        
                    else:
                        mb.showinfo("Confirm entry","Please revise entry and resubmit.")
    
        else:

            # logical to check if data was entered
            if (self.root.center_frame.center_frame_right.onsiteQuantEntryRec.get()=="" or
                self.root.center_frame.center_frame_right.recvdQuantEntryRec.get()==""):
                
                # message box
                mb.showinfo("Confirm entry","Quantity onsite and quantity received must be entered.")

            else:

                # set up dict
                df_dict={'chemName':self.root.comboBoxChem_selection.get(),
                        'onsiteQuantUnits':epcradat.onsiteQuantUnits[epcradat.chemName==self.root.comboBoxChem_selection.get()].iloc[0],
                        'onsiteQuant':(int(self.root.center_frame.center_frame_right.onsiteQuantEntryRec.get())+int(self.root.center_frame.center_frame_right.recvdQuantEntryRec.get()))}
                
                # code for confirmatory popup box
                popuptextLS=("Please confirm the information that you entered\n\n"+
                    "Chemical name: "+df_dict["chemName"]+"\n"+
                    "Units: "+df_dict["onsiteQuantUnits"]+"\n"+
                    "Onsite qty: "+str(self.root.center_frame.center_frame_right.onsiteQuantEntryRec.get())+"\n"+
                    "Recvd qty: "+str(self.root.center_frame.center_frame_right.recvdQuantEntryRec.get())+"\n\n")
                confResp=mb.askyesno("Confirm entry",popuptextLS)
                if confResp==True:
    
                    # send dict to other class
                    EpcraProc(df_dict,epcradat,self.root.dataDirUpdatefiles,self.root.dataDirDbfiles)
                    mb.showinfo("Confirm entry","Entry has been saved.")
    
                else:
                    mb.showinfo("Confirm entry","Please revise entry and resubmit.")

        return None

    # define function to depop frame
    def depopFrame(self,root):
        
        # bind root
        self.root=root
        
        # destroy right frame widgets
        self.root.center_frame.center_frame_right.label5.grid_remove()
        self.root.center_frame.center_frame_right.chemNameEntryRec.grid_remove()
        self.root.center_frame.center_frame_right.spacer4.grid_remove()
        self.root.center_frame.center_frame_right.label6.grid_remove()
        self.root.center_frame.center_frame_right.comboBoxUnitsRec.grid_remove()
        self.root.center_frame.center_frame_right.spacer5.grid_remove()
        self.root.center_frame.center_frame_right.label7.grid_remove()
        self.root.center_frame.center_frame_right.onsiteQuantEntryRec.grid_remove()
        self.root.center_frame.center_frame_right.spacer6.grid_remove()
        self.root.center_frame.center_frame_right.label8.grid_remove()
        self.root.center_frame.center_frame_right.recvdQuantEntryRec.grid_remove()
        self.root.center_frame.center_frame_right.spacer7.grid_remove()
        self.root.center_frame.center_frame_right.label9.grid_remove()
        self.root.center_frame.center_frame_right.spacer8.grid_remove()
        self.root.center_frame.center_frame_right.label10.grid_remove()
        self.root.center_frame.center_frame_right.label11.grid_remove()
        self.root.center_frame.center_frame_right.cas1NumEntry.grid_remove()
        self.root.center_frame.center_frame_right.cas1PercEntry.grid_remove()
        self.root.center_frame.center_frame_right.cas2NumEntry.grid_remove()
        self.root.center_frame.center_frame_right.cas2PercEntry.grid_remove()
        self.root.center_frame.center_frame_right.cas3NumEntry.grid_remove()
        self.root.center_frame.center_frame_right.cas3PercEntry.grid_remove()
        self.root.center_frame.center_frame_right.cas4NumEntry.grid_remove()
        self.root.center_frame.center_frame_right.cas4PercEntry.grid_remove()
        self.root.center_frame.center_frame_right.cas5NumEntry.grid_remove()
        self.root.center_frame.center_frame_right.cas5PercEntry.grid_remove()
        self.root.center_frame.center_frame_right.label5b.grid_remove()
        self.root.center_frame.center_frame_right.label6b.grid_remove()
        self.root.center_frame.center_frame_right.cas1NumEntry_label.grid_remove()
        self.root.center_frame.center_frame_right.cas1PercEntry_label.grid_remove()
        self.root.center_frame.center_frame_right.cas2NumEntry_label.grid_remove()
        self.root.center_frame.center_frame_right.cas2PercEntry_label.grid_remove()
        self.root.center_frame.center_frame_right.cas3NumEntry_label.grid_remove()
        self.root.center_frame.center_frame_right.cas3PercEntry_label.grid_remove()
        self.root.center_frame.center_frame_right.cas4NumEntry_label.grid_remove()
        self.root.center_frame.center_frame_right.cas4PercEntry_label.grid_remove()
        self.root.center_frame.center_frame_right.cas5NumEntry_label.grid_remove()
        self.root.center_frame.center_frame_right.cas5PercEntry_label.grid_remove()
        
        # clear entry widget entries
        self.root.center_frame.center_frame_right.chemNameEntryRec.delete(0,"end")
        self.root.center_frame.center_frame_right.onsiteQuantEntryRec.delete(0,"end")
        self.root.center_frame.center_frame_right.recvdQuantEntryRec.delete(0,"end")
        self.root.center_frame.center_frame_right.cas1NumEntry.delete(0,"end")
        self.root.center_frame.center_frame_right.cas1PercEntry.delete(0,"end")
        self.root.center_frame.center_frame_right.cas2NumEntry.delete(0,"end")
        self.root.center_frame.center_frame_right.cas2PercEntry.delete(0,"end")
        self.root.center_frame.center_frame_right.cas3NumEntry.delete(0,"end")
        self.root.center_frame.center_frame_right.cas3PercEntry.delete(0,"end")
        self.root.center_frame.center_frame_right.cas4NumEntry.delete(0,"end")
        self.root.center_frame.center_frame_right.cas4PercEntry.delete(0,"end")
        self.root.center_frame.center_frame_right.cas5NumEntry.delete(0,"end")
        self.root.center_frame.center_frame_right.cas5PercEntry.delete(0,"end")
        self.root.center_frame.center_frame_right.label6.config(text="Units:")

        return None

    pass

# declare class for saving data into epcra dataframe
class EpcraProc:   

    # define essential function
    def __init__(self,df_dict,epcradat,dataDirUpdatefiles,dataDirDbfiles):
        
        # load base epcra inventory file
        fileToOpen1=dataDirDbfiles/"stackEpcraDatabases_2024-06-21.csv"
        epcra_refdb=pandas.read_csv(fileToOpen1,sep=",",index_col=False)
        
        # logic to check which funcion to use for df_dict
        if len(df_dict)>1:
            self.addNewEntry(df_dict,epcradat,dataDirUpdatefiles,epcra_refdb)
        else:
            self.updateData(df_dict,epcradat,dataDirUpdatefiles,epcra_refdb)
        
        return None

    # define function to process new data
    def addNewEntry(df_dict,epcradat,dataDirUpdatefiles,epcra_refdb):

        # gen dataframe from dict
        epcra_copy1_aug0=pandas.DataFrame(df_dict)
        
        # subset dataframe to remove empty entries
        epcra_copy1_aug1=epcra_copy1_aug0[epcra_copy1_aug0.casPercent!=""]
        
        # convert strings to floats
        for convLooper in epcra_copy1_aug1.casPercent:
            epcra_copy1_aug1.casPercent[epcra_copy1_aug1.casPercent==convLooper]=float(convLooper)
        
        # calculate the casQuant vector
        epcra_copy1_aug1.casQuant=epcra_copy1_aug1.maxOnsiteQuant*(epcra_copy1_aug1.casPercent*0.01)
        
        # add time to entry
        epcra_copy1_aug1.onsiteQuant_date=datetime.now()
        epcra_copy1_aug1.maxOnsiteQuant_date=datetime.now()

        # update flags
        for casLooper in epcra_copy1_aug1.chemConstCas:
            sub_df=epcra_refdb[epcra_refdb.casNum.str.contains(casLooper)]
            if len(sub_df.index)>0:
                epcra_copy1_aug1.ehsFlag[epcra_copy1_aug1.chemConstCas==casLooper]="FLAG"
                if(epcra_copy1_aug1.maxOnsiteQuant[epcra_copy1_aug1.chemConstCas==casLooper].iloc[0]>=epcra_refdb.repQuant[epcra_refdb.casNum==casLooper].iloc[0]):
                    epcra_copy1_aug1.reportFlag[epcra_copy1_aug1.chemConstCas==casLooper]="REPORT"
        
        # remove data from base epcra file, concat new df in and save
        epcradat_copy=pandas.concat([epcradat,epcra_copy1_aug1])
        filename="epcraTest_"+datetime.now().strftime("%Y%m%d-%H%M%S")+".csv"
        fileToSave=dataDirUpdatefiles/filename
        epcradat_copy.to_csv(fileToSave,sep=',',index=False)
        
        return None

    # define function to updata database
    def updateData(df_dict,epcradat,dataDirUpdatefiles,epcra_refdb):
        
        # subset out chem dataframe
        chemsub_df=epcradat[epcradat["chemName"].str.contains(df_dict["chemName"])]
        
        # update subbed dataframe
        chemsub_df.onsiteQuant=df_dict["onsiteQuant"]
        chemsub_df.onsiteQuant_date=datetime.now()
        
        # update maxOnsiteQuant
        if(chemsub_df.onsiteQuant.iloc[0]>chemsub_df.maxOnsiteQuant.iloc[0]):
            chemsub_df.maxOnsiteQuant=chemsub_df.onsiteQuant
            chemsub_df.maxOnsiteQuant_date=datetime.now() 
            chemsub_df.casQuant=chemsub_df.maxOnsiteQuant*(chemsub_df.casPercent*0.01)

        # update flags
        for casLooper in chemsub_df.chemConstCas:
            sub_df=epcra_refdb[epcra_refdb.casNum.str.contains(casLooper)]
            if len(sub_df.index)>0:
                chemsub_df.ehsFlag[chemsub_df.chemConstCas==casLooper]="FLAG"
                if(chemsub_df.maxOnsiteQuant[chemsub_df.chemConstCas==casLooper].iloc[0]>=epcra_refdb.repQuant[epcra_refdb.casNum==casLooper].iloc[0]):
                    chemsub_df.reportFlag[chemsub_df.chemConstCas==casLooper]="REPORT"

        # remove data from base epcra file, concat new df in and save
        epcradat_copy=epcradat.copy()
        epcradat_copy=epcradat_copy[(epcradat_copy.chemName!=df_dict["chemName"])]
        epcradat_copy2=pandas.concat([epcradat_copy,chemsub_df])
        filename="epcraTest_"+datetime.now().strftime("%Y%m%d-%H%M%S")+".csv"
        fileToSave=dataDirUpdatefiles/filename
        epcradat_copy2.to_csv(fileToSave,sep=',',index=False)

        return None
    
    pass


# initial processing point
if __name__ == "__main__":
    main()
