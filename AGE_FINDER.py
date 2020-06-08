import datetime
import tkinter as tk
from PIL import Image,ImageTk
#Now, let’s create a simple window for our app and name it as Age Calculator App.

window=tk.Tk()
window.geometry("620x780")
window.title(" Age Calculator App ")

#Then, we are going to create four labels, each for the name, year, month, and the date, and put them in the grid.

name = tk.Label(text = "Name")
name.grid(column=0,row=1)
year = tk.Label(text = "Year")
year.grid(column=0,row=2)
month = tk.Label(text = "Month")
month.grid(column=0,row=3)
date = tk.Label(text = "Day")
date.grid(column=0,row=4)
#We will create entry fields to get the user inputs corresponding to all the labels created. Put them at the right side of the corresponding labels using the grid method.

nameEntry = tk.Entry()
nameEntry.grid(column=1,row=1)
yearEntry = tk.Entry()
yearEntry.grid(column=1,row=2)
monthEntry = tk.Entry()
monthEntry.grid(column=1,row=3)
dateEntry = tk.Entry()
dateEntry.grid(column=1,row=4)


'''Then, we are going to define a function to get user inputs. We name that function as getInput(). 

Inside that function, we will create an object of the Person class (which will be defined later), and pass the name and birth date to the “__init__” method of that class.

Note that we use the predefined int() method to convert values into integer format. Then, we create a text area that will display the age of the user as output.'''

def getInput():
    name=nameEntry.get()
    monkey = Person(name,datetime.date(int(yearEntry.get()),int(monthEntry.get()),int(dateEntry.get())))
    
    textArea = tk.Text(master=window,height=10,width=25)
    textArea.grid(column=1,row=6)
    answer = " Heyy {monkey}!!!. You are {age} years old!!! ".format(monkey=name, age=monkey.age())
    textArea.insert(tk.END,answer)
    
    
button=tk.Button(window,text="Calculate Age",command=getInput,bg="green")
button.grid(column=1,row=5)
#Now, let’s define the Person class. We are also going to code the __init__ method and also the age method, which will calculate the age of the user by subtracting the user’s birth date from today’s date.

class Person:
    def __init__(self,name,birthdate):
        self.name = name
        self.birthdate = birthdate
    def age(self):
        today = datetime.date.today()
        age = today.year-self.birthdate.year
        return age
    
    
image=Image.open('use.jpg')
image.thumbnail((500,500),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
label_image=tk.Label(image=photo)
label_image.grid(column=1,row=0)
image=Image.open('use.jpg')
image.thumbnail((600,600),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
label_image=tk.Label(image=photo)
label_image.grid(column=1,row=6)

window.mainloop()
