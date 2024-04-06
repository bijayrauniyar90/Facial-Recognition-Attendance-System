from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        # Top img
        img_top = Image.open(
            r"C:\Users\KIIT01\Face Recognition System\images\contact.jpg")
        img_top = img_top.resize((1550, 840), Image.BILINEAR)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl_top = Label(self.root, image=self.photoimg_top)
        f_lbl_top.place(x=0, y=0, width=1550, height=840)

        # # Title = Help Team
        # # bg img
        # img_bg = Image.open(
        #     r"C:\Users\KIIT01\Face Recognition System\images\bg.jpg")
        # img_bg = img_bg.resize((1530, 710), Image.BILINEAR)
        # self.photoimg_bg = ImageTk.PhotoImage(img_bg)

        # bg_img = Label(self.root, image=self.photoimg_bg)
        # bg_img.place(x=0, y=155, width=1530, height=810)

        # # title_lbl = Label(bg_img, text="Help Desk", font=(
        # #     "20th Century Font", 30, "bold"), bg="white", fg="darkgreen")
        # # title_lbl.place(x=0, y=0, width=1530, height=55)

        # # Bottom img
        # img_bottom = Image.open(
        #     r"C:\Users\KIIT01\Face Recognition System\images\botgreen.jpg")
        # img_bottom = img_bottom.resize((1550, 200), Image.BILINEAR)
        # self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        # f_lbl_bottom = Label(self.root, image=self.photoimg_bottom)
        # f_lbl_bottom.place(x=0, y=732, width=1550, height=100)


if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
