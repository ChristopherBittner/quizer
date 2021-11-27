from tkinter import *

# and import messagebox as mb from tkinter
from tkinter import messagebox as mb
import readQuiz

# class to define the components of the GUI
class Quiz:
    # This is the first method which is called when a
    # new object of the class is initialized. This method
    # sets the question count to 0. and initialize all the
    # other methoods to display the content and make all the
    # functionalities available
    def __init__(self):

        # set question number to 0
        self.q_no = 0

        # no of questions
        self.data_size = len(question)

        # Will store temporary images
        self.images = []

        # assigns ques to the display_question function to update later.
        self.display_title()
        self.display_question()

        # opt_selected holds an integer value which is used for
        # selected option in a question.
        self.opt_selected = IntVar()

        # displaying radio button for the current question and used to
        # display options for the current question
        self.opts = self.radio_buttons()

        # display options for the current question
        self.display_options()

        # displays the button for next and exit.
        self.buttons()

        # keep a counter of correct answers
        self.correct = 0

    def display_result(self):
        # calculates the wrong count
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"

        # calcultaes the percentage of correct answers
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"

        # Shows a message box to display the result
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")

    # This method checks the Answer after we click on Next.
    def check_ans(self, q_no):
        if self.opt_selected.get() == answer[q_no]:
            # if the option is correct it return true
            return True

    def next_btn(self):
        if self.check_ans(self.q_no):
            # if the answer is correct it increments the correct by 1
            self.correct += 1
        self.q_no += 1

        # checks if the q_no size is equal to the data size
        if self.q_no == self.data_size:
            self.display_result()
            gui.destroy()
        else:
            for im in self.images:
                im.destroy()
            self.display_title()
            self.display_question()
            self.display_options()

    def buttons(self):
        next_button = Button(gui, text="Next", command=self.next_btn,
                             width=10, bg="blue", fg="white", font=("ariel", 16, "bold"))
        next_button.place(x=100, y=720)
        quit_button = Button(gui, text="Quit", command=gui.destroy,
                             width=5, bg="black", fg="white", font=("ariel", 16, " bold"))
        quit_button.place(x=1800, y=50)

    def display_options(self):
        self.opt_selected.set(0)
        for i, option in enumerate(options[self.q_no]):
            if type(option) == str:
                self.opts[i]['text'] = option
            else:
                label = Label(image=option)
                label.place(x=450 * i, y=150)
                self.images.append(label)
                self.opts[i]['text'] = i + 1


    # This method shows the current Question on the screen
    def display_question(self):
        currentQuestion = question[self.q_no]
        if type(currentQuestion) == str:
            # setting the Question properties
            q_no = Label(gui, text=f"Which one is {question[self.q_no]}", width=60,
                         font=('ariel', 16, 'bold'), anchor='w')
            q_no.place(x=70, y=100)
        else:
            q_no = Label(gui, text="What animal is this?", width=60,
                         font=('ariel', 16, 'bold'), anchor='w')
            q_no.place(x=70, y=100)
            label = Label(image=currentQuestion)
            label.place(x=150, y=150)
            self.images.append(label)


    # This method is used to Display Title
    def display_title(self):
        # The title to be shown
        title = Label(gui, text="QUIZ question %d / %d" % (self.q_no + 1, self.data_size),
                      width=120, bg="green", fg="white", font=("ariel", 20, "bold"))

        # place of the title
        title.place(x=0, y=2)

    # This method shows the radio buttons to select the Question
    # on the screen at the specified position. It also returns a
    # lsit of radio button which are later used to add the options to
    # them.
    def radio_buttons(self):
        q_list = []
        y_pos = 550
        while len(q_list) < 4:
            # setting the radio button properties
            radio_btn = Radiobutton(gui, text=" ", variable=self.opt_selected,
                                    value=len(q_list) + 1, font=("ariel", 14))
            q_list.append(radio_btn)
            radio_btn.place(x=100, y=y_pos)
            y_pos += 40

        # return the radio buttons
        return q_list


# Create a GUI Window
gui = Tk()

# set the size of the GUI Window
gui.geometry("1900x800")

quizName = "huntingLicenceAnimalRecognition"
gui.title(quizName)

generatedQuiz = readQuiz.createQuiz(20, 4)
question = generatedQuiz["questions"]
options = generatedQuiz["options"]
answer = generatedQuiz["answers"]
# # 0 - select name from selection of given photo
# # 1 - select photo of the given name
# question = ([
#     "Moose",
#     ImageTk.PhotoImage(Image.open("huntingLicenceAnimalRecognition/pix/mb_moose.bmp")),
#     "Reindeer",
#     "Roe deer"
#   ])
# options = ([
#     # [ImageTk.PhotoImage(Image.open("huntingLicenceAnimalRecognition/pix/mb_moose.bmp")),
#     #  ImageTk.PhotoImage(Image.open("huntingLicenceAnimalRecognition/pix/mb_r54zmg4h.bmp")),
#     #  ImageTk.PhotoImage(Image.open("huntingLicenceAnimalRecognition/pix/mb_moose.bmp")),
#     #  ImageTk.PhotoImage(Image.open("huntingLicenceAnimalRecognition/pix/mb_ucthl1v5.bmp"))
#     # ],
#     ["Moose",
#       "Reindeer",
#       "Roe deer",
#       "Goose"
#     ],
#     ["Goose",
#       "Moose",
#       "Reindeer",
#       "Roe deer"
#     ],
#     ["Goose",
#       "Reindeer",
#       "Roe deer",
#       "Moose"
#     ]])
# answer = ([
#     1,
#     1,
#     2,
#     4
#   ])

# create an object of the Quiz Class.
quiz = Quiz()
gui.mainloop()
