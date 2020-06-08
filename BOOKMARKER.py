import tkinter as tk
import webbrowser
#Now, we will create 2 functions, each for opening your LinkedIn and Facebook profiles. You can open these pages on a new tab in your browser, thanks to open_new_tab(‘URL’) method of webbrowser library.

def linkedin(event):
    webbrowser.open_new_tab(' put your linkedin profile link here ')

def facebook(event):
    webbrowser.open_new_tab(' put your facebook profile link here ')
#Now, let’s create a window for our app and name it as ‘Social Media Bookmark App’.

window=tk.Tk()
window.geometry("300x200")
window.title("Social Media Bookmark App")
#Let’s create a label to add some text to our app.

label1=tk.Label(text="My Social Media")
label1.grid(column=0,row=0)
#You can also style your fonts in the label in the following way if needed.

label1 = tk.Label(text = "My social Media", font=("Times new roman",20))
#Now, create 2 buttons each for LinkedIn and Facebook. Arrange them using the ‘grid’ method. Note that I used different colors for the buttons. We can color the button using ‘bg‘ argument.


button1=tk.Button(window,text="Linkedin",bg="orange")
button1.grid(column=1,row=1)
button2=tk.Button(window,text="Facebook",bg="pink")
button2.grid(column=3,row=1)
#We will bind these buttons to their corresponding functions using the ‘bind’ method.

button1.bind("<Button-1>",linkedin)
button2.bind("<Button-1>",facebook)
#Finally, let’s run everything inside the window using ‘mainloop()’ method.

window.mainloop()
