from Tkinter import *

def fun():
    print 'button clicked ...'

def main():
    r = Tk()

    b = Button(r, text='click', command = fun)
    b.pack()
    r.mainloop()

main()

