from tkinter import Label, Tk, Frame, LEFT, RIGHT, TOP, BOTTOM,RAISED

class MainGUI:
    def __init__(self, master):
        self.master = master
        self.backgroundColor = "pink"
        master.title("A simple GUI.")

        self.leftLabel = Label(master, text="LEFT", width=10, height=10,relief=RAISED, background="grey")
        self.leftLabel.pack(side=LEFT)

        self.rightLabel = Label(master, text="RIGHT", width=10, height=10,relief=RAISED, background="grey")
        self.rightLabel.pack(side=RIGHT)

        self.topLabel = Label(master, text="TOP", width=10, height=10,relief=RAISED, background="grey")
        self.topLabel.pack(side=TOP)

        self.bottomLabel = Label(master, text="BOTTOM", width=10, height=10,relief=RAISED, background="grey")
        self.bottomLabel.pack(side=BOTTOM)


        self.frame = Frame(master, width=100, height=100)
        self.frame.bind('<KeyRelease>',self.keyPressed)
        self.frame.pack()
        self.frame.focus()

        print("hello")
    def keyPressed(self, event):

        self.clearLabelColor()

        if event.char == "a" or event.char == "A":
            self.leftLabel.configure(background="pink")
        if event.char == "s" or event.char == "S":
            self.bottomLabel.configure(background="pink")
        if event.char == "d" or event.char == "D":
            self.rightLabel.configure(background="pink")
        if event.char == "w" or event.char == "W":
            self.topLabel.configure(background="pink")

        return

    def clearLabelColor(self):
        self.leftLabel.configure(background="grey")
        self.bottomLabel.configure(background="grey")
        self.topLabel.configure(background="grey")
        self.rightLabel.configure(background="grey")


root = Tk()




gui = MainGUI(root)



root.mainloop()

