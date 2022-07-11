# import tkinter
from tkinter import *

# tkinter object
window = Tk()

window.title("xyz")

# function for submit button
def click():
    enter_text = str(textbox.get())
    output.delete(0.0,END)

#     exception handling
    try:
        define = my_dict[enter_text]
    except:
        define = 'not available'
    output.insert(END,define)

Label(window,text = 'Hello I am your first GUI',height = 20,bg = 'red',fg='black').grid(row=0,column=0,sticky=W)


# text box
textbox = Entry(window,width=30,bg='white')
textbox.grid(row=0,column=1)

# submit button
Button(window,text = 'SUBMIT',width=10,command=click,bg = 'blue',fg='white').grid(row=0,column=2)

output = Text(window,width=30,height=20,bg = 'white')
output.grid(row=0,column=3)


# create the data
my_dict = {
    'name':['Mohit','Muzakkir','John Cena'],
    'bug':'code error'
}















# run the code infinite times
window.mainloop()

