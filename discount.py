from tkinter import*
from tkinter import messagebox
window=Tk()
window.title("Discount")
window.config(bg="pink")
window.geometry("250x300")
def discount_eligibility():
 purchase_amount=int(e1.get())
 membership=True
 if purchase_amount>5000 and membership==True:
  messagebox.showinfo("discount details","you will get 20% discount")
 else:
  messagebox.showinfo ("discount details","you are not get any discount")


l1=Label(window,text="total purchase amount")
l1.grid(row=0,column=0)
e1=Entry(window)
e1.grid(row=0,column=1)

b1=Button(window,text="Discount",command=discount_eligibility)
b1.grid(row=2,column=1)


window.mainloop()
