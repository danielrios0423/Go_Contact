from ctypes.wintypes import INT
import os
import unittest
import pathlib
from queue import Queue
from threading import Thread
from tkinter.filedialog import askdirectory, askopenfilename
from sqlalchemy import tuple_
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap import utility

from pyunitreport import HTMLTestRunner
from Go_Contact_test.test_go import GoContactTest
from Template_edit.templates import RW_template_db
from Template_edit.new_templates import NewJason
from delete import delete

class FileSearchEngine(ttk.Frame):

    queue = Queue()
    searching = False

    def __init__(self, master):
        delete()
        super().__init__(master, padding=15)
        self.pack(fill=BOTH, expand=YES)

        # application variables
        _path = pathlib.Path().absolute().as_posix()
        self.path_file = ttk.StringVar(value= "")
        self.path_directory = ttk.StringVar(value= "")
        self.campaign_entry = ttk.StringVar(value='Test')
        self.template_entry = ttk.StringVar(value='ejemplo_test')
        
        self.type_var = ttk.StringVar(value='manual')
        self.term_var = ttk.StringVar(value='md')        
        self.list_table = []
        
        self.error_display = ttk.StringVar(value= "")
        
        # header and labelframe option container
        option_text = "Complete el formulario para comenzar el proceso"
        self.option_lf = ttk.Labelframe(self, text=option_text, padding=15)
        self.option_lf.pack(fill=X, expand=YES, anchor=N)   
        
        self.create_type_row()        
        self.campaign_select()
        self.template_select()      
        self.create_path_file()
        self.execute_button()
        self.execute_button_1()
        self.insert_button()  
        self.create_results_view()  
        self.disabled()           
        
        self.progressbar = ttk.Progressbar(
            master=self, 
            mode=INDETERMINATE, 
            bootstyle=(STRIPED, SUCCESS)
        )
        self.progressbar.pack(fill=X, expand=YES)
        
    def disabled(self):
        self.execute_button_type.pack_forget()
        self.path_row_file.pack(fill=X, expand=YES, pady= 15)
        if self.type_var.get() == "manual":
            self.execute_button_type.pack(fill=X, expand=YES, pady = 15)
            self.resultview.pack_forget() 
            self.execute_button_type_1.pack_forget()   
        elif self.type_var.get() == "automático":  
            self.execute_button_type_1.pack(fill=X, expand=YES, pady = 15)
            self.resultview.pack(fill=BOTH, expand=YES, pady=10)
            self.execute_button_type.pack_forget()      
            
                
    def create_path_file(self):
        """Add path row to labelframe"""
        self.path_row_file = ttk.Frame(self.option_lf)    #Crea Frame del buscador (URL)
        #self.path_row_file.pack(fill=X, expand=YES, pady= 15)        
        path_lbl = ttk.Label(self.path_row_file, text="Documento CSV", width= 15)  #Crea y configura label (Documento CSV)
        path_lbl.pack(side=LEFT, padx=(15, 0))
        self.path_ent = ttk.Entry(self.path_row_file, textvariable=self.path_file, width= 50, state="disabled",) #Crea entrada para URL
        self.path_ent.pack(side=LEFT, fill=X, expand=YES, padx=5)
        self.browse_btn_file = ttk.Button(        #Crea Button de Browse
            bootstyle="info",
            master=self.path_row_file, 
            text="Explorar", 
            command=self.on_browse_file, 
            width=8
        )
        self.browse_btn_file.pack(side=LEFT, padx=5)
     
    def on_browse_file(self):
        """Callback for directory browse"""
        path = askopenfilename(title="Select File", filetypes=(("csv files", "*.csv"),("all files", "*.*")))
        if path:
            self.path_file.set(path)

    def campaign_select(self):
        path_row = ttk.Frame(self.option_lf)    #Crea Frame del buscador (URL)
        path_row.pack(fill=X, expand=YES, pady = 15)        
        path_lbl = ttk.Label(path_row, text="Campaña", width= 15)
        path_lbl.pack(side=LEFT, padx=(15, 0))
        path_ent = ttk.Combobox(path_row, textvariable=self.campaign_entry, width= 50,bootstyle="info", state="readonly") #Crea entrada para URL
        path_ent.pack(side=LEFT, fill=X, expand=YES, padx=5)
        path_ent["values"] = ["Test","Test_1", "Prueba", "Prueba_1"]
        
    def template_select(self):
        path_row = ttk.Frame(self.option_lf)    #Crea Frame del buscador (URL)
        path_row.pack(fill=X, expand=YES)        
        path_lbl = ttk.Label(path_row, text="Plantilla", width= 15)
        path_lbl.pack(side=LEFT, padx=(15, 0))
        path_ent = ttk.Combobox(path_row, textvariable= self.template_entry, width= 50,bootstyle="info", state="readonly") #Crea entrada para URL
        path_ent.pack(side=LEFT, fill=X, expand=YES, padx=5)
        path_ent["values"] = ["ejemplo_test", "Test_1", "Prueba", "Prueba_1"]
        
    def create_type_row(self):
        """Add type row to labelframe"""
        type_row = ttk.Frame(self.option_lf)
        type_row.pack(fill=X, expand=YES, pady = 15)
        type_lbl = ttk.Label(type_row, text="Type", width=8)
        type_lbl.pack(side=LEFT, padx=(15, 0))

        contains_opt = ttk.Radiobutton(
            master=type_row, 
            text="Manual", 
            variable=self.type_var,
            command = self.disabled, 
            value="manual"
        )
        contains_opt.pack(side=LEFT, padx = 15)
        contains_opt.invoke()

        endswith_opt = ttk.Radiobutton(
            master=type_row, 
            text="Automático", 
            variable=self.type_var, 
            value="automático",
            command = self.disabled,
        )
        endswith_opt.pack(side=LEFT)

    def execute_button(self):
        self.execute_button_type = ttk.Frame(self.option_lf)
        path_lbl = ttk.Label(self.execute_button_type, textvariable=self.error_display, width= 70)  #Crea y configura label (Documento CSV)
        path_lbl.pack(side=LEFT, padx=(40, 5))        
        browse_btn = ttk.Button(        #Crea Button
            bootstyle='info',
            master=self.execute_button_type, 
            text="Aceptar", 
            command=self.run, 
            width=8
        )
        browse_btn.pack(side=RIGHT, padx=4)
        
    def insert_button(self):
        path_lbl = ttk.Label(self.execute_button_type_1, textvariable=self.error_display, width= 70)  #Crea y configura label (Documento CSV)
        path_lbl.pack(side=LEFT, padx=(40, 5))
        browse_btn = ttk.Button(        #Crea Button
            bootstyle="info",
            master=self.execute_button_type_1, 
            text="Insertar", 
            command=self.new_template, 
            width=8
        )
        browse_btn.pack(side=RIGHT, padx=4)
        
    def execute_button_1(self):
        self.execute_button_type_1 = ttk.Frame(self.option_lf)
        browse_btn = ttk.Button(        #Crea Button
            bootstyle="info",
            master=self.execute_button_type_1, 
            text="Iniciar", 
            command=self.run_1, 
            width=8
        )
        browse_btn.pack(side=RIGHT, padx=4)
        
    def new_template(self):
        
        if self.verification() == True:
            data =  [self.campaign_entry.get() ,self.template_entry.get(), self.path_file.get()]
            if data[2] in self.list_table:
                self.error_display.set("BASE DE DATOS REPETIDA")
            else:
                self.list_table.append(self.path_file.get())
                nj = NewJason()
                nj.new_template(data) 
                self.insert_row(data)
            
    def verification(self):
        if self.path_file.get() == '':
            self.error_display.set("FALTA URL DEL DOCUMENTO")
            return False        
        else:
            return True
    
    def edit_template(self):
        data =  [self.campaign_entry.get() ,self.template_entry.get(), self.path_file.get()]
        data_template = RW_template_db()
        data_template.change(data)  
         
    def run(self):  
        if self.verification() == True: 
            self.edit_template()     
            try:
                unittest.main(verbosity= 2)
            except:
                self.error_display.set("TEST NO SE SABE")
        else: self.error_display.set("FALTA URL DEL DOCUMENTO")
        
    def run_1(self):
        self.error_display.set("RUN AUTOMÁTICO")
        
    def create_results_view(self):
        """Add result treeview to labelframe"""
        self.resultview = ttk.Treeview(
            master=self, 
            bootstyle=INFO, 
            columns=[0, 1, 2, 3],
            show=HEADINGS
        )
        #self.resultview.pack(fill=BOTH, expand=YES, pady=10)

        # setup columns and use `scale_size` to adjust for resolution
        self.resultview.heading(0, text='Nombre', anchor=W)
        self.resultview.heading(1, text='Campaña', anchor=W)
        self.resultview.heading(2, text='Plantilla', anchor=W)
        self.resultview.heading(3, text='Documento CSV', anchor=W)
        self.resultview.column(
            column=0, 
            anchor=W, 
            width=utility.scale_size(self, 150), 
            stretch=False
        )
        self.resultview.column(
            column=1, 
            anchor=W, 
            width=utility.scale_size(self, 120), 
            stretch=False
        )
        self.resultview.column(
            column=2, 
            anchor=W, 
            width=utility.scale_size(self, 120), 
            stretch=False
        )
        self.resultview.column(
            column=3, 
            anchor=W, 
            width=utility.scale_size(self, 300), 
            stretch=False
        ) 
        
    def insert_row(self, data):
        data_name = (os.path.basename(data[2]))[:-4]
        print("dataaa",data)
        iid = self.resultview.insert(
                parent='', 
                index=END,                 
                values=(data_name, data[0], data[1], data[2])
            )
        self.resultview.selection_set(iid)
        
        
            
if __name__ == '__main__':

    app = ttk.Window("Go Contact DB", "journal")
    FileSearchEngine(app)
    app.mainloop()
