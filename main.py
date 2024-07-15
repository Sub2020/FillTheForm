from tkinter import*

def saveToFile():
    saveFirstName = firstNameEntry.get()
    saveLastName = lastNameEntry.get()
    SaveGender = gender.get()
    SaveEmail = email.get()
    SavePhone = phone.get()
    SaveBirth = birth.get()
    SaveCity = city.get()
    SaveState = state.get()
    SaveZip = zip.get()
    SaveTip = tip.get()

    file = open('C:/Users/Devraj/Desktop/notepade.txt','a+')
    file.write(saveFirstName)
    file.write(',')
    file.write(saveLastName)
    file.write(',')

    if SaveGender ==1:
        file.write('M')
    elif SaveGender == 2:
        file.write(F)
    else:
        pass


    file.write(',')
    file.write(SaveBirth)
    file.write(',')
    file.write(SaveEmail)
    file.write(',')
    file.write(SavePhone)
    file.write(',')
    file.write(SaveCity)
    file.write(',')
    file.write(SaveState)
    file.write(',')
    file.write(SaveZip)
    file.write('\n')

    file.close()


    firstNameEntry.delete(0,END)
    lastNameEntry.delete(0, END)
    male.deselect()
    female.deselect()
    no.select()
    email.delete(0,END)
    phone.delete(0,END)
    phone.delete(0,END)
    city.delete(0, END)
    state.delete(0, END)
    birth.delete(0, END)
    zip.delete(0, END)


root = Tk()
root.geometry('270x300')
root.title('Entry form')

firstName = Label(root, text = 'Full Name: ', fg='violet')
firstName.grid(row=0, sticky='E')
lastName = Label(root, text = 'last Name: ', fg='indigo')
lastName.grid(row=1, sticky='E')
birth = Label(root, text = 'Date of Birth:\n(mm/dd/yyyy)', fg='blue')
birth.grid(row=3, sticky='E')
email = Label(root, text = 'Email: ', fg='green')
email.grid(row=4, sticky='E')
phone = Label(root, text='Phone No.: ', fg= 'red')
phone.grid(row=5, sticky='E')
city = Label(root, text= 'City:', fg='black')
city.grid(row=6, sticky='E')
state = Label(root, text='State: ', fg='pink')
state.grid(row=7, sticky='E')
zip = Label(root, text='ZipCode:', fg='brown')
zip.grid(row=8, sticky='E')

firstNameEntry = Entry()
lastNameEntry = Entry()
birth = Entry()
email = Entry()
phone = Entry()
city = Entry()
state = Entry()
zip = Entry()

firstNameEntry.grid(row=0, column=1)
lastNameEntry.grid(row=1, column=1)
birth.grid(row=3, column=1)
email.grid(row=4, column=1)
phone.grid(row=5, column=1)
city.grid(row=6, column=1)
state.grid(row=7, column=1)
zip.grid(row=8, column=1)

gender = IntVar()


male = Radiobutton(root, text = 'Male', variable=gender, value=1)
female = Radiobutton(root, text = 'Female', variable=gender, value=2)
other = Radiobutton(root, text = 'Other', variable=gender, value=3)
no = Radiobutton(root, variable=gender, value=3)


male.place(x=58, y=42)
female.grid(row=2, column=1)
other.place(x=175, y=42)

submitButton = Button(root, text='Submit', command=saveToFile, bg='orange', fg='black')
submitButton.place(x=60, y=220, width=150)

quitButton = Button(root, text='Quit', bg='orange', fg='purple', command=root.quit)
quitButton.place(x=60, y=260, width=150)

root.mainloop()
