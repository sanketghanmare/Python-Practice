# import tkinter
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

# print(tkinter.TkVersion)
# print(tkinter.TclVersion)
# tkinter._test()

mainWindows = tkinter.Tk()

mainWindows.title("Hello World")
mainWindows.geometry('640x480-8-200')

label = tkinter.Label(mainWindows, text="Hello World")
# label.pack(side='top')
label.grid(row=0, column=0)

leftFrame = tkinter.Frame(mainWindows)
leftFrame.grid(row=1, column=1)

# canvas = tkinter.Canvas(mainWindows, relief='raised', borderwidth=1)
canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
# canvas.pack(side='left', fill=tkinter.X, expand=True)
# canvas.pack(side='left')
# canvas.pack(side='left', anchor='n')
canvas.grid(row=1, column=0)

rightFrame = tkinter.Frame(mainWindows)
# rightFrame.pack(side='left', anchor='n', expand='True')
rightFrame.grid(row=1, column=2, sticky='n')

# button1 = tkinter.Button(mainWindows, text="button1")
# button2 = tkinter.Button(mainWindows, text="button2")
# button3 = tkinter.Button(mainWindows, text="button3")

button1 = tkinter.Button(rightFrame, text="button1")
button2 = tkinter.Button(rightFrame, text="button2")
button3 = tkinter.Button(rightFrame, text="button3")

# button1.pack(side='left', anchor='n')
# button2.pack(side='left', anchor='s')
# button3.pack(side='left', anchor='e')

# button1.pack(side='top')
# button2.pack(side='top')
# button3.pack(side='top')

button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)

mainWindows.mainloop()
