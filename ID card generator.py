from tkinter import *
from PIL import Image as I 
from PIL import ImageTk as IT
from PIL import ImageDraw as ID
from PIL import ImageFont as IF
import pyqrcode as Q


 
# creating a main window
class main_window:
    def __init__(self, root):
        self.root = root
        self.root.title("ID card generator") 
        self.root.geometry("1360x800")
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
                          bg = 'white'                  
         )
        self.logo_img = I.open('user logo.png')
        self.res_img = self.logo_img.resize((70,70))
        self.Tk_Image = IT.PhotoImage(self.res_img)
        
        
        # putting our logo image into the label
        self.logo_text = Label(self.logo,
                               image = self.Tk_Image                        
        )
        
        # creating the first frame 
        self.frame1 = Frame(self.root, 
                          relief = SUNKEN,
                          bd = 1,
                          bg = 'white'                  
         )
        
        # creating the second frame
        self.frame2 = Frame(self.root, 
                          relief = SUNKEN,
                          bd = 1,
                          bg = 'white'                  
         )
        
        # creating a title for the first frame (frame1)
        self.frame1_tit = Label(self.frame1,
                                bg = '#000000',
                                fg = '#ffffff',
                                text = 'Details',
                                font = 20,
                                pady = 5                        
        )
        
        # creating a title for the second frame (frame2)
        self.frame2_tit = Label(self.frame2,
                                bg = '#000000',
                                fg = '#ffffff',
                                text = 'ID Card',
                                font = 20,
                                pady = 5                        
        )
        
         # creating a label for first name
        self.first_name = Label(self.frame1,
                                text = 'Full name',
                                bg = 'white',
                                font = 20,                    
        )
        
        # creating a label for gender
        self.gender = Label(self.frame1,
                                text = 'Gender',
                                bg = 'white',
                                font = 20,                    
        )
        
        # creating a label for age
        self.age = Label(self.frame1,
                                text = 'Age',
                                bg = 'white',
                                font = 20,                    
        )
        
        # creating a label for blood group
        self.blood_group = Label(self.frame1,
                                text = 'Blood group',
                                bg = 'white',
                                font = 20,                    
        )
        
        # creating a label for mobile
        self.phone = Label(self.frame1,
                                text = 'Mobile',
                                bg = 'white',
                                font = 20,                    
        )
        
        # creating a label for email
        self.email = Label(self.frame1,
                                text = 'Email',
                                bg = 'white',
                                font = 20,                    
        )
        
        
        
        
        # placing the variables
        self.title.place(x=0, y=0, relwidth=1)
        self.logo.place(x=3, y=2, width=70, height=70)
        self.logo_text.place(x=0, y=0, relheight=1, relwidth=1)
        self.frame1.place(x=10, y=100, width=665, height=550)
        self.frame2.place(x=685, y=100, width=665, height=550)
        self.frame1_tit.place(x=0, y=0, relwidth=1)
        self.frame2_tit.place(x=0, y=0, relwidth=1)
        self.first_name.place(x=10, y=80)
        self.gender.place(x=10, y=140)
        self.age.place(x=10, y=200)
        self.blood_group.place(x=10, y=260)
        self.phone.place(x=10, y=320)
        self.email.place(x=10, y=380)
        
        
    
    
root = Tk()
App = main_window(root)
root.mainloop()







    
