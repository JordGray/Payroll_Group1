import tkinter as tk
from tkinter import Label,Button,messagebox
import os

font10="{Courier New} 10 normal"
font11="{U.S 101} 30 bold"
font12="Al-Aramco 11 bold"
font13="{Courier New} 10 bold"
font14="{Segoe UI} 15 bold"
font15="Arial 13 bold"
font16="{Segoe UI} 13 bold"




class App1:
 def __init__(self,top):
 	self.top=top

 	top.title("Payroll Management")
 	top.geometry("800x600")
 	top.configure(background="#091833")

 	

 	self.Label1=tk.Label(master=top,text="Payroll Management System",font=font11,background="#091833",foreground="#f2a343")
 	self.Label1.place(relx=0.12,rely=0.02,height=50,width=600)

 	self.Label2=tk.Label(master=top,text="Username",font=font12,background="#091833",foreground="#bac8bd")
 	self.Label2.place(relx=0.3,rely=0.25)

 	self.Label3=tk.Label(master=top,text="Password",font=font12,background="#091833",foreground="#bac8bd")
 	self.Label3.place(relx=0.3,rely=0.4)


 	self.entry1=tk.Entry(master=top,background="#d9d9d9",foreground="#c60000",font=font13)
 	self.entry1.place(relx=0.35,rely=0.3)

 	self.entry2=tk.Entry(master=top,background="#d9d9d9",foreground="#c60000",font=font13,show="*")
 	self.entry2.place(relx=0.35,rely=0.45)



 	self.Button1= tk.Button(master=top,text="Login",background="#122c63",font=font14,foreground="#ffffff",command=self.receive)
 	self.Button1.place(relx=0.4,rely=0.55,height=35,width=80)

 	self.Button2= tk.Button(master=top,text="SignUp",background="#122c63",font=font14,foreground="#ffffff",command=self.Msg)
 	self.Button2.place(relx=0.4,rely=0.7,height=35,width=80)


 def send(self):
    global username
    global password
    username = self.entry1.get()
    password = self.entry2.get()
    f = open("database.txt", "a")
    f.write(username)
    f.write("\n")
    f.write(password)
    f.write("\n")
    f.close()

 def Msg(self):
    MsgBox = tk.messagebox.askquestion ('Terms and policies','Do you Accept our Terms and Policies')
    if MsgBox == 'yes':

       tk.messagebox.showinfo('Sucess','Your account has been created.')
       self.send()

    else:
        tk.messagebox.showinfo('Fail','You can\'t create account without accepting terms and policies.' )



 def receive(self):
 	with open('database.txt') as f:
 		if self.entry1.get() + "\n" in f.read():
 			tk.messagebox.showinfo('Sucess','Welcome '+self.entry1.get()+". You have got a account with us" )
 		else:
 			tk.messagebox.showinfo('Fail','Sorry, No username with id '+self.entry1.get()+" is registered with us." )
 

root=tk.Tk()

my_gui=App1(root)
root.mainloop()