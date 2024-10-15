from tkinter import *
from PIL import Image, ImageTk

class Display:
    def __init__(self, w, h, im_in, im_out):
        self.canvas = Canvas(win, width=w, height=h)
        self.button_in = Button(win, text="Show In", command=self.but_in_press)
        self.button_out = Button(win, text="Show Out", command=self.but_out_press)
        self.im_in = im_in
        self.im_out = im_out
        self.show = "in"
        
    def show_image(self):
        if self.show == "in":
            self.img = ImageTk.PhotoImage(self.im_in)
        else:
            self.img = ImageTk.PhotoImage(self.im_out)
        self.canvas.delete("picture")
        self.canvas.create_image(0, 0, anchor=NW, image=self.img, tag="picture")
        self.canvas.place(x=0, y=0)
        self.button_in.place(x=1000, y=10)
        self.button_out.place(x=1100, y=10)

    def but_out_press(self):
        self.show = "out"
        self.show_image()

    def but_in_press(self):
        self.show= "in"
        self.show_image()

win = Tk()

im_in = Image.open("Veil.png")
im_out = im_in.copy()

print(im_in.format, im_in.size, im_in.mode)
#print(im.getpixel([227, 248]))
width_in = im_in.size[0]
height_in = im_in.size[1]

win.geometry(str(width_in) + "x" + str(height_in))

canvas = Canvas(win, width=width_in, height=height_in)

for y in range(height_in):
    for x in range(width_in):
        pxl = im_in.getpixel([x, y])
        if pxl[0] + pxl[1] + pxl[2] < 100:
            im_out.putpixel( (x,y), (5, 5, 5, 255))

disp = Display(width_in , height_in, im_in, im_out)
disp.show_image()

#im_out.save("Cliff.png")

win.mainloop()