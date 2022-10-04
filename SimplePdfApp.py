import tkinter as tk
import PyPDF2
from tkinter import filedialog

LARGE_FONT = ('Verdana', 22)
Middle_FONT = ('Verdana', 12)


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('EasyPdf')
        self.geometry('800x600')
        self.resizable(False,False)
 
        # this container contains all the pages
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)   # make the cell in grid cover the entire window
        container.grid_columnconfigure(0,weight=1) # make the cell in grid cover the entire window
        self.frames = {} # these are pages we want to navigate to
 
        for F in (StartPage, CombinePage, DeletePage, RotatePage,WaterMarkPage): # for each page
            frame = F(container, self) # create the page
            self.frames[F] = frame  # store into frames
            frame.grid(row=0,column=0,sticky='nesw') 
 
        self.show_frame(StartPage) # let the first page is StartPage
 

    def show_frame(self,name):
        frame = self.frames[name]
        frame.tkraise()

    
        

#    def switch_frame(self, fromPage, toPage):
#        frame = self.frames[fromPage]
#        frame.grid_forget()
#        frame = self.frames[toPage]
#        frame.tkraise()
 
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        layout = tk.Frame(self)
        
        label = tk.Label(layout, text='Main Menu', font=LARGE_FONT)
        label.grid(row=0,column=0,columnspan=2,pady=10, padx=10)
        
 
        button1 = tk.Button(layout, width=30, height=10,
                            text='Combine PDFs',bg='white',fg='black',
                            command=lambda : controller.show_frame(CombinePage))
        button1.grid(row=1, column=0,pady=10, padx=10)
        button1.bind("<Enter>",lambda e: button1.configure(bg='grey',fg='white'))
        button1.bind("<Leave>",lambda e: button1.configure(bg='white',fg='black'))

        button2 = tk.Button(layout, width=30, height=10,
                             text ='Delete Pages',bg='white',fg='black',
                            command=lambda : controller.show_frame(DeletePage))
        button2.grid(row=1, column=1,pady=10, padx=10)
        button2.bind("<Enter>",lambda e: button2.configure(bg='grey',fg='white'))
        button2.bind("<Leave>",lambda e: button2.configure(bg='white',fg='black'))

        button3 = tk.Button(layout, width=30,height=10,
                             text='Rotate Pages',bg='white',fg='black',
                            command=lambda : controller.show_frame(RotatePage))
        button3.grid(row=2, column=0,pady=10, padx=10)
        button3.bind("<Enter>",lambda e: button3.configure(bg='grey',fg='white'))
        button3.bind("<Leave>",lambda e: button3.configure(bg='white',fg='black'))

        button4 = tk.Button(layout, width=30,height=10,
                             text ='Add WaterMark',bg='white',fg='black',
                            command=lambda : controller.show_frame(WaterMarkPage))
        button4.grid(row=2, column=1,pady=10, padx=10)
        button4.bind("<Enter>",lambda e: button4.configure(bg='grey',fg='white'))
        button4.bind("<Leave>",lambda e: button4.configure(bg='white',fg='black'))

        layout.pack(pady=10, padx=10)

         


        
 
class CombinePage(tk.Frame):
    pdfReaders = []
    
    def loadPDF(self):
        filename = tk.filedialog.askopenfilename(parent=self, filetypes=[('PDF Files','*.pdf')])
        if filename!='':
           f = open(filename, 'rb')
           if f is not None:
               pdfReader = PyPDF2.PdfFileReader(f)
               self.pdfReaders.append(pdfReader)
               label1 = tk.Label(self, text=filename+' has been loaded!')
               label1.pack()
        
    def combine(self):
        pdfWriter = PyPDF2.PdfFileWriter()
        for reader in self.pdfReaders:
            for pageNum in range(reader.numPages):
                pageObj = reader.getPage(pageNum)
                pdfWriter.addPage(pageObj)

        filename = tk.filedialog.asksaveasfilename(parent=self, defaultextension=".pdf", filetypes=[('PDF Files','*.pdf')])
        if filename!='':
            f = open(filename, 'wb')
            if f is not None:
                pdfWriter.write(f)
                f.close()
            
        label = tk.Label(self, text='Files have been combined!')
        label.pack()

        
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Combine PDFs', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button2 = tk.Button(self, text='Load PDF', 
                            command=lambda : self.loadPDF())
        button2.pack()
        button3 = tk.Button(self, text ='Combine',
                            command=lambda : self.combine())
        button3.pack()
 
        button1 = tk.Button(self, text='Back to Home', # likewise StartPage
                            command=lambda : controller.show_frame(StartPage))
        button1.pack()

class DeletePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Delete Pages', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
 
        button1 = tk.Button(self, text='Back to Home', # likewise StartPage
                            command=lambda : controller.show_frame(StartPage))
        button1.pack()

class RotatePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Rotate Pages', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
 
        button1 = tk.Button(self, text='Back to Home', # likewise StartPage
                            command=lambda : controller.show_frame(StartPage))
        button1.pack()

class WaterMarkPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Add WaterMark', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
 
        button1 = tk.Button(self, text='Back to Home', # likewise StartPage
                            command=lambda : controller.show_frame(StartPage))
        button1.pack()
 
if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
