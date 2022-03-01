import unittest
import pathlib
from queue import Queue
from threading import Thread
from tkinter.filedialog import askdirectory, askopenfilename
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap import utility

from pyunitreport import HTMLTestRunner
from go_contact_test.test_go import GoContactTest
from templates import RW_template_db

class FileSearchEngine(ttk.Frame):

    queue = Queue()
    searching = False

    def __init__(self, master):
        super().__init__(master, padding=15)
        self.pack(fill=BOTH, expand=YES)

        # application variables
        _path = pathlib.Path().absolute().as_posix()
        self.path_file = ttk.StringVar(value= "")
        self.path_directory = ttk.StringVar(value= "")
        self.campaign_entry = ttk.StringVar(value='Test')
        self.template_entry = ttk.StringVar(value='ejemplo_test')
        
        self.type_var = ttk.StringVar(value='')
        self.term_var = ttk.StringVar(value='md')
        

        # header and labelframe option container
        option_text = "Complete el formulario para comenzar el proceso"
        self.option_lf = ttk.Labelframe(self, text=option_text, padding=15)
        self.option_lf.pack(fill=X, expand=YES, anchor=N)
        
        self.create_type_row()
        self.campaign_select()
        self.template_select()      
        self.create_path_directory()
        self.create_path_file()
        self.execute_button()

        self.progressbar = ttk.Progressbar(
            master=self, 
            mode=INDETERMINATE, 
            bootstyle=(STRIPED, SUCCESS)
        )
        self.progressbar.pack(fill=X, expand=YES)
        
    def disabled(self):
        self.execute_button_type.pack_forget()
        if self.type_var.get() == "manual":
            self.path_row_file.pack(fill=X, expand=YES, pady= 15)
            self.path_row_directory.pack_forget()            
        elif self.type_var.get() == "automático":
            self.path_row_directory.pack(fill=X, expand=YES, pady= 15)
            self.path_row_file.pack_forget()
        self.execute_button_type.pack(fill=X, expand=YES, pady = 15)
                
    def create_path_file(self):
        """Add path row to labelframe"""
        self.path_row_file = ttk.Frame(self.option_lf)    #Crea Frame del buscador (URL)
        #self.path_row_file.pack(fill=X, expand=YES, pady= 15)        
        path_lbl = ttk.Label(self.path_row_file, text="Documento CSV", width= 15)  #Crea y configura label (Documento CSV)
        path_lbl.pack(side=LEFT, padx=(15, 0))
        self.path_ent = ttk.Entry(self.path_row_file, textvariable=self.path_file, width= 50) #Crea entrada para URL
        self.path_ent.pack(side=LEFT, fill=X, expand=YES, padx=5)
        self.browse_btn_file = ttk.Button(        #Crea Button de Browse
            bootstyle="info",
            master=self.path_row_file, 
            text="Explorar", 
            command=self.on_browse_file, 
            width=8
        )
        self.browse_btn_file.pack(side=LEFT, padx=5)
        
    def create_path_directory(self):
        """Add path row to labelframe"""
        self.path_row_directory = ttk.Frame(self.option_lf)    #Crea Frame del buscador (URL)
        #self.path_row_directory.pack(fill=X, expand=YES, pady= 15)        
        path_lbl = ttk.Label(self.path_row_directory, text="Carpeta CSV", width=15)  #Crea y configura label (Documento CSV)
        path_lbl.pack(side=LEFT, padx=(15, 0))
        path_ent = ttk.Entry(self.path_row_directory, textvariable=self.path_directory, width= 50) #Crea entrada para URL
        path_ent.pack(side=LEFT, fill=X, expand=YES, padx=5)
        self.browse_btn_directory = ttk.Button(        #Crea Button de Browse
            bootstyle="info",
            master=self.path_row_directory, 
            text="Explorar", 
            command=self.on_browse_directory, 
            width=8
        )
        self.browse_btn_directory.pack(side=LEFT, padx=5)
     
    def on_browse_directory(self):
        """Callback for directory browse"""
        path = askdirectory(title="Select directory")
        if path:
            self.path_directory.set(path)
        
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
            value="manual"
        )
        contains_opt.pack(side=LEFT, padx = 15)
        contains_opt.invoke()

        endswith_opt = ttk.Radiobutton(
            master=type_row, 
            text="Automático", 
            variable=self.type_var, 
            value="automático"
        )
        endswith_opt.pack(side=LEFT)
        
        browse_btn = ttk.Button(        #Crea Button de Browse
            bootstyle="default-link",
            master=type_row, 
            text="Aceptar", 
            command=self.disabled, 
            width=8
        )
        browse_btn.pack(side=LEFT, padx=40)

    def execute_button(self):
        self.execute_button_type = ttk.Frame(self.option_lf)
        browse_btn = ttk.Button(        #Crea Button
            bootstyle="info",
            master=self.execute_button_type, 
            text="Aceptar", 
            command=self.run, 
            width=8
        )
        browse_btn.pack(side=BOTTOM, padx=40)
        
    def run(self):
        print("hola")
        data =  [self.campaign_entry.get() ,self.template_entry.get(), self.path_directory.get()]
        data_template = RW_template_db()
        #data_template.change(data)
        
        #GoContactTest(unittest.TestCase)
        try:
            unittest.main(verbosity= 2, testRunner= HTMLTestRunner(output= "report", report_name= "report_Go"))
        except:
            print("OK")

if __name__ == '__main__':

    app = ttk.Window("Go Contact DB", "journal")
    FileSearchEngine(app)
    app.mainloop()
