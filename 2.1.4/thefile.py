import tkinter as tki

class App(object):

    def init(self):
        self.root = tki.Tk()
        self.root.wm_title("Play With python")
        for r in range(8):
            self.root.rowconfigure(r, weight=1)
        for c in range(2):
            self.root.columnconfigure(c, weight=1)
    # Create Frames
        Frame1 = tki.Frame(self.root, borderwidth=1, bg = 'blue')
        Frame1.grid(row = 0, column = 0, rowspan = 2, columnspan = 2, sticky = 'w, e, n, s')

        Frame2 = tki.Frame(self.root, borderwidth=1, bg = 'blue')
        Frame2.grid(row = 2, column = 0, rowspan = 2, columnspan = 2, sticky = 'w, e, n, s')

        Frame3 = tki.Frame(self.root, borderwidth=1, bg = 'blue')
        Frame3.grid(row = 4, column = 0, rowspan = 2, columnspan = 2, sticky = 'w, e, n, s')

        Frame4 = tki.Frame(self.root, borderwidth=1, bg = 'blue')
        Frame4.grid(row = 6, column = 0, rowspan = 2, columnspan = 2, sticky = 'w, e, n, s')

app = App()
app.root.mainloop()