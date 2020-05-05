from tkinter import BOTH, Frame, Label, Canvas, Button, Tk

class MainWindow(Frame):
    def __init__(self):
        super().__init__()
        self.pointer = 0
        self.bap = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.count = 0
        self.x_list = []
        self.y_list = []
        self.win_x_counter = 0
        self.win_o_counter = 0
        self.draw_counter = 0
        self.win = False
        self.UI()

    def UI(self):
        self.lbl_greet = Label(text="Mini-Project By Shubham")
        self.lbl_greet.pack(fill=BOTH)
        self.master.title("Tic Tac Toe")
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self)
        self.canvas.create_line(40, 50, 210, 50)
        self.canvas.create_line(40, 95, 210, 95)
        self.canvas.create_line(100, 0, 100, 150)
        self.canvas.create_line(150, 0, 150, 150)
        self.canvas.pack(fill=BOTH)
        self.lbl_1 = Label(text="   ", bg="white", width=5, height=2)
        self.lbl_1.place(x=55, y=32)
        self.lbl_1.bind("<ButtonRelease-1>", lambda event, ku=0: self.pressed(ku))
        self.lbl_2 = Label(text="   ", bg="white", width=5, height=2)
        self.lbl_2.place(x=105, y=32)
        self.lbl_2.bind("<ButtonRelease-1>", lambda event, ku=1: self.pressed(ku))
        self.lbl_3 = Label(text="   ", bg="white", width=5, height=2)
        self.lbl_3.place(x=155, y=32)
        self.lbl_3.bind("<ButtonRelease-1>", lambda event, ku=2: self.pressed(ku))
        self.lbl_4 = Label(text="   ", bg="white", width=5, height=2)
        self.lbl_4.place(x=55, y=76)
        self.lbl_4.bind("<ButtonRelease-1>", lambda event, ku=3: self.pressed(ku))
        self.lbl_5 = Label(text="   ", bg="white", width=5, height=2)
        self.lbl_5.place(x=105, y=76)
        self.lbl_5.bind("<ButtonRelease-1>", lambda event, ku=4: self.pressed(ku))
        self.lbl_6 = Label(text="   ", bg="white", width=5, height=2)
        self.lbl_6.place(x=155, y=76)
        self.lbl_6.bind("<ButtonRelease-1>", lambda event, ku=5: self.pressed(ku))
        self.lbl_7 = Label(text="   ", bg="white", width=5, height=2)
        self.lbl_7.place(x=55, y=121)
        self.lbl_7.bind("<ButtonRelease-1>", lambda event, ku=6: self.pressed(ku))
        self.lbl_8 = Label(text="   ", bg="white", width=5, height=2)
        self.lbl_8.place(x=105, y=121)
        self.lbl_8.bind("<ButtonRelease-1>", lambda event, ku=7: self.pressed(ku))
        self.lbl_9 = Label(text="   ", bg="white", width=5, height=2)
        self.lbl_9.place(x=155, y=121)
        self.lbl_9.bind("<ButtonRelease-1>", lambda event, ku=8: self.pressed(ku))
        self.labelShow1 = Label(text="Your Turn:- X", fg="Orange", height=2, font='Helvetica 18 bold')
        self.labelShow1.place(x=20, y=190)
        self.lbl_win_x = Label(text="X Won :-", fg="red")
        self.lbl_win_x.place(x=20, y=235)
        self.lbl_win_o = Label(text="O Won :-", fg="blue")
        self.lbl_win_o.place(x=20, y=255)
        self.lbl_draw = Label(text="Draw :-", fg="brown")
        self.lbl_draw.place(x=30, y=275)
        self.lbl_win_x_no = Label(text="0 Times")
        self.lbl_win_x_no.place(x=70, y=235)
        self.lbl_win_o_no = Label(text="0 Times")
        self.lbl_win_o_no.place(x=70, y=255)
        self.lbl_draw_no = Label(text="0 Times")
        self.lbl_draw_no.place(x=70, y=275)
        self.B = Button(text="New Game", command=self.new, width=29, bg="#90ee90", fg="Green")
        self.B.place(x=20, y=180)

    def new(self):
        self.pointer = 0
        self.bap = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.count = 0
        self.x_list = []
        self.y_list = []
        self.win = False
        lbl_list = [self.lbl_1, self.lbl_2, self.lbl_3, self.lbl_4, self.lbl_5, self.lbl_6, self.lbl_7, self.lbl_8,
                    self.lbl_9]
        for i in self.bap:
            lbl_list[i].config(text="  ", bg="white", fg="red", width=5, height=2)
            self.labelShow1.config(text="Your Turn:- X", fg="Orange")

    def pressed(self, ku):
        lbl_list = [self.lbl_1, self.lbl_2, self.lbl_3, self.lbl_4, self.lbl_5, self.lbl_6, self.lbl_7, self.lbl_8,
                    self.lbl_9]
        combo = [[0, 4, 8], [2, 4, 6], [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8]]
        passed = False
        chance = None
        if self.pointer == 0:
            for i in self.bap:
                if i == ku:
                    lbl_list[ku].config(text=" X ", fg="red")
                    self.labelShow1.config(text="Your Turn:- O")
                    self.pointer = 1
                    self.bap.remove(i)
                    self.count += 1
                    passed = True
                    chance = "X"
                    self.x_list.append(ku)
                    break
        elif self.pointer == 1:
            for i in self.bap:
                if i == ku:
                    lbl_list[ku].config(text=" O ", fg="blue")
                    self.labelShow1.config(text="Your Turn:- X")
                    self.pointer = 0
                    self.bap.remove(i)
                    self.count += 1
                    passed = True
                    chance = "O"
                    self.y_list.append(ku)
                    break
        if passed is True and self.count >= 5:
            for winner in combo:
                if chance == "X":
                    x_y_list = self.x_list
                    text = " X "
                else:
                    x_y_list = self.y_list
                    text = " O "
                match = set(winner).intersection(x_y_list)
                won = bool(set(winner).difference(match))
                print(match, won)
                if won is False:
                    self.win = True
                    self.labelShow1.config(text=text + " Won!", fg="Green")
                    self.pointer = 2
                    for i in winner:
                        lbl_list[i].config(text=text, bg="green", fg="white", width=5, height=2)
                    if chance == "X":
                        self.win_x_counter += 1
                        self.lbl_win_x_no.config(text=str(self.win_x_counter) + " Times")
                    else:
                        self.win_o_counter += 1
                        self.lbl_win_o_no.config(text=str(self.win_o_counter) + " Times")
                    break
        if self.bap == [] and self.win is False:
            if self.pointer <= 2:
                self.draw_counter += 1
                self.lbl_draw_no.config(text=str(self.draw_counter) + " Times")
                self.labelShow1.config(text="Its a Draw!", fg="Brown")
            self.pointer = 3


def main():
    window = Tk()
    show = MainWindow()
    window.geometry("250x300")
    window.maxsize(250, 300)
    window.minsize(250, 300)
    window.mainloop()


if __name__ == '__main__':
    main()
