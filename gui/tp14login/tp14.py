import tkinter as tk

root = tk.Tk()
root.title("Login")
root.geometry("600x350")

users=[
    {"username":"admin","password":"admin"},
    {"username":"ahmed","password":"123"},
    {"username":"omar","password":"sanfour"},
    {"username":"admin","password":"admin"},
    {"username":"admin","password":"admin"}
       ]



label1=tk.Label(root,text="Login page",padx=10,pady=10,anchor="e",bg="black",fg="white",font=("Arial",20))
label1.grid(row=0,column=0,sticky="nsew")
frame1=tk.Frame(root,padx=10,pady=10,bg="green")
frame1.grid(row=1,column=0)
img=tk.PhotoImage(file="D:\python_tps_cit\gui\\tp14login\profil.png")
label2=tk.Label(frame1,image=img,padx=10,pady=10)
label2.pack(side="left")
frame2=tk.Frame(frame1,padx=10,pady=10)
frame2.pack(side="left")

usernamelabel=tk.Label(frame2,text="Username: ",font=("Arial",15))
usernamelabel.grid(row=0,column=0,sticky="ew",padx=10,pady=10)
usernameentry=tk.Entry(frame2,font=("Arial",15))
usernameentry.grid(row=0,column=1,sticky="ew")

pwdlabel=tk.Label(frame2,text="Password: ",font=("Arial",15))
pwdlabel.grid(row=1,column=0,sticky="ew",padx=10,pady=10)
pwdentry=tk.Entry(frame2,font=("Arial",15),show="*")
pwdentry.grid(row=1,column=1,sticky="ew")

frame3=tk.Frame(frame2,padx=10,pady=10)
frame3.grid(row=2,column=0,columnspan=2,sticky="ew")

loginbutton=tk.Button(frame3,text="Login",font=("Arial",15),bg="blue",fg="white",padx=10)
loginbutton.pack(side="left",fill="x",expand=True,padx=10)
signbutton=tk.Button(frame3,text="Sign up",font=("Arial",15),bg="blue",fg="white")
signbutton.pack(side="right",fill="x",expand=True)



root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=20)


frame2.columnconfigure(0,weight=1)
frame2.columnconfigure(1,weight=3)


usernameentry.focus_set()

def funt(event):
    event.widget.config(bg="yellow")

def funt2(event):
    event.widget.config(bg="white")


root.mainloop()