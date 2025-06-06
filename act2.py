from datetime import date
from tkinter import *
window=Tk()
window.title("demo project")
window.geometry("500x500")
lbl=Label(window,text="application",font=("Arial",20))
name_label=Label(text="full name",bg="black")
name_entry=Entry()
text_box=Text(height=3)

def display():
    name=name_entry.get()
    greet=f"Hello {name}, welcome to the application!\n"
    message="This is a simple GUI application.\n"
    global Message
    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END, date.today())

btn=Button(window,text="begin",command=display,height=1,bg="#1261A0",fg="white")
lbl.pack()
name_label.pack()
name_entry.pack()
text_box.pack()
btn.pack()
window.mainloop()