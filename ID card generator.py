from tkinter import *
from turtle import bgcolor, fillcolor
from PIL import Image as I
from tkinter import ttk 
from PIL import ImageTk as IT
from PIL import ImageDraw as ID
from PIL import ImageFont as IF
import qrcode as Q
from resizeimage  import resizeimage as re
from tkinter import ttk


 
# creating a main window
class main_window:
    def __init__(self, root):
        self.root = root
        self.root.title("ID card generator") 
        self.root.geometry("1360x800")
        self.root.resizable()
        
        # Creating a label to write a title
        self.title = Label(self.root, 
                           text = "ID card generator", 
                           font = ('cooper', 20, 'bold'),
                           pady = 20,
                           bg   = '#000000',
                           fg   = '#ffffff')
        
        # Creating a logo in our label
        self.logo = Frame(self.title, 
                          relief = SUNKEN,
                          bd = 1,
                          bg = 'white')
        
        self.logo_img = I.open('user logo.png')
        self.res_img = self.logo_img.resize((70,70))
        self.Tk_Image = IT.PhotoImage(self.res_img)
        
        
        # Putting our logo image into the label
        self.logo_text = Label(self.logo,
                               image = self.Tk_Image                        
        )
        
        # Creating the first frame 
        self.frame1 = Frame(self.root, 
                          relief = SUNKEN,
                          bd = 1,
                          bg = 'white'                  
         )
        
        # Creating the second frame
        self.frame2 = Frame(self.root, 
                          relief = SUNKEN,
                          bd = 1,
                          bg = 'white'                  
         )
        
        # Creating a title for the first frame (frame1)
        self.frame1_tit = Label(self.frame1,
                                bg = '#000000',
                                fg = '#ffffff',
                                text = 'Details',
                                font = ('cooper', 20, 'bold'),
                                pady = 5                        
        )
        
        # Creating a title for the second frame (frame2)
        self.frame2_tit = Label(self.frame2,
                                bg = '#000000',
                                fg = '#ffffff',
                                text = 'ID Card',
                                font = ('cooper', 20, 'bold'),
                                pady = 5                        
        )
        
         # Creating a label for first name
        self.full_name = Label(self.frame1,
                                text = 'Full name',
                                bg = 'white',
                                font = ('cooper', 13, 'bold'),                   
        )
        
        # Creating a label for gender
        self.gender = Label(self.frame1,
                                text = 'Gender',
                                bg = 'white',
                                font = ('cooper', 13, 'bold'),                      
        )
        
        # Creating a label for age
        self.age = Label(self.frame1,
                                text = 'Age',
                                bg = 'white',
                                font = ('cooper', 13, 'bold'),                       
        )
        
        # Creating a label for blood group
        self.blood_group = Label(self.frame1,
                                text = 'Blood group',
                                bg = 'white',
                                font = ('cooper', 13, 'bold'),                      
        )
        
        # Creating a label for mobile
        self.phone = Label(self.frame1,
                                text = 'Mobile',
                                bg = 'white',
                                font = ('cooper', 13, 'bold'),                      
        )
        
        # Creating a label for email
        self.email = Label(self.frame1,
                                text = 'Email',
                                bg = 'white',
                                font = ('cooper', 13, 'bold'),                       
        )
        
        
        self.Name = StringVar()
        self.Gender = StringVar()
        self.Age = StringVar()
        self.bloodGroup = StringVar()
        self.Phone = StringVar()
        self.Email = StringVar()
        
        # creating an entry for the "Full name" label
        self.fullname_entry = Entry(self.frame1,
                                    textvariable=self.Name,
                                    font = 10, 
                                    width = 30,
                                    bg = "white", 
                                    fg = "black",)
        
         # creating an entry for the "gender" label
        self.gender_entry = ttk.Combobox(self.frame1,
                                    textvariable=self.Gender,     
                                    font = 5, 
                                    width = 28,
                                    state='readonly',
                                    foreground = "black",
                                    background = "white"  
        )                                  
      

        self.gender_entry['values'] = ('Select Gender', 'Male', 'Female', 'Others')
        self.gender_entry.current(0)
        
        # creating an entry for the "age" label
        self.age_entry = Entry(self.frame1,
                                    textvariable=self.Age,
                                    font = 5, 
                                    width = 30,
                                    bg = "white", 
                                    fg = "black"                           
                                    )
        
        # creating an entry for the "blood group" label
        self.blood_entry = Entry(self.frame1,
                                    textvariable=self.bloodGroup,
                                    font = 5, 
                                    width = 30,
                                    bg = "white", 
                                    fg = "black"                           
                                    )
        
        # creating an entry for the "phone" label
        self.phone_entry = Entry(self.frame1,
                                    textvariable=self.Phone,
                                    font = 5, 
                                    width = 30,
                                    bg = "white", 
                                    fg = "black"                           
                                    )
        
        # creating an entry for the "email" label
        self.email_entry = Entry(self.frame1,
                                    textvariable=self.Email,
                                    font = 5, 
                                    width = 30,
                                    bg = "white", 
                                    fg = "black"                           
                                    )
        
        # creating a button to generate an id card
        self.gen_button = Button(self.frame1,
                                 text = 'Generate',
                                 font = ('cooper', 15, 'bold'),
                                 command= self.Generate
                                 )
        
        # creating a button to clear the data
        self.clear_button = Button(self.frame1,
                                 command= self.Clear,
                                 text = 'Clear',
                                 font = ('cooper', 15, 'bold')
                                 )
        
        # printing a message on the frame1
        self.msg = ''
        self.msg_frame1 = Frame(self.frame1, 
                                bg = 'white',
                                relief=SUNKEN,
                                bd=1,)
        
        # creating a label for the frame1 message
        self.msg_label = Label(self.msg_frame1, 
                              text = self.msg,
                              font = ('cooper', 15, 'bold'),
                              fg = 'red',
                              bg = 'white',
                              )
        # creating a frame for the ID card(frame2) area
        self.ID_Frame = Frame(self.frame2,
                              relief=SUNKEN,
                              bd=1,
                              bg = 'white')
        # creating a label for frame2
        self.F2_txt = Label(self.ID_Frame,
                              text="ID\nCard\nNot Found",
                              relief=SUNKEN,
                              font = ('cooper', 20, 'bold'),
                              bd=1)
        
        
        # placing the variables
        self.title.place(x=0, y=0, relwidth=1)
        self.logo.place(x=3, y=2, width=70, height=70)
        self.logo_text.place(x=0, y=0, relheight=1, relwidth=1)
        self.frame1.place(x=10, y=100, width=665, height=650)
        self.frame2.place(x=685, y=100, width=665, height=650)
        self.frame1_tit.place(x=0, y=0, relwidth=1)
        self.frame2_tit.place(x=0, y=0, relwidth=1)
        self.full_name.place(x=10, y=80)
        self.gender.place(x=10, y=140)
        self.age.place(x=10, y=200)
        self.blood_group.place(x=10, y=260)
        self.phone.place(x=10, y=320)
        self.email.place(x=10, y=380)
        self.fullname_entry.place(x=180, y=80)
        self.gender_entry.place(x=180, y=140)
        self.age_entry.place(x=180, y=200)
        self.blood_entry.place(x=180, y=260)
        self.phone_entry.place(x=180, y=320)
        self.email_entry.place(x=180, y=380)
        self.gen_button.place(x=10, y=430, width=200)
        self.clear_button.place(x=350, y=430, width=200)
        self.msg_frame1.place(x=10,y=490, width=625, height=150)
        self.msg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.ID_Frame.place(x=10, y=100, width=645, height=400)
        self.F2_txt.place(x=0, y=0, relwidth=1, relheight=1)
        
        
        
    def Generate(self):
        global msg
        if self.Name.get() == '' or self.Gender.get() == '' or self.Age.get() == '' or self.bloodGroup.get() == '' or self.Phone.get() == '' or self.Email.get() == '':
            self.msg = 'Please fill in all required entry fields'
            self.msg_label.config(text=self.msg, fg = 'red', font = ('cooper', 20, 'bold'),   )
            
        elif self.gender_entry.current() == 0:
            self.msg = 'Please select gender'
            self.msg_label.config(text=self.msg, fg = 'red', font = ('cooper', 30, 'bold'),   )
            
        else:
        
        
          fon = IF.truetype('ArialCE.ttf', size=30)
          self.img = I.new('RGB', (1000, 600), (255, 255, 255))
          self.Drw = ID.Draw(self.img)
          self.Drw.text((20, 100), 'Full Name:', fill='#000000', font=fon)
          self.Drw.text((20, 150), 'Gender:', fill='#000000', font=fon)
          self.Drw.text((20, 200), 'Age:', fill='#000000', font=fon)
          self.Drw.text((20, 250), 'Blood-group:', fill='#000000', font=fon)
          self.Drw.text((20, 300), 'Phone:', fill='#000000', font=fon)
          self.Drw.text((20, 350), 'Email:', fill='#000000', font=fon)
          
          self.Drw.text((250, 100), self.Name.get() , fill='#000000', font=fon)
          self.Drw.text((250, 150), self.Gender.get(), fill='#000000', font=fon)
          self.Drw.text((250, 200), self.Age.get(), fill='#000000', font=fon)
          self.Drw.text((250, 250), self.bloodGroup.get(), fill='#000000', font=fon)
          self.Drw.text((250, 300), self.Phone.get(), fill='#000000', font=fon)
          self.Drw.text((250, 350), self.Email.get(), fill='#000000', font=fon)
          
          self.Qrcode = Q.QRCode(version=1, box_size=10, border=1)
          self.Qrcode.add_data(f'Full Name: {self.Name.get()}\nGender: {self.Gender.get()} \nAge: {self.Age.get()} \nBlood Group: {self.bloodGroup.get()} \nPhone: {self.Phone.get()} \nEmail: {self.Email.get()} ')
          self.Qrcode.make(fit=True)
          self.Qr = self.Qrcode.make_image(fill_color='#000000', back_color='#ffffff')
          self.Qr.save('QR Code/Qr Code of ' + str(self.Name.get())+'.png')
          self.Qr_res = re.resize_cover(self.Qr,[300, 300])
          self.img.paste(self.Qr_res, (680, 100))
          self.img.save('ID Card/ID Card of ' + str(self.Name.get())+'.png')
          self.res_F2 = self.img.resize((640, 400))
          self.img_F2 = IT.PhotoImage(self.res_F2)
          self.F2_txt.config(image=self.img_F2)
          self.Qrcode.clear()
          
          self.msg = 'Done'
          self.msg_label.config(text=self.msg, fg = 'green', font = ('cooper', 30, 'bold'),)
    
    def Clear(self):
        
        self.Name.set('')
        self.Gender.set('') 
        self.Age.set('')
        self.bloodGroup.set('')
        self.Phone.set('')
        self.Email.set('')
        self.msg_label.config(text='')
        self.F2_txt.config(image='')
        self.gender_entry.current(0) 
        
    
root = Tk()
App = main_window(root)
root.mainloop()







    
