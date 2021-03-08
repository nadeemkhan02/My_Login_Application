import tkinter
import sqlite3
from tkinter import messagebox
from PIL import Image, ImageTk 



root=tkinter.Tk()
root.resizable(width=False, height=False)




#Home screen configuretion
root.configure(background='black')
root.title("User Login")
root.geometry("720x480")
root.iconbitmap(r'shield.ico')



#Database
#connect the data base
conn = sqlite3.connect('user_pass.db')

#creating the cursor
c = conn.cursor()



c.execute("""CREATE TABLE user (
    user_name text NOT NULL,
     password text NOT NULL);
     """)
c.execute("SELECT * FROM user")





#checking for new user name
def check():
    #connect the data base
    conn = sqlite3.connect('user_pass.db')

    #creating the cursor
    c = conn.cursor()
    global top
    find_uer = ("SELECT user_name FROM user WHERE user_name=?")
    c.execute(find_uer,[(e3.get())])
 
    result = c.fetchall()

    if result and e3.get() == "" and e4.get() == "":
        message = messagebox.showerror("username exist","Try another user name")
        e3.delete(0, "end")
        e4.delete(0, "end")

    elif len(e3.get())<=8:
        message = messagebox.showerror("user name type error","username must be greater then 8")
        e3.delete(0, "end")
        e4.delete(0, "end")

    else:
        c.execute("INSERT INTO user VALUES (:user_name, :password)",
                {
                    "user_name": e3.get(),
                    "password": e4.get()
                }
                )
        message1 = messagebox.showinfo("username created","successfully username created")
        top.destroy()
    conn.commit()
    conn.close()
    
'''
    elif e3.get != "" and e4.get() != "":


        c.execute("INSERT INTO user VALUES (:user_name, :password)",
                {
                    "user_name": e3.get(),
                    "password": e4.get()
                }
                )
        message1 = messagebox.showinfo("username created","successfully username created")
        top.destroy()
'''




def valid_user():
    global top1
    
    top1 = tkinter.Tk()
    top1.configure(background='black')
    top1.title("Valid User")
    top1.geometry("500x350")
    top1.iconbitmap(r'shield.ico')
    top1.resizable(width = False, height = False)
    button_query = tkinter.Button(top1, text = "see all logs", command = query)
    button_query.grid(row = 0, column = 0, padx = 100, pady = 20)

    
  

    
  #function for existing user
def all_user():
        #connect the data base
    conn = sqlite3.connect('user_pass.db')

    #creating the cursor
    c = conn.cursor()
    global top

    find_uer = ("SELECT user_name FROM user WHERE user_name=? AND password = ?")
    c.execute(find_uer,[(e1.get()), (e2.get())])
 
    result = c.fetchall()
    if result and e1.get() != "" and e2.get() != "":
        message3 =  messagebox.showinfo("loged in", "Hello user")
        valid_user()
        
        
    else:
        message4 =  messagebox.showerror("oops!", "User name not found")
        e1.delete(0, "end")
        e2.delete(0, "end")

    conn.commit()
    conn.close()


#new_user function for adding entry in database
def new_user():
    #new screen display
    global top
    top = tkinter.Tk()
    top.configure(background='black')
    top.title("New User")
    top.geometry("500x350")
    top.iconbitmap(r'shield.ico')
    top.resizable(width = False, height = False)

    #new screeen label and entry
    label7 = tkinter.Label(top, text = "", bg = "black")
    label7.grid(row = 0, column = 0, padx = 50, pady = 30)

    frame = tkinter.LabelFrame(top, text = "User Logins", bg = 'black', font = ("Helvetica", 10), fg = "red")
    frame.grid(row = 1, column = 0, padx = 80, ipadx = 10)

    label5 = tkinter.Label(frame, text = "Enter New User Name:  ", bg = "black", fg = "green", font = ("Helvetica", 10), pady = 5, padx = 5)
    label5.grid(row =0, column = 0)
    label6 = tkinter.Label(frame, text = "Enter Your Password:  ", bg = "black", fg = "green", font = ("Helvetica", 10), pady = 5, padx = 5)
    label6.grid(row =1, column = 0)
    global e3
    global e4
    e3 = tkinter.Entry(frame, borderwidth = 1)
    e3.grid(row = 0, column = 1)
    e4 = tkinter.Entry(frame, borderwidth = 1, show = "*")
    e4.grid(row = 1, column = 1)
    
    button3 = tkinter.Button(frame, text = "Submit", command = check)
    button3.grid(row = 2, column = 1, pady = 3)



def query():
    global top1
    #connect the data base
    conn = sqlite3.connect('user_pass.db')

    #creating the cursor
    c = conn.cursor()

    c.execute("SELECT *, oid FROM user")
    records = c.fetchall()
    print_record = ''
    for record in records:
        print_record += str(record[0]) +"   "+str(record[1])+"   "+ str(record[2])+"\n"
    label7 = tkinter.Label(top1, text = print_record, bg = "black", font = ("Helvetica", 13), fg = "red")
    label7.grid(row = 2, column = 0, padx = 150)

    
    conn.commit()
    conn.close()



#adding background image
img = Image.open(r'img.png')
img1 = img.resize((720, 480), Image.ANTIALIAS)
new_img = ImageTk.PhotoImage(img1)
background_label = tkinter.Label(root, image=new_img)
background_label.place(x=1, y=1)

#putting backgroung image on screen
label3 = tkinter.Label(root, text = "", bg = "black")
label3.grid(row = 0, column = 0, padx = 140, pady = 65)

#creating frame for login stufs
fram = tkinter.LabelFrame(root, text = "User Logins", bg = 'black', font = ("Helvetica", 10), fg = "red")
fram.grid(row = 1, column = 0, padx = 140, ipadx = 10)

#creating username password label and putting them in frame
label = tkinter.Label(fram, text = "Enter Your User Name:  ", bg = "black", fg = "green", font = ("Helvetica", 10), pady = 5, padx = 5)
label.grid(row =0, column = 0)
label2 = tkinter.Label(fram, text = "Enter Your Password:  ", bg = "black", fg = "green", font = ("Helvetica", 10), pady = 5, padx = 5)
label2.grid(row =1, column = 0)

#creating entry for user name password and putting them in frame
global e1
global e2
e1 = tkinter.Entry(fram, borderwidth = 1)
e1.grid(row = 0, column = 1)
e2 = tkinter.Entry(fram, borderwidth = 1, show = "*")
e2.grid(row = 1, column = 1)

#button for submit
button1 = tkinter.Button(fram, text = "Submit", command = all_user)
button1.grid(row = 2, column = 1, pady = 3)

#button for create new account

button2 = tkinter.Button(root, text = "Creat Account", command = new_user)
button2.grid(row = 2, column = 0, padx = 140, pady = 10)


conn.commit()
conn.close


root.mainloop()