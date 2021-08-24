from tkinter import *


def button_clicked():
    result_label['text'] = int(input.get()) * 1.609344


window = Tk()
window.title('Mile to Km converter')
window.minsize(width=250, height=280)
window.config(padx=30, pady=70)


equal_label = Label(text='is equal to:', font=('Arial', 10, 'bold'))
equal_label.grid(column=0, row=1)

input = Entry(width=10)
input.grid(column=1, row=0)

miles_label = Label(text='Miles', font=('Arial', 10, 'bold'))
miles_label.grid(column=2, row=0)

result_label = Label(text='0', font=('Arial', 10))
result_label.grid(column=1, row=1)

km_label = Label(text='Km', font=('Arial', 10, 'bold'))
km_label.grid(column=2, row=1)


button = Button(text='Convert', command=button_clicked)
button.grid(column=1, row=2)





window.mainloop()
