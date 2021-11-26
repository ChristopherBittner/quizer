# importing the tkinter module and PIL
# that is pillow module
from tkinter import *
from PIL import ImageTk, Image


def select(img_no):
    pass

def next():
    pass

def question(questionSummary, pathsToImage, selections=[], correctSelectionIndex=0):
    root = Tk()
    root.title(questionSummary)
    root.geometry("700x700")

    image = ImageTk.PhotoImage(Image.open(pathsToImage))
    label = Label(image=image)
    label.grid(row=0, column=0, columnspan=3)

    buttons = []
    currentRow = 1
    length = 100
    for i, s in enumerate(selections):
        buttons.append(Button(root, text=f"{i}%s{s}" % ((length - len(s)) * " "), command=lambda: select(i)))
        buttons[-1].grid(row=currentRow, column=0)
        currentRow += 1
    # button_next = Button(root, text="Next question", command=back)

    # # We will have three button back ,forward and exit
    # button_1 = Button(root, text="Back", command=back,
    #                      state=DISABLED)
    #
    # # root.quit for closing the app
    # button_exit = Button(root, text="Exit",
    #                      command=root.quit)
    #
    # button_forward = Button(root, text="Forward",
    #                         command=lambda: forward(1))
    #
    # # grid function is for placing the buttons in the frame
    # button_back.grid(row=5, column=0)
    # button_exit.grid(row=5, column=1)
    # button_forward.grid(row=5, column=2)

    root.mainloop()
