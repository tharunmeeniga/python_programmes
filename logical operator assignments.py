from tkinter import*
from tkinter import messagebox, Label

window=Tk()
window.title("fine")
window.geometry("350x400")
window.config(bg="yellow")
def speed_cal():
    speed=int(e1.get())
    limit=int(e2.get())
    if speed<=limit:
        messagebox.showinfo("result","no penalty")
    elif speed<=limit+20:
        messagebox.showinfo("result","warning:you are going speed")
    else:
        messagebox.showinfo("result","penalty")






l1=Label(window,text="enter the speed")
l1.grid(row=0,column=0)
e1=Entry(window)
e1.grid(row=0,column=1)
l2=Label(window,text="enter the speed_limit")
l2.grid(row=1,column=0)
e2=Entry(window)
e2.grid(row=1,column=1)
b1=Button(window,text="speed_cal",command=speed_cal)
b1.grid(row=2,column=1)


window.mainloop()
