from tkinter import *
import random
okno = Tk()
okno.geometry('1500x700+0+0')
koordinatkax=random.randint(-15,15)
koordinatkay=random.randint(-6,6)
holst = Canvas(okno, width=1500, height = 600, bg = "white")
holst.create_line(0,300,1500,300,fill="black",width=3,arrow=LAST)
holst.create_line(750,600,750,0,fill="black",width=3,arrow=LAST)
metka = Label(okno,font=20,text="Привет всем! Найди точку с координатами x = " + str(koordinatkax) + ",  y = " + str(koordinatkay))
metka.place(x = 0,y = 620)
metkaX = Label(holst,font=20,text="X")
metkaX.place(x = 1475,y =310)
metkaY = Label(holst,font=20,text="Y")
metkaY.place(x =760,y = 10)
#положительные метки Y
metka1Y = Label(holst,font=20,text="1")
metka1Y.place(x =725,y = 240)
#метка 0
metka0 = Label(holst,font=20,text="0")
metka0.place(x =725,y = 305)
#положительные метки X
metka1X = Label(holst,font=20,text="1")
metka1X.place(x =792,y = 308)
#отрицательные метки Y
metka1Y = Label(holst,font=20,text="-1")
metka1Y.place(x =725,y = 340)
#отрицательные метки X
metka1X = Label(holst,font=20,text="-1")
metka1X.place(x =692,y = 308)
for i in range(14):
    holst.create_line(0,50*i,1500,50*i,fill="black",width=1)
    holst.create_line(745,50*i,755,50*i,fill="black",width=3)
for i in range(30):
    holst.create_line(50*i,0,50*i,600,fill="black",width=1)
    holst.create_line(50*i,295,50*i,305,fill="black",width=3)
holst.place(x=0,y=0)
knopka = Button(okno)
knopka.place(x = 50,y = 650)
def gdelevyklik(event):
    xo = koordinatkax*50+750
    yo = 300-koordinatkay*50
    if int(((event.x-xo)**2+(event.y-yo)**2)**0.5) < 5:
        okno.title("Молодец! Левая кнопка мыши нажата" + str(event.x) + " " + str(event.y))
    else:
        okno.title("Не правильно! Левая кнопка мыши нажата" + str(event.x) + " " + str(event.y))
holst.bind('<Button-1>', gdelevyklik)

okno.mainloop()