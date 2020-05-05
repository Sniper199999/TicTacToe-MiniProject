from tkinter import BOTH, Frame, Label, Canvas, Button, Tk


class MainWindow(Frame):
    def __init__(self):
        super().__init__()
        self.pointer = 0
        self.count = 0
        self.win_x_counter = 0
        self.win_o_counter = 0
        self.draw_counter = 0
        self.win = False
        self.iterate = "X"
        self.x_list = []
        self.y_list = []
        self.record = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.ui()

    def ui(self):
        self.lbl_greet = Label(text="Mini-Project By Sniper199999")
        self.lbl_greet.pack(fill=BOTH)
        self.master.title("Tic Tac Toe")
        self.pack(fill=BOTH, expand=1)
        
        # create 2 Horizontal & Vertical lines
        self.canvas = Canvas(self)
        self.canvas.create_line(40, 50, 210, 50)
        self.canvas.create_line(40, 95, 210, 95)
        self.canvas.create_line(100, 0, 100, 146)
        self.canvas.create_line(150, 0, 150, 146)
        self.canvas.pack(fill=BOTH)
        
        # lbl_1 to lbl_9 are boxes
        self.lbl_1 = Label(text="   ", bg="white", width=5, height=2)
        self.lbl_1.place(x=55, y=32)
        self.lbl_1.bind("<ButtonRelease-1>", lambda event, box=0: self.mouseclk(box))
        self.lbl_2 = Label(text="   ", bg="white", width=5, height=2)
        self.lbl_2.place(x=105, y=32)
        self.lbl_2.bind("<ButtonRelease-1>", lambda event, box=1: self.mouseclk(box))
        self.lbl_3 = Label(text="   ", bg="white", width=5, height=2)
        self.lbl_3.place(x=155, y=32)
        self.lbl_3.bind("<ButtonRelease-1>", lambda event, box=2: self.mouseclk(box))
        self.lbl_4 = Label(text="   ", bg="white", width=5, height=2)
        self.lbl_4.place(x=55, y=76)
        self.lbl_4.bind("<ButtonRelease-1>", lambda event, box=3: self.mouseclk(box))
        self.lbl_5 = Label(text="   ", bg="white", width=5, height=2)
        self.lbl_5.place(x=105, y=76)
        self.lbl_5.bind("<ButtonRelease-1>", lambda event, box=4: self.mouseclk(box))
        self.lbl_6 = Label(text="   ", bg="white", width=5, height=2)
        self.lbl_6.place(x=155, y=76)
        self.lbl_6.bind("<ButtonRelease-1>", lambda event, box=5: self.mouseclk(box))
        self.lbl_7 = Label(text="   ", bg="white", width=5, height=2)
        self.lbl_7.place(x=55, y=121)
        self.lbl_7.bind("<ButtonRelease-1>", lambda event, box=6: self.mouseclk(box))
        self.lbl_8 = Label(text="   ", bg="white", width=5, height=2)
        self.lbl_8.place(x=105, y=121)
        self.lbl_8.bind("<ButtonRelease-1>", lambda event, box=7: self.mouseclk(box))
        self.lbl_9 = Label(text="   ", bg="white", width=5, height=2)
        self.lbl_9.place(x=155, y=121)
        self.lbl_9.bind("<ButtonRelease-1>", lambda event, box=8: self.mouseclk(box))
        
        self.lbl_Show = Label(text="Your Turn:- X", fg="Orange", height=2, font='Helvetica 18 bold')
        self.lbl_Show.place(x=20, y=190)
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
        self.B = Button(text="New Game", command=self.newgame, width=29, bg="#90ee90", fg="Green")
        self.B.place(x=20, y=180)
        self.lbl_list = [self.lbl_1, self.lbl_2, self.lbl_3, self.lbl_4, self.lbl_5, self.lbl_6, self.lbl_7, self.lbl_8,
                         self.lbl_9]

    def newgame(self):
        if self.iterate == "X":
            self.pointer = 1
            self.iterate = "O"
        else:
            self.pointer = 0
            self.iterate = "X"
        self.record = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.count = 0
        self.x_list = []
        self.y_list = []
        self.win = False
        for i in self.record:
            self.lbl_list[i].config(text="  ", bg="white", fg="red")
            self.lbl_Show.config(text="Your Turn:- " + self.iterate, fg="Orange")

    def mouseclk(self, box):
        combo = [[0, 4, 8], [2, 4, 6], [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8]]
        passed = False
        chance = None
        if self.pointer == 0:
            for i in self.record:
                if i == box:
                    self.lbl_list[box].config(text=" X ", fg="red")
                    self.lbl_Show.config(text="Your Turn:- O")
                    self.pointer = 1
                    self.record.remove(i)
                    self.count += 1
                    passed = True
                    chance = "X"
                    self.x_list.append(box)
                    break
        elif self.pointer == 1:
            for i in self.record:
                if i == box:
                    self.lbl_list[box].config(text=" O ", fg="blue")
                    self.lbl_Show.config(text="Your Turn:- X")
                    self.pointer = 0
                    self.record.remove(i)
                    self.count += 1
                    passed = True
                    chance = "O"
                    self.y_list.append(box)
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
                    self.lbl_Show.config(text=text + " Won!", fg="Green")
                    self.pointer = 2
                    for i in winner:
                        self.lbl_list[i].config(text=text, bg="green", fg="white")
                    if chance == "X":
                        self.win_x_counter += 1
                        self.lbl_win_x_no.config(text=str(self.win_x_counter) + " Times")
                    else:
                        self.win_o_counter += 1
                        self.lbl_win_o_no.config(text=str(self.win_o_counter) + " Times")
                    break
        if self.record == [] and self.win is False:
            if self.pointer <= 2:
                self.draw_counter += 1
                self.lbl_draw_no.config(text=str(self.draw_counter) + " Times")
                self.lbl_Show.config(text="Its a Draw!", fg="Brown")
            self.pointer = 3


def main():
    window = Tk()
    MainWindow()
    window.geometry("250x300")
    window.maxsize(250, 300)
    window.minsize(250, 300)
    window.mainloop()


if __name__ == '__main__':
    main()
