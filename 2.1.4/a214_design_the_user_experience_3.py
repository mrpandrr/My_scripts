import tkinter as tki

class App(object):

    def __init__(self):
        self.root = tki.Tk()        
        self.root.wm_title("Play With python")
        for r in range(8):
            self.root.rowconfigure(r, weight=1)
        for c in range(2):
            self.root.columnconfigure(c, weight=1)
    # Create Frames
        Frame1 = tki.Frame(self.root, width=500, height=200, background = 'blue')
        sizeofcolumn = 2
        Frame1.grid(row = 3, column = 0, sticky = 'n,e,w,s')

        Frame2 = tki.Frame(self.root, width=200, height=200, background = 'green')
        Frame2.grid(row = 3, column = 1, sticky = 'n,e,w,s')

        Frame3 = tki.Frame(self.root, width=500, height=200, background = 'red')
        Frame3.grid(row = 4, column = 0, sticky = 'n,e,w,s')

        Frame4 = tki.Frame(self.root, width=200, height=200, background = 'yellow')
        Frame4.grid(row = 4, column = 1, sticky = 'n,e,w,s')

app = App()
app.root.mainloop()