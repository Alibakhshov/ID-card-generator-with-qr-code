from tkinter import *
from PIL import Image as I 
from PIL import ImageTk as IT
from PIL import ImageDraw as ID
from PIL import ImageFont as IF
import qrcode as Q


 
# creating a main window
class main_window:
    def __init__(self, root):
        self.root = root
        self.root.title("ID card generator") 
        self.root.geometry("1000x800")
        self.root.resizable()
        
        # creating a label to write a title
        self.title = Label(self.root, 
                           text = "ID card generator", 
                           font = ('cooper', 20, 'bold'),
                           pady = 20,
                           bg   = '#000000',
                           fg   = '#ffffff'
        )
        
        # creating a logo in our label
        self.logo = Frame(self.title, 
                          relief = SUNKEN,
                          bd = 1,
                          bg = 'red'                  
         )
        
        # creating a label(text) inside our logo
        self.logo_text = Label(self.logo,
                               text = 'Logo\nNew',
                               font = ('cooper', 20, 'bold')     
        )
        
        
        
        # placing the labels
        self.title.place(x=0, y=0, relwidth=1)
        self.logo.place(x=3, y=2, width=70, height=70)
        self.logo_text.place(x=0, y=0, relheight=1, relwidth=1)
        
    
    
root = Tk()
App = main_window(root)

root.mainloop()







    
