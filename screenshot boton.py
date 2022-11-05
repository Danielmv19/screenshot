import pyautogui 
import tkinter 
from tkinter import messagebox
from tkinter import *
from tkinter import ttk

def captura():
    cap = pyautogui.screenshot()
    cap.save("screenshot.png")

root = Tk()
root.title("Ventana de captura")
root.geometry("400x200")
root.configure(width=400, height=200)


bg = PhotoImage(file = ("women.jpg"))
lb = ttk.Label(root, image= bg)
lb.place(x=0, y=0)



label = ttk.Label(root, text=("Screenshot")).place(x=160, y=50)
ttk.Button(None, text='Nueva', command=captura).place(x=160, y=90)
root.mainloop()
