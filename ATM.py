# write a program to perform atm operations
from tkinter import*
from tkinter import messagebox

window=Tk()
window.title("ATM")
window.config(bg="black")
window.geometry("300x400")
def Atm_operation():
    balance=10000
    withdrawamnt=int(e1.get())
    if withdrawamnt<=balance and withdrawamnt%100==0:
        messagebox.showinfo("daily limit","take your money and take your money in 100rs notes")
    elif withdrawamnt>balance:
        messagebox.showinfo("daily limit","your daily limit is finished")
    else:
        messagebox.showinfo(("balance","total balance is"))
        total_bal=withdrawamnt-balance












l1=Label(window,text="enter the wityhdraw amnt")
l1.grid(row=0,column=0)
e1=Entry(window)
e1.grid(row=0,column=1)
b1=Button(window,text="withdraw",command=Atm_operation)
b1.grid(row=2,column=1)



window.mainloop()




