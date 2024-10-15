from tkinter import *
from PIL import Image, ImageTk
import numpy as np

class Display:
    def __init__(self, w, h, data):
        self.canvas = Canvas(win, width=w, height=h)
        self.w = w
        self.h = h
        self.button_in = Button(win, text="Show In", command=self.but_in_press)
        self.button_out = Button(win, text="Show Out", command=self.but_out_press)
        self.threshold_slide = Scale(win, from_=0, to=255, label="Threshold", command=self.thresh_update, orient=HORIZONTAL)
        self.threshold_slide.set(100)
        self.grey_slide = Scale(win, from_=0, to=255, label="Grey level", command=self.grey_update, orient=HORIZONTAL)
        self.grey_slide.set(5)
        self.im_in = data
        self.im_out = np.copy(data)
        self.show = "in"
        
    def show_image(self):
        if self.show == "in":
            self.img = ImageTk.PhotoImage(Image.fromarray(self.im_in, 'RGBA'))
        else:
            self.img = ImageTk.PhotoImage(Image.fromarray(self.im_out, 'RGBA'))
        self.canvas.delete("picture")
        self.canvas.create_image(0, 0, anchor=NW, image=self.img, tag="picture")
        self.canvas.place(x=0, y=0)
        self.button_in.place(x=1000, y=10)
        self.button_out.place(x=1100, y=10)
        self.threshold_slide.place(x=10, y=10)
        self.grey_slide.place(x=500, y=10)

    def but_out_press(self):
        self.show = "out"
        self.show_image()

    def but_in_press(self):
        self.show= "in"
        self.show_image()

    def get_threshold(self):
        return self.threshold_slide.get()

    def get_grey(self):
        return self.grey_slide.get()

    def thresh_update(self, event):
        print(self.threshold_slide.get())
        self.proc_img()

    def grey_update(self, event):
        print(self.grey_slide.get())
        self.proc_img()

    def proc_img(self):
        grey = self.grey_slide.get()
        for y in range(self.h - 1):
            for x in range(self.w - 1):
                pxl = self.im_in[x, y]
                if pxl[0] + pxl[1] + pxl[2] < self.threshold_slide.get():
                    self.im_out[x,y] = (grey, grey, grey, 255)

win = Tk()

im_in = Image.open("Veil.png")
#im_out = im_in.copy()

data = np.asarray(im_in)
print(data.shape)
print(data[100, 100])

width_in = im_in.size[0]
height_in = im_in.size[1]

win.geometry(str(width_in) + "x" + str(height_in))

canvas = Canvas(win, width=width_in, height=height_in)

#for y in range(height_in):
#    for x in range(width_in):
#        pxl = im_in.getpixel([x, y])
#        if pxl[0] + pxl[1] + pxl[2] < threshold:
#            im_out.putpixel( (x,y), (grey_lvl, grey_lvl, grey_lvl, 255))

disp = Display(width_in , height_in, data)
disp.show_image()

win.mainloop()