import tkinter as tk
import random as rd
import csv

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.master.geometry("380x200")
        self.master.title("古典暗記ソフト")

        self.canvas = tk.Canvas(self.master, bg = "green", width = 50, height = 50)
        self.canvas.place(x = 30,y = 135)

        self.WordInput()
        self.SetVar()
        self.widget()


        self.master.bind("<Return>", self.EnterJudge)

    def SetVar(self):
        self.judgeNum = -1
        self.num = rd.randint(0,len(self.wordlist) - 1)


    def WordInput(self):
        f = open("word.csv","r",encoding = "utf-8-sig")

        self.wordlist = list(csv.reader(f))

        f.close()


    #部品の配置↓

    def widget(self):

        self.txt1 = tk.Entry(self.master, width = 33)
        self.txt1.place(x = 50, y = 30)

        self.txt1.insert(0,self.wordlist[self.num][0])

        self.txt2 = tk.Entry(self.master, width = 33)
        self.txt2.place(x = 50, y = 90)

        self.BtnJudge = tk.Button(self.master, text = "判定", command = self.ClickJudge, width = 10)
        self.BtnJudge.place(x = 110, y = 148)

        self.BtnNext = tk.Button(self.master, text = "次の単語", command = self.Next, width = 10)
        self.BtnNext.place(x = 215, y = 148)

        self.select4()#4択


    #部品の配置↑


    #4択の表示↓
    def select4(self):

        rdNum = rd.randint(0,3)
        lbl_x = 280
        lbl_y = 15

        self.Rdlist()

        for i in range(4):

            if i == 0:
                if i == rdNum:
                    self.lbl1 = tk.Label(self.master, text = str(i+1) + " . " + self.wordlist[self.num][1])
                    self.lbl1.place(x = lbl_x, y = lbl_y + i * 30)
                else:
                    self.lbl1 = tk.Label(self.master, text = str(i+1) + " . " + self.wordlist[self.rdlist[i]][1])
                    self.lbl1.place(x = lbl_x, y = lbl_y + i * 30)


            if i == 1:
                if i == rdNum:
                    self.lbl2 = tk.Label(self.master, text = str(i+1) + " . " + self.wordlist[self.num][1])
                    self.lbl2.place(x = lbl_x, y = lbl_y + i * 30)
                else:
                    self.lbl2 = tk.Label(self.master, text = str(i+1) + " . " + self.wordlist[self.rdlist[i]][1])
                    self.lbl2.place(x = lbl_x, y = lbl_y + i * 30)


            if i == 2:
                if i == rdNum:
                    self.lbl3 = tk.Label(self.master, text = str(i+1) + " . " + self.wordlist[self.num][1])
                    self.lbl3.place(x = lbl_x, y = lbl_y + i * 30)
                else:
                    self.lbl3 = tk.Label(self.master, text = str(i+1) + " . " + self.wordlist[self.rdlist[i]][1])
                    self.lbl3.place(x = lbl_x, y = lbl_y + i * 30)


            if i == 3:
                if i == rdNum:
                    self.lbl4 = tk.Label(self.master, text = str(i+1) + " . " + self.wordlist[self.num][1])
                    self.lbl4.place(x = lbl_x, y = lbl_y + i * 30)
                else:
                    self.lbl4 = tk.Label(self.master, text = str(i+1) + " . " + self.wordlist[self.rdlist[i]][1])
                    self.lbl4.place(x = lbl_x, y = lbl_y + i * 30)


    def Rdlist(self):
        self.rdlist = list(range(len(self.wordlist)))
        rd.shuffle(self.rdlist)
        self.rdlist.remove(self.wordlist.index(self.wordlist[self.num]))

    def select4_destroy(self):
        self.lbl1.destroy()
        self.lbl2.destroy()
        self.lbl3.destroy()
        self.lbl4.destroy()

    #4択の表示↑


    #判定↓

    def Judge(self):
        if self.txt2.get() == self.wordlist[self.num][1]:
            self.marupro()
        else:
            self.batsupro()

    def ClickJudge(self):
        self.Judge()

    def EnterJudge(self, event):
        self.Judge()


    def marupro(self):
        self.canvas.delete("batsu1")
        self.canvas.delete("batsu2")
        self.judgeNum = 1
        #print("正解")
        self.canvas.create_oval(10,10,43,43,outline = "red", width = 5, tag = "maru")

    def batsupro(self):
        #print("不正解")
        self.canvas.create_line(10,10,43,43,fill = "black", width = 5, tag = "batsu1")
        self.canvas.create_line(10,43,43,10,fill = "black", width = 5, tag = "batsu2")
        self.txt2.delete(0,tk.END)

    #判定↑


    def Next(self):
        if self.judgeNum == 1:
            self.canvas.delete("maru")

            self.num = rd.randint(1,len(self.wordlist) - 1)

            self.txt1.delete(0,tk.END)
            self.txt2.delete(0,tk.END)
            self.txt1.insert(0,self.wordlist[self.num][0])

            self.select4_destroy()
            self.select4()

            self.judgeNum = -1


def main():
    win = tk.Tk()
    app = Application(master = win)
    app.mainloop()


if __name__ == "__main__":

    main()
