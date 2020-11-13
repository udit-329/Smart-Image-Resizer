'''
Creator: Udit Kapoor
Date   : 12 November 2020

This program allows you to browse for pictures on your device and converts
those images to a specific square size. Rectangular images have transparent
padding added to make them square.

Useful for when you need to reuse old pictures and make them a standard size 
and format for things like catalogues and ecommerce websites.

Supported import file types: png, jpg
Supported export file type : png
'''
from tkinter import *
from tkinter import filedialog
import os
from PIL import Image, ImageTk

root = Tk()
root.title("Smart Image Resizer")

#function to open a file dialog and return a list of paths to selected images
def open_file():
    root.filename = filedialog.askopenfilenames(initialdir = "C:/Users",
                                                title = "Select a file",
                                                filetypes = (("images","*.png *.jpg *.jpeg"), ("png files", "*.png"), ("jpg files", "*.jpg *.jpeg")))
    return root.filename

#functions takes an image and the filepath and saves it on the machine
def save_image(new_im, file_path):
    dir_name = os.path.dirname(file_path)
    file_name = os.path.basename(file_path)

    #change file extension
    file_name = os.path.splitext(file_name)[0] + '.png'
    #set current directory
    os.chdir(dir_name)
    #folder 
    if not os.path.exists('new images'):
            os.makedirs("new images")
    
    os.chdir("new images")
    new_im = new_im.save(file_name)

#Functions takes in the filepath to an image, resizes it and saves a copy in a new folder in the path
def resize(file_path, desired_size):
    im = Image.open(file_path)

    old_size = im.size
    #Set the ratio as the desired size divided by the larger of input length or width
    ratio = float(desired_size)/max(old_size)
    new_size = tuple([int(x*ratio) for x in old_size])

    im = im.resize(new_size, Image.ANTIALIAS)

    #make new square blank image
    new_im = Image.new("RGBA", (desired_size, desired_size))
    #Paste the image on blank and center it
    new_im.paste(im, ((desired_size-new_size[0])//2,(desired_size-new_size[1])//2))

    #run save_image
    save_image(new_im, file_path)
    
    
size_input = Entry(root, width = 40)

#function starts when the button is clicked in dialog box
def start():
    paths = open_file()
    for p in paths:

        text_display = "Saved " + str(len(paths)) + " images!"
        label_infomation = Label(root, text = text_display)
        label_infomation.grid(row = 3, column = 0)
        if len(size_input.get()) == 0:
            resize(p, 600)
        else:
            resize(p, int(size_input.get()))

program_label = Label(root, text = "Enter the size, default: 600px")
select_button = Button(root, text = "select images", command = start)

program_label.grid(row = 0, column = 0)
size_input.grid(row = 1, column = 0)
select_button.grid(row = 3, column = 2)


root.mainloop()
