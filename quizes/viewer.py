from tkinter import *
import readQuiz
import random


class Viewer:
    # This is the first method which is called when a
    # new object of the class is initialized. This method
    # sets the question count to 0. and initialize all the
    # other methoods to display the content and make all the
    # functionalities available
    def __init__(self):
        self.index_no = 0
        # no of questions
        self.data_size = len(entries)

        # Will store temporary images
        self._itemsToDestroyOnrefresh = []

        # displays the button for next and exit.
        self.buttons()

        # assigns ques to the display_question function to update later.
        self.display_title()
        self.display_entry()

    def refresh(self):
        for im in self._itemsToDestroyOnrefresh:
            im.destroy()
        self.display_title()
        self.display_entry()

    def next_btn(self):
        if self.index_no < self.data_size - 1:
            self.index_no += 1
            self.refresh()

    def previous_btn(self):
        if self.index_no > 0:
            self.index_no -= 1
            self.refresh()

    def goto(self):
        entryVar = self.goto_entry.get()
        try:
            string_int = int(entryVar) - 1
            if 0 <= string_int < self.data_size - 1:
                self.index_no = string_int
                self.refresh()
        except:
            pass

    def random_btn(self):
        self.index_no = random.randint(0, self.data_size - 1)
        self.refresh()

    def buttons(self):
        previous_button = Button(gui, text="Previous", command=self.previous_btn,
                             width=10, bg="blue", fg="white", font=("ariel", 12, "bold"))
        previous_button.place(x=600, y=40)
        next_button = Button(gui, text="Next", command=self.next_btn,
                             width=10, bg="blue", fg="white", font=("ariel", 12, "bold"))
        next_button.place(x=750, y=40)
        self.goto_entry = Entry(gui, text="1",
                             width=10, bg="black", fg="white", font=("ariel", 8, "italic"))
        self.goto_entry.place(x=900, y=45)
        goto_button = Button(gui, text="Goto", command=self.goto,
                               width=10, bg="black", fg="white", font=("ariel", 10, "bold"))
        goto_button.place(x=950, y=40)
        random_button = Button(gui, text="Random", command=self.random_btn,
                             width=10, bg="yellow", fg="black", font=("ariel", 10, "bold"))
        random_button.place(x=1050, y=40)

        quit_button = Button(gui, text="Quit", command=gui.destroy,
                             width=5, bg="black", fg="white", font=("ariel", 16, " bold"))
        quit_button.place(x=1550, y=50)

    def display_entry(self):
        currentEntry = entries[self.index_no]
        yAlign = 250
        yOffset = 0
        xAlign = 200
        entryID = Label(gui, text=f"{currentEntry['ID']}", width=40,
                        font=('ariel', 16, 'bold'), anchor='w')
        entryID.place(x=0, y=6)
        altID = Label(gui, text=f"{currentEntry['IDAlt3']}", width=40,
                        font=('ariel', 10, 'normal'), anchor='w')
        altID.place(x=0, y=40)
        self._itemsToDestroyOnrefresh.append(entryID)
        for i, prefix in enumerate(currentEntry['Prefixes']):
            prefixID = Label(gui, text=f"{prefix['Type']}", width=30,
                            font=('ariel', 16, 'normal'), anchor='w')
            prefixID.place(x=20, y=80 + (yOffset + yAlign * i))
            self._itemsToDestroyOnrefresh.append(prefixID)
            for j, photo in enumerate(prefix["Photos"]):
                if j != 0 and j % 8 == 0:
                    yOffset += 200
                label = Label(image=photo)
                label.place(x=xAlign * (j % 8), y=120 + (yOffset + yAlign * i))
                self._itemsToDestroyOnrefresh.append(label)

    def display_title(self):
        # The title to be shown
        title = Label(gui, text="VIEWER entry %d / %d" % (self.index_no + 1, self.data_size),
                      width=100, bg="green", fg="white", font=("ariel", 20, "bold"))
        title.place(x=0, y=2)

gui = Tk()
gui.geometry("1665x850")
quizName = "huntingLicenceAnimalRecognition"
gui.title(quizName)

entries = readQuiz.createCatalog()

viewer = Viewer()
gui.mainloop()
