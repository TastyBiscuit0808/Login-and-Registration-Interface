
from tkinter import *
from PIL import ImageTk,Image  

#mainwindow (1st window)
userdict = {}
choose = Tk()

choose.geometry('1000x1000')

choose.title(' This is the main window ')

#homescreenimage = Image.open( "C:\Users\Aryan Wadhwa\OneDrive\Desktop\TYRFxptW-2013_bus_base.jpg")
#img = PhotoImage(file = "C:\\Users\\Aryan Wadhwa\\OneDrive\\Desktop\\Python Files\\Bus Ticket Management System\\User_credentials")
                    

def login():

    login = Tk()
    login.geometry('1000x1000')
    login.title('Login')    
    
    #username label and text entry box
    emailLabel = Label(login, text="E Mail").grid(row=0, column=0)
    emailLabel = StringVar()
    email_Entry = Entry(login, textvariable=emailLabel)
    email_Entry.grid(row=0, column=1)
    

    #password label and password entry box
    passwordLabel = Label(login,text="Password").grid(row=1, column=0)  
    passwordLabel = StringVar()
    passwordEntry = Entry(login, textvariable=passwordLabel, show='*')
    passwordEntry.grid(row=1, column=1)


    def login_message():


        file = open("User_credentials", 'r')
        string = file.read()
        lst = string.split()
        name = email_Entry.get()
        loginpass = passwordEntry.get()
        if name in lst:
            for i in range(len(lst)):
                if lst[i] == name:
                    password = lst[i+1]
                    break
            if loginpass == str(password):
                sucesful = Label(login, text = "You have successfully logged in").grid(row = 1 , column = 2)
               
                
                selecting_booking = Tk()######################
                selecting_booking.geometry('1000x1000')####################################
                vamsiLabel = Label(selecting_booking, text = "Vamsi can add his code here this will be the selecting and booking window").pack()##########################################
                            
            else:
                unseceful = Label(login, text = "Incorrect Password, try again").grid(row = 1, column = 2)
        else:
            createuser = Label(login, text = "Please create an account by registering").grid(row = 1 , column = 2)        
                
    #login button
    login_Button = Button(login, text="Login", bg = 'red', command =login_message).grid(row=4, column=0)
    home_page_button=Button(login,text='HOME PAGE',bg='green',command=home_page).grid(row=5, column=0)
    
    login.mainloop()

def register():
    
    register = Toplevel()
    register.geometry('1000x1000')
    register.title('Register')


    rusername = Label(register, text = "Enter your name").grid(row=3, column = 2)
    rusername_entry = Entry(register)
    rusername_entry.grid(row = 3, column = 3)

    passd = Label(register, text = "Enter your password ").grid(row=4, column=2)
    passd_entry = Entry(register, show = '*')
    passd_entry.grid(row=4, column=3)

    passd_confir = Label(register, text = "Confirm Password").grid(row = 5,column = 2)
    passd_confir_entry = Entry(register,  show ='*' )
    passd_confir_entry.grid(row = 5, column = 3)
    
    email = Label(register, text = "Enter your email").grid(row = 6, column = 2)
    email_entry = Entry(register)
    email_entry.grid(row = 6, column = 3)

    group_1=StringVar()
    gender = Label(register, text = "Gender")
    gender.grid(row = 7, column =2)
    male_button = Radiobutton(register,variable=group_1,value="Male", text = "Male").grid(row = 7, column = 3)
    female_button = Radiobutton(register,variable=group_1,value="Female",text = "Female").grid(row = 8, column = 3)
    other_button = Radiobutton(register,variable=group_1,value="Other", text = "Other").grid(row = 9, column = 3)

    age_Label = Label(register, text = "Enter your age in years").grid(row = 10, column =2)
    age_entry = Entry(register)
    age_entry.grid(row = 10, column = 3)

    phonenumber_label = Label(register, text = "Enter your phone number").grid(row = 11, column = 2)
    phonenumber_entry = Entry(register)
    phonenumber_entry.grid(row = 11, column = 3) 
    
    def file_message():
        
        email = email_entry.get()
        password = passd_entry.get()
        password_confirmation = passd_confir_entry.get()
        
        if (str(password))==(str(password_confirmation)):
            file = open("User_credentials", 'a')
            file.write(str(email))
            file.write(' ')
            file.write(str(password))
            file.write(' ')
            file.close()
            userdict[str(email)] = str(password)

            correct_password_message = Label(register, text = "The password matches").grid(row = 5, column = 5)
            display_message_label = Label(register, text = "You have successfully registered").grid(row = 14, column = 5)

            if mycon.is_connected():
                print('succefully connected')
                msg1=rusername_entry.get()
                print(msg1)
                msg2=passd_entry.get()
                print(msg2)
                msg3=email_entry.get()
                print(msg3)
                msg4=group_1.get()
                print(msg4)
                msg5=age_entry.get()
                print(msg5)
                msg6=phonenumber_entry.get()#################
                print(msg6)
                mycursor=mycon.cursor()
                sql_query_1="""insert into bus_ticket.user_account_info(user_name,pass_word,e_mail,gender,age,phone_no)values(%s,%s,%s,%s,%s,%s)"""
                val=(msg1,msg2,msg3,msg4,msg5,msg6)
                mycursor.execute(sql_query_1,val)
                mycon.commit()
                print(mycursor.rowcount,'record inserted')
                df=pd.read_sql('select * from bus_ticket.user_account_info;',mycon)
                print(df)
            
        else:
            
            Incorrect_passd_label = Label(register, text = 'Password does not match').grid(row = 5, column = 5)
            
        

    
    register_button = Button(register, text = 'Register', bg = 'red', command = file_message).grid(row = 14, column = 3)

login_message = Label(choose, text = 'WELCOME TO 123BUS', height = 3, width = 20, fg = 'white',bg = 'blue', font = 'System').place(x = 425, y = 150)
flex1 = Label(choose, text = "The most trusted bus servies", bg = 'blue', fg = 'white',font = 'System').place(x = 10, y = 280)
flex2 = Label(choose, text = "Covid Precautions will be followed", bg = 'blue', fg = 'white',font = 'System').place(x = 10, y = 320)                                                                                       
open_login_button = Button(choose, text = 'Click here to login', command = login, width = 15, bg = 'blue', fg = 'white').place(x = 450, y = 435)
open_register_button = Button(choose, text = 'Click here to register', command = register, width = 15, bg = 'blue', fg = 'white').place(x = 450, y = 400)

choose.mainloop()