from tkinter import *
from PIL import Image, ImageTk
import sys

screen = Tk("Cadastro Pessoas")
screen.geometry("1080x720")

x_center_screen = 1080 / 2
y_center_screen = 720 / 2

def close_program():
    sys.exit()

btn_sair = Button(screen, text="Sair", command=close_program).place(x=x_center_screen,y=y_center_screen)

screen.mainloop()