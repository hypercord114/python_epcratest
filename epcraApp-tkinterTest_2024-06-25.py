# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 17:44:53 2024

@author: kelna
"""

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
    dataDir=Path("""C:/Users/kelna/Documents/pythonTest/datafiles/updatefiles""")

    # load base epcra inventory file
    filesArr = os.listdir(dataDir)
    filesArr.sort(reverse=True)
    fileToOpen=dataDir/filesArr[0]
    epcra_raw=pandas.read_csv(fileToOpen,sep=",",index_col=False)
    epcra_copy1=epcra_raw.copy()
    
    root = tk.Tk()
    window1 = Window(root, "EPCRA Chemical Tracking App", 675, 550,epcra_copy1)
    return None

# declare class/object for popup window
class Window:
    
    # define essential function
    def __init__(self, root, title, width, height, epcradat):

        # define function to check values in Entry boxes
        def validate_int(char):
            if char!="":
                try:
                    int(char)
                except ValueError:
                    return False
                else:
                    return True
        def validate_float(char):
            if char!="":
                try:
                    float(char)
                except ValueError:
                    return False
                else:
                    return True

        # define function to get selection from combobox
        def on_select(event):
    
            # checking which combobox event is being handled
            if event.widget.name=="cb1":

                # if chem is selected, grid other widgets and destroy right frame widgets        
                if event.widget.get()!="Not listed":
            
                    # destroy right frame widgets
                    label5.grid_remove()
                    chemNameEntryRec.grid_remove()
                    spacer4.grid_remove()
                    label6.grid_remove()
                    comboBoxUnitsRec.grid_remove()
                    spacer5.grid_remove()
                    label7.grid_remove()
                    onsiteQuantEntryRec.grid_remove()
                    spacer6.grid_remove()
                    label8.grid_remove()
                    recvdQuantEntryRec.grid_remove()
                    spacer7.grid_remove()
                    label9.grid_remove()
                    spacer8.grid_remove()
                    label10.grid_remove()
                    label11.grid_remove()
                    cas1NumEntry.grid_remove()
                    cas1PercEntry.grid_remove()
                    cas2NumEntry.grid_remove()
                    cas2PercEntry.grid_remove()
                    cas3NumEntry.grid_remove()
                    cas3PercEntry.grid_remove()
                    cas4NumEntry.grid_remove()
                    cas4PercEntry.grid_remove()
                    cas5NumEntry.grid_remove()
                    cas5PercEntry.grid_remove()
                    
                    label5b.grid_remove()
                    label6b.grid_remove()
                    cas1NumEntry_label.grid_remove()
                    cas1PercEntry_label.grid_remove()
                    cas2NumEntry_label.grid_remove()
                    cas2PercEntry_label.grid_remove()
                    cas3NumEntry_label.grid_remove()
                    cas3PercEntry_label.grid_remove()
                    cas4NumEntry_label.grid_remove()
                    cas4PercEntry_label.grid_remove()
                    cas5NumEntry_label.grid_remove()
                    cas5PercEntry_label.grid_remove()
                    

                    # adjust labels
                    label5b.config(text=event.widget.get())
                    unitsStr=epcradat.onsiteQuantUnits[epcradat.chemName==event.widget.get()].iloc[0]
                    label6b.config(text=unitsStr)
                    
                    for indexlooper in range(len(epcradat.chemConstCas[epcradat.chemName==event.widget.get()])):
                    #for indexlooper in range(epcradat.chemConstCas[epcradat.chemName==event.widget.get()]):
                    #for indexlooper in [0:len(epcradat.chemConstCas[epcradat.chemName==event.widget.get()].index)]:
                        if(indexlooper==0):
                              cas1NumEntry_label.config(text=epcradat.chemConstCas[epcradat.chemName==event.widget.get()].iloc[indexlooper]) 
                              cas1PercEntry_label.config(text=epcradat.casPercent[epcradat.chemName==event.widget.get()].iloc[indexlooper])
                              cas1NumEntry_label.grid(row=15, column=0, sticky="nw")
                              cas1PercEntry_label.grid(row=15, column=1, sticky="nw")
                        if(indexlooper==1):
                              cas2NumEntry_label.config(text=epcradat.chemConstCas[epcradat.chemName==event.widget.get()].iloc[indexlooper]) 
                              cas2PercEntry_label.config(text=epcradat.casPercent[epcradat.chemName==event.widget.get()].iloc[indexlooper])
                              cas2NumEntry_label.grid(row=16, column=0, sticky="nw")
                              cas2PercEntry_label.grid(row=16, column=1, sticky="nw")
                        if(indexlooper==2):
                              cas3NumEntry_label.config(text=epcradat.chemConstCas[epcradat.chemName==event.widget.get()].iloc[indexlooper]) 
                              cas3PercEntry_label.config(text=epcradat.casPercent[epcradat.chemName==event.widget.get()].iloc[indexlooper])
                              cas3NumEntry_label.grid(row=17, column=0, sticky="nw")
                              cas3PercEntry_label.grid(row=17, column=1, sticky="nw")
                        if(indexlooper==3):
                              cas4NumEntry_label.config(text=epcradat.chemConstCas[epcradat.chemName==event.widget.get()].iloc[indexlooper]) 
                              cas4PercEntry_label.config(text=epcradat.casPercent[epcradat.chemName==event.widget.get()].iloc[indexlooper])
                              cas4NumEntry_label.grid(row=18, column=0, sticky="nw")
                              cas4PercEntry_label.grid(row=18, column=1, sticky="nw")
                        if(indexlooper==4):
                              cas5NumEntry_label.config(text=epcradat.chemConstCas[epcradat.chemName==event.widget.get()].iloc[indexlooper]) 
                              cas5PercEntry_label.config(text=epcradat.casPercent[epcradat.chemName==event.widget.get()].iloc[indexlooper])
                              cas5NumEntry_label.grid(row=19, column=0, sticky="nw")
                              cas5PercEntry_label.grid(row=19, column=1, sticky="nw")

                    ##for indexlooper in range(len(epcradat.chemConstCas[epcradat.chemName==event.widget.get()])):
                    #for indexlooper, iloclooper in range(epcradat.chemConstCas[epcradat.chemName==event.widget.get()]):
                    ##for indexlooper in [0:len(epcradat.chemConstCas[epcradat.chemName==event.widget.get()].index)]:
                    #    if(indexlooper==0):
                    #          cas1NumEntry_label.config(text=epcradat.chemConstCas[epcradat.chemName==event.widget.get()].iloc[iloclooper]) 
                    #          cas1PercEntry_label.config(text=epcradat.casPercent[epcradat.chemName==event.widget.get()].iloc[iloclooper])
                    #          cas1NumEntry_label.grid(row=15, column=0, sticky="nw")
                    #          cas1PercEntry_label.grid(row=15, column=1, sticky="nw")
                    #    if(indexlooper==1):
                    #          cas2NumEntry_label.config(text=epcradat.chemConstCas[epcradat.chemName==event.widget.get()].iloc[iloclooper]) 
                    #          cas2PercEntry_label.config(text=epcradat.casPercent[epcradat.chemName==event.widget.get()].iloc[iloclooper])
                    #          cas2NumEntry_label.grid(row=16, column=0, sticky="nw")
                    #          cas2PercEntry_label.grid(row=16, column=1, sticky="nw")
                    #    if(indexlooper==2):
                    #          cas3NumEntry_label.config(text=epcradat.chemConstCas[epcradat.chemName==event.widget.get()].iloc[iloclooper]) 
                    #          cas3PercEntry_label.config(text=epcradat.casPercent[epcradat.chemName==event.widget.get()].iloc[iloclooper])
                    #          cas3NumEntry_label.grid(row=17, column=0, sticky="nw")
                    #          cas3PercEntry_label.grid(row=17, column=1, sticky="nw")
                    #    if(indexlooper==3):
                    #          cas4NumEntry_label.config(text=epcradat.chemConstCas[epcradat.chemName==event.widget.get()].iloc[iloclooper]) 
                    #          cas4PercEntry_label.config(text=epcradat.casPercent[epcradat.chemName==event.widget.get()].iloc[iloclooper])
                    #          cas4NumEntry_label.grid(row=18, column=0, sticky="nw")
                    #          cas4PercEntry_label.grid(row=18, column=1, sticky="nw")
                    #    if(indexlooper==4):
                    #          cas5NumEntry_label.config(text=epcradat.chemConstCas[epcradat.chemName==event.widget.get()].iloc[iloclooper]) 
                    #          cas5PercEntry_label.config(text=epcradat.casPercent[epcradat.chemName==event.widget.get()].iloc[iloclooper])
                    #          cas5NumEntry_label.grid(row=19, column=0, sticky="nw")
                    #          cas5PercEntry_label.grid(row=19, column=1, sticky="nw")

                    # grid right frame widgets
                    label5.grid(row=0, column=0, columnspan=2, sticky="nw")
                    label5b.grid(row=1, column=0, columnspan=2, sticky="nw")
                    spacer4.grid(row=2, column=0, columnspan=2, sticky="nw")
                    label6.grid(row=3, column=0, columnspan=2, sticky="nw")
                    label6b.grid(row=4, column=0, columnspan=2, sticky="nw")
                    spacer5.grid(row=5, column=0, columnspan=2, sticky="nw")
                    label7.grid(row=6, column=0, columnspan=2, sticky="nw")
                    onsiteQuantEntryRec.grid(row=7, column=0, columnspan=2, sticky="nw")
                    spacer6.grid(row=8, column=0, columnspan=2, sticky="nw")
                    label8.grid(row=9, column=0, columnspan=2, sticky="nw")
                    recvdQuantEntryRec.grid(row=10, column=0, columnspan=2, sticky="nw")
                    spacer7.grid(row=11, column=0, columnspan=2, sticky="nw")
                    label9.grid(row=12, column=0, columnspan=2, sticky="nw")
                    spacer8.grid(row=13, column=0, columnspan=2, sticky="nw")
                    label10.grid(row=14, column=0, sticky="nw")
                    label11.grid(row=14, column=1, sticky="nw")

                # if Not listed is selected, set up right frame widgets
                else:

                    # adjust label1
                    #label1.config(text="Chemical name: NA")
            
                    # destroy right frame widgets
                    label5.grid_remove()
                    chemNameEntryRec.grid_remove()
                    spacer4.grid_remove()
                    label6.grid_remove()
                    comboBoxUnitsRec.grid_remove()
                    spacer5.grid_remove()
                    label7.grid_remove()
                    onsiteQuantEntryRec.grid_remove()
                    spacer6.grid_remove()
                    label8.grid_remove()
                    recvdQuantEntryRec.grid_remove()
                    spacer7.grid_remove()
                    label9.grid_remove()
                    spacer8.grid_remove()
                    label10.grid_remove()
                    label11.grid_remove()
                    cas1NumEntry.grid_remove()
                    cas1PercEntry.grid_remove()
                    cas2NumEntry.grid_remove()
                    cas2PercEntry.grid_remove()
                    cas3NumEntry.grid_remove()
                    cas3PercEntry.grid_remove()
                    cas4NumEntry.grid_remove()
                    cas4PercEntry.grid_remove()
                    cas5NumEntry.grid_remove()
                    cas5PercEntry.grid_remove()
            
                    # grid right frame widgets
                    label5.grid(row=0, column=0, columnspan=2, sticky="nw")
                    chemNameEntryRec.grid(row=1, column=0, columnspan=2, sticky="nw")
                    spacer4.grid(row=2, column=0, columnspan=2, sticky="nw")
                    label6.grid(row=3, column=0, columnspan=2, sticky="nw")
                    comboBoxUnitsRec.grid(row=4, column=0, columnspan=2, sticky="nw")
                    spacer5.grid(row=5, column=0, columnspan=2, sticky="nw")
                    label7.grid(row=6, column=0, columnspan=2, sticky="nw")
                    onsiteQuantEntryRec.grid(row=7, column=0, columnspan=2, sticky="nw")
                    spacer6.grid(row=8, column=0, columnspan=2, sticky="nw")
                    label8.grid(row=9, column=0, columnspan=2, sticky="nw")
                    recvdQuantEntryRec.grid(row=10, column=0, columnspan=2, sticky="nw")
                    spacer7.grid(row=11, column=0, columnspan=2, sticky="nw")
                    label9.grid(row=12, column=0, columnspan=2, sticky="nw")
                    spacer8.grid(row=13, column=0, columnspan=2, sticky="nw")
                    label10.grid(row=14, column=0, sticky="nw")
                    label11.grid(row=14, column=1, sticky="nw")
                    cas1NumEntry.grid(row=15, column=0, sticky="nw")
                    cas1PercEntry.grid(row=15, column=1, sticky="nw")
                    cas2NumEntry.grid(row=16, column=0, sticky="nw")
                    cas2PercEntry.grid(row=16, column=1, sticky="nw")
                    cas3NumEntry.grid(row=17, column=0, sticky="nw")
                    cas3PercEntry.grid(row=17, column=1, sticky="nw")
                    cas4NumEntry.grid(row=18, column=0, sticky="nw")
                    cas4PercEntry.grid(row=18, column=1, sticky="nw")
                    cas5NumEntry.grid(row=19, column=0, sticky="nw")
                    cas5PercEntry.grid(row=19, column=1, sticky="nw")

            # checking which combobox event is being handled
            if event.widget.name=="cb3":
                label6.config(text="Units: " + event.widget.get())        

        # define function to capture all data, create dict and pass to other class
        # for processing when submit button is clicked
        def submitData():
            
            # value for both scenarios
            totalQuant_int=int(onsiteQuantEntryRec.get())+int(recvdQuantEntryRec.get())
            
            # logical to check if entry update or new entry is submit
            if(comboBoxChem_selection.get()=="Not listed"):
            
                # gather all entries
                casNumArr=[cas1NumEntry.get(),
                            cas2NumEntry.get(),
                            cas3NumEntry.get(),
                            cas4NumEntry.get(),
                            cas5NumEntry.get()]
                casPercArr=[cas1PercEntry.get(),
                            cas2PercEntry.get(),
                            cas3PercEntry.get(),
                            cas4PercEntry.get(),
                            cas5PercEntry.get()]
                df_chemName=[chemNameEntryRec.get()]*len(casNumArr)
                df_onsiteQuantUnits=[comboBoxUnitsRec_selection.get()]*len(casNumArr)
                df_onsiteQuant=[totalQuant_int]*len(casNumArr)
                df_onsiteQuant_date=["NA"]*len(casNumArr)
                df_maxOnsiteQuant=[totalQuant_int]*len(casNumArr)
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
                      "Onsite qty: "+str(onsiteQuantEntryRec.get())+"\n"+
                      "Recvd qty: "+str(recvdQuantEntryRec.get())+"\n\n"+
                      "CAS #1: "+df_dict["chemConstCas"][0]+"; Max CAS %: "+str(df_dict["casPercent"][0])+"\n"+
                      "CAS #2: "+df_dict["chemConstCas"][1]+"; Max CAS %: "+str(df_dict["casPercent"][1])+"\n"+
                      "CAS #3: "+df_dict["chemConstCas"][2]+"; Max CAS %: "+str(df_dict["casPercent"][2])+"\n"+
                      "CAS #4: "+df_dict["chemConstCas"][3]+"; Max CAS %: "+str(df_dict["casPercent"][3])+"\n"+
                      "CAS #5: "+df_dict["chemConstCas"][4]+"; Max CAS %: "+str(df_dict["casPercent"][4]))
                confResp=mb.askyesno("Confirm entry",popuptextNL)
                if confResp==True:
                
                    # send dict to other class
                    EpcraProc.addNewEntry(df_dict,epcradat)
                    mb.showinfo("Confirm entry","Entry has been saved.")

                else:
                    mb.showinfo("Confirm entry","Please revise entry and resubmit.")
    
            else:
                
                # set up dict
                df_dict={'chemName':comboBoxChem_selection.get(),
                        'onsiteQuantUnits':epcradat.onsiteQuantUnits[epcradat.chemName==comboBoxChem_selection.get()].iloc[0],
                        'onsiteQuant':totalQuant_int}
                
                # code for confirmatory popup box
                popuptextLS=("Please confirm the information that you entered\n\n"+
                      "Chemical name: "+df_dict["chemName"]+"\n"+
                      "Units: "+df_dict["onsiteQuantUnits"]+"\n"+
                      "Onsite qty: "+str(onsiteQuantEntryRec.get())+"\n"+
                      "Recvd qty: "+str(recvdQuantEntryRec.get())+"\n\n")
                confResp=mb.askyesno("Confirm entry",popuptextLS)
                if confResp==True:

                    # send dict to other class
                    EpcraProc.updateData(df_dict,epcradat)
                    mb.showinfo("Confirm entry","Entry has been saved.")

                else:
                    mb.showinfo("Confirm entry","Please revise entry and resubmit.")

            return None

        # declare self.root parameters
        self.root = root
        self.root.title(title)
        self.root.geometry('{}x{}'.format(width, height))

        # create frame rows
        top_frame = tk.LabelFrame(self.root, text="Enter information for newly received chemicals", width=width, height=20, pady=3)
        center_frame = tk.Frame(self.root, width=width, height=(height-70), padx=3, pady=3)
        btm_frame = tk.Frame(self.root, width=width, height=50, padx=8, pady=8)

        # declare layout for frame rows
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        top_frame.grid(row=0, sticky="ew")
        center_frame.grid(row=1, sticky="nsew")
        btm_frame.grid(row=2, sticky="se")

        # layout center_frame
        center_frame.grid_rowconfigure(1, weight=1)
        center_frame.grid_columnconfigure(2, weight=1)

        # add 2 frames in center
        center_frame_left = tk.Frame(center_frame, width=350, height=(height-70), padx=3, pady=3)
        center_frame_right = tk.Frame(center_frame, width=(width-350), height=(height-70), padx=3, pady=3)
        center_frame_left.grid(row=1,column=1,sticky="nw")
        center_frame_right.grid(row=1,column=2,sticky="nw")

        # layout center_frame_left
        center_frame_left.grid_rowconfigure(12, weight=1)
        center_frame_left.grid_columnconfigure(1, weight=1)

        # layout center_frame_right
        center_frame_right.grid_rowconfigure(20, weight=1)
        center_frame_right.grid_columnconfigure(2, weight=1)

        # layout btm_frame
        btm_frame.grid_rowconfigure(1, weight=1)
        btm_frame.grid_columnconfigure(2, weight=1)

        # declare widgets for center frame
        #
        # label widgets
        label1 = tk.Label(center_frame_left, text="Chemical name: ")

        label5 = tk.Label(center_frame_right, text="Enter the chemical name below exactly as it appears in the SDS: ")
        label5b = tk.Label(center_frame_right, text="SOME CHEMICAL NAME")
        label6 = tk.Label(center_frame_right, text="Units: ")
        label6b = tk.Label(center_frame_right, text="SOME UNITS")
        label7 = tk.Label(center_frame_right, text="Onsite quantity before receiving: ")
        label8 = tk.Label(center_frame_right, text="Quantity received: ")

        spacer4=tk.Label(center_frame_right,text="")
        spacer5=tk.Label(center_frame_right,text="")
        spacer6=tk.Label(center_frame_right,text="")
        spacer7=tk.Label(center_frame_right,text="")

        label9 = tk.Label(center_frame_right, text="Enter all CAS numbers listed exactly as they are in the Chemical Composition section of the SDS.")
        spacer8=tk.Label(center_frame_right,text="")

        label10 = tk.Label(center_frame_right, text="CAS number:")
        label11 = tk.Label(center_frame_right, text="Max of the % range for CAS:")

        cas1NumEntry_label=tk.Label(center_frame_right, text=" ")
        cas1PercEntry_label=tk.Label(center_frame_right, text=" ")

        cas2NumEntry_label=tk.Label(center_frame_right, text=" ")
        cas2PercEntry_label=tk.Label(center_frame_right, text=" ")

        cas3NumEntry_label=tk.Label(center_frame_right, text=" ")
        cas3PercEntry_label=tk.Label(center_frame_right, text=" ")

        cas4NumEntry_label=tk.Label(center_frame_right, text=" ")
        cas4PercEntry_label=tk.Label(center_frame_right, text=" ")

        cas5NumEntry_label=tk.Label(center_frame_right, text=" ")
        cas5PercEntry_label=tk.Label(center_frame_right, text=" ")

        # entry widgets
        chemNameEntryRec=tk.Entry(center_frame_right,width=65)
        onsiteQuantEntryRec=tk.Entry(center_frame_right, validate="key", validatecommand=(root.register(validate_int), "%P"))
        recvdQuantEntryRec=tk.Entry(center_frame_right, validate="key", validatecommand=(root.register(validate_int), "%P"))

        cas1NumEntry=tk.Entry(center_frame_right)
        cas1PercEntry=tk.Entry(center_frame_right, validate="key", validatecommand=(root.register(validate_float), "%P"))

        cas2NumEntry=tk.Entry(center_frame_right)
        cas2PercEntry=tk.Entry(center_frame_right, validate="key", validatecommand=(root.register(validate_float), "%P"))

        cas3NumEntry=tk.Entry(center_frame_right)
        cas3PercEntry=tk.Entry(center_frame_right, validate="key", validatecommand=(root.register(validate_float), "%P"))

        cas4NumEntry=tk.Entry(center_frame_right)
        cas4PercEntry=tk.Entry(center_frame_right, validate="key", validatecommand=(root.register(validate_float), "%P"))

        cas5NumEntry=tk.Entry(center_frame_right)
        cas5PercEntry=tk.Entry(center_frame_right, validate="key", validatecommand=(root.register(validate_float), "%P"))

        # combobox widgets
        comboBoxChem_values=list(epcradat.chemName.unique())
        comboBoxChem_values.append("Not listed")
        comboBoxChem_selection=tk.StringVar(self.root)
        comboBoxChem=ttk.Combobox(center_frame_left, textvariable=comboBoxChem_selection, values=comboBoxChem_values)
        comboBoxChem.name="cb1"
        comboBoxChem.bind("<<ComboboxSelected>>", on_select)

        comboBoxUnitsRec_selection=tk.StringVar(self.root)
        comboBoxUnitsRec=ttk.Combobox(center_frame_right, values=["Lbs","Gal","55gal Drums","Tons","Other"],textvariable=comboBoxUnitsRec_selection)
        comboBoxUnitsRec.name="cb3"
        comboBoxUnitsRec.bind("<<ComboboxSelected>>", on_select)

        # grid first widgets (rest to be grid in on_select function)
        label1.grid(row=0, sticky="nw")
        comboBoxChem.grid(row=1, sticky="nw")
        
        # declare buttons for btm_frame
        submit_btn=tk.Button(btm_frame, text="Submit", width=10, command=submitData)
        next_btn=tk.Button(btm_frame, text="Next Entry", width=10)
        
        # grid buttons
        submit_btn.grid(row=0, column=0, sticky="e")
        next_btn.grid(row=0, column=1, sticky="e")
        
        # run loop
        self.root.mainloop()

    pass

# declare class for saving data into epcra dataframe
class EpcraProc:   

    # define essential function
    def __init__(self):
        return None

    # define function to process new data
    def addNewEntry(df_dict,epcradat):

        # initialize route path
        dataDir=Path("""C:/Users/kelna/Documents/pythonTest/datafiles/!PERM""")

        # load base epcra inventory file
        fileToOpen1=dataDir/"stackEpcraDatabases_2024-06-21.csv"
        epcra_refdb=pandas.read_csv(fileToOpen1,sep=",",index_col=False) 

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
        dataDir2=Path("""C:/Users/kelna/Documents/pythonTest/datafiles/updatefiles""")
        fileToSave=dataDir2/filename
        epcradat_copy.to_csv(fileToSave,sep=',',index=False)
        
        return None

    # define function to updata database
    def updateData(df_dict,epcradat):
        
        # initialize route path
        dataDir=Path("""C:/Users/kelna/Documents/pythonTest/datafiles/!PERM""")

        # load base epcra inventory file
        fileToOpen1=dataDir/"stackEpcraDatabases_2024-06-21.csv"
        epcra_refdb=pandas.read_csv(fileToOpen1,sep=",",index_col=False)
        
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
        dataDir2=Path("""C:/Users/kelna/Documents/pythonTest/datafiles/updatefiles""")
        fileToSave=dataDir2/filename
        epcradat_copy2.to_csv(fileToSave,sep=',',index=False)

        return None
    
    pass

main()
