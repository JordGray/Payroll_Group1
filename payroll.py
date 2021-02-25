import tkinter as tk
from tkinter import Label,Button,messagebox
import os
import re


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
    username =cipher_encrypt(self.entry1.get(),4)
    password = cipher_encrypt(self.entry2.get(),4)
    f = open("database.txt", "a")
    f.write(username)
    f.write("\n")
    f.write(password)
    f.write("\n")
    f.close()

 def Msg(self):
    u = self.entry1.get()
    p = self.entry2.get()
    if (("<" in u) or (">" in u)):
        tk.messagebox.showinfo('Sucess','You cannot use special characters \"<\" or \">\" in your username')
    else:
        if ("<" or ">") in p:
            tk.messagebox.showinfo('Sucess','You cannot use special characters \"<\" or \">\" in your password')
        else:
            if password_checker(p):
                MsgBox = tk.messagebox.askquestion ('Terms and policies','Do you Accept our Terms and Policies')
                if MsgBox == 'yes':
                    tk.messagebox.showinfo('Sucess','Your account has been created.')
                    self.send()

                else:
                    tk.messagebox.showinfo('Fail','You can\'t create account without accepting terms and policies.' )
            else:
                tk.messagebox.showinfo('Invalid Password!!!.', 'Password must be 8 characters long.Should include a uppercase,a lowecase and a special character.No spaces allowed.')



 def receive(self):
 	with open('database.txt') as f:
 		if self.entry1.get() + "\n" in cipher_decrypt(f.read(),4):
 			tk.messagebox.showinfo('Sucess','Welcome '+self.entry1.get()+". You have got a account with us" )
 		else:
 			tk.messagebox.showinfo('Fail','Sorry, No username with id '+self.entry1.get()+" is registered with us." )


# The Encryption Function
def cipher_encrypt(plain_text, key):

    encrypted = ""

    for c in plain_text:

        if c.isupper(): #check if it's an uppercase character

            c_index = ord(c) - ord('A')

            # shift the current character by key positions
            c_shifted = (c_index + key) % 26 + ord('A')

            c_new = chr(c_shifted)

            encrypted += c_new

        elif c.islower(): #check if its a lowecase character

            # subtract the unicode of 'a' to get index in [0-25) range
            c_index = ord(c) - ord('a') 

            c_shifted = (c_index + key) % 26 + ord('a')

            c_new = chr(c_shifted)

            encrypted += c_new

        elif c.isdigit():

            # if it's a number,shift its actual value 
            c_new = (int(c) + key) % 10

            encrypted += str(c_new)

        else:

            # if its neither alphabetical nor a number, just leave it like that
            encrypted += c

    return encrypted

# The Decryption Function
def cipher_decrypt(ciphertext, key):

    decrypted = ""

    for c in ciphertext:

        if c.isupper(): 

            c_index = ord(c) - ord('A')

            # shift the current character to left by key positions to get its original position
            c_og_pos = (c_index - key) % 26 + ord('A')

            c_og = chr(c_og_pos)

            decrypted += c_og

        elif c.islower(): 

            c_index = ord(c) - ord('a') 

            c_og_pos = (c_index - key) % 26 + ord('a')

            c_og = chr(c_og_pos)

            decrypted += c_og

        elif c.isdigit():

            # if it's a number,shift its actual value 
            c_og = (int(c) - key) % 10

            decrypted += str(c_og)

        else:

            # if its neither alphabetical nor a number, just leave it like that
            decrypted += c

    return decrypted

def password_checker(pw):
    flag = 0
    while True:   
        if (len(pw)<8): 
            flag = -1
            break
        elif not re.search("[a-z]", pw): 
            flag = -1
            break
        elif not re.search("[A-Z]", pw): 
            flag = -1
            break
        elif not re.search("[0-9]", pw): 
            flag = -1
            break
        elif not re.search("[_@$]", pw): 
            flag = -1
            break
        elif re.search("\s", pw): 
            flag = -1
            break
        else: 
            flag = 0
            return True
            break
  
    if flag ==-1: 
        return False


 

root=tk.Tk()

my_gui=App1(root)
root.mainloop()