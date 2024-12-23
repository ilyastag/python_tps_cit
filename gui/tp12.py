import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

def calculer_somme():
    try:
        s=int(nombre1.get())+int(nombre2.get())
        label1.configure(text=f"Résultat: {s}")
    except ValueError as v:
        messagebox.showerror("Error",v)


def reset():
    nombre1.set(value="0")
    nombre2.set(value="0")
    label1.configure(text="Résultat: 0")

w_width=20
w_font=('Tahoma',20)



ff=tk.Tk()
ff.title("Somme")
ff.geometry("350x550")
ff.configure(background="darkorange")

nombre1=tk.StringVar(value="0")
nombre2=tk.StringVar(value="0")

img=PhotoImage(file="D:\CITProjects\Projects_Analyste\gui\clipartcalc.png")
labelimg=tk.Label(ff,image=img)
entry1=tk.Entry(ff, width=w_width, font=w_font,textvariable=nombre1,)
entry2=tk.Entry(ff, width=w_width, font=w_font,textvariable=nombre2)

label1=tk.Label(ff, text="Résultat:",width=w_width,font=w_font, bg="green",fg="yellow")
button_calculer=tk.Button(ff,text="Calculer", width=w_width,font=w_font, command=calculer_somme)
button_effacer=tk.Button(ff,text="Reset", width=w_width,font=w_font, 
                         command=reset)

labelimg.pack(pady=10)
entry1.pack(pady=10)
entry2.pack(pady=10)
label1.pack(pady=10)
button_calculer.pack(pady=10)
button_effacer.pack(pady=10)

ff.mainloop()