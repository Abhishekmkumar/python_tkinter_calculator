from tkinter import *
import pygame

pygame.mixer.init()

#V 2.0.0.0

root = Tk()
root.title("Calculator")

sound = pygame.mixer.Sound('click sound.wav')
error = pygame.mixer.Sound('error.wav')
correct = pygame.mixer.Sound('correct.wav')
back_clear = pygame.mixer.Sound('back.mp3')

def play_click_sound():
    sound.play()
def play_error_sound():
    error.play()
def play_correct_sound():
    correct.play()
def play_back_clear_sound():
    back_clear.play()

e = Entry(root, width=27, borderwidth=5, font="Arial 20")
e.grid(row=0, column=0, columnspan=5, padx=10, pady=20)

def out(value):
    e.insert(END, value)
def equal():
    try:
        c_get=e.get()
        ans = eval(c_get)
        e.delete(0, END)
        e.insert(0,str(ans))
        play_correct_sound()
    except:
        e.delete(0, END)
        e.insert(0, "Error")
        play_error_sound()
def clear():
    e.delete(0, END)
    play_back_clear_sound()
def back():
    c_text=e.get()
    e.delete(0, END)
    e.insert(0, c_text[:-1])
    play_back_clear_sound()
def button_click(value):
    out(value)
    play_click_sound()

myB1 = Button(root, text="1", width=10, height=3, borderwidth=5, command=lambda: button_click("1"))
myB1.grid(row=1, column=0)
myB2 = Button(root, text="2", width=10, height=3, borderwidth=5, command=lambda: button_click("2"))
myB2.grid(row=1, column=1)
myB3 = Button(root, text="3", width=10, height=3, borderwidth=5, command=lambda: button_click("3"))
myB3.grid(row=1, column=2)
myB4 = Button(root, text="+", width=10, height=3, borderwidth=5, command=lambda: button_click("+"))
myB4.grid(row=1, column=3)
myB5 = Button(root, text="/", width=10, height=3, borderwidth=5, command=lambda: button_click("/"))
myB5.grid(row=1, column=4)

myB6 = Button(root, text="4", width=10, height=3, borderwidth=5, command=lambda: button_click("4"))
myB6.grid(row=2, column=0)
myB7 = Button(root, text="5", width=10, height=3, borderwidth=5, command=lambda: button_click("5"))
myB7.grid(row=2, column=1)
myB8 = Button(root, text="6", width=10, height=3, borderwidth=5, command=lambda: button_click("6"))
myB8.grid(row=2, column=2)
myB9 = Button(root, text="-", width=10, height=3, borderwidth=5, command=lambda: button_click("-"))
myB9.grid(row=2, column=3)
myB10 = Button(root, text="%", width=10, height=3, borderwidth=5, command=lambda: button_click("%"))
myB10.grid(row=2, column=4)

myB11 = Button(root, text="7", width=10, height=3, borderwidth=5, command=lambda: button_click("7"))
myB11.grid(row=3, column=0)
myB12 = Button(root, text="8", width=10, height=3, borderwidth=5, command=lambda: button_click("8"))
myB12.grid(row=3, column=1)
myB13 = Button(root, text="9", width=10, height=3, borderwidth=5, command=lambda: button_click("9"))
myB13.grid(row=3, column=2)
myB14 = Button(root, text="*", width=10, height=3, borderwidth=5, command=lambda: button_click("*"))
myB14.grid(row=3, column=3)
myB15 = Button(root, text="**", width=10, height=3, borderwidth=5, command=lambda: button_click("**"))
myB15.grid(row=3, column=4)

myB16 = Button(root, text="0", width=10, height=3, borderwidth=5, command=lambda: button_click("0"))
myB16.grid(row=4, column=0)
myB17 = Button(root, text="<-", width=23, height=3, borderwidth=5, command=back)
myB17.grid(row=4, column=1, columnspan=2)
myB18 = Button(root, text=".", width=10, height=3, borderwidth=5, command=lambda: button_click("."))
myB18.grid(row=4, column=3)
myB19 = Button(root, text="//", width=10, height=3, borderwidth=5, command=lambda: button_click("//"))
myB19.grid(row=4, column=4)
myB20 = Button(root, text="CLEAR", width=23, height=3, borderwidth=5, command=clear)
myB20.grid(row=5, column=3, columnspan=2)

myB21 = Button(root, text="EQUAL", width=35, height=3, borderwidth=5, command=equal)
myB21.grid(row=5, column=0, columnspan=3)

root.mainloop()
