import cv2
import numpy as np
import tkinter as tk
import urllib
import urllib.request


# Deprecated code not used
# Exists to show learning path as the code was being developed
def change_black_slow(img, threshold, color):
    for i in range(0, len(img)):
        for j in range(0, len(img[i])):
            if img[i][j][0] < threshold and img[i][j][1] < threshold or img[i][j][2] < threshold:
                img[i][j] = color
    cv2.imshow('image', img)  # shows image in a new window
    cv2.waitKey(10000)  # waits till key is pressed
    cv2.destroyAllWindows()  # closes opened windows


# converts black pixels to a color set by user
def change_black(img, threshold, color):
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mask = np.where(grayscale < threshold)
    img[mask] = (color[0], color[1], color[2])

    cv2.imshow('image', img)
    cv2.waitKey(0)  # press any key to close the image
    cv2.destroyAllWindows()


# decodes image from url before calling pixel conversion function
def image():
    inp = inputtxt.get(1.0, "end-1c")
    b_inp = blue.get(1.0, "end-1c")
    g_inp = green.get(1.0, "end-1c")
    r_inp = red.get(1.0, "end-1c")

    url_response = urllib.request.urlopen(inp)
    img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
    img = cv2.imdecode(img_array, -1)

    change_black(img, 50, [int(b_inp), int(g_inp), int(r_inp)])


# tkinter window
frame = tk.Tk()
frame.title("Black Pixel Conversion - Kanishk Chinna")
frame.geometry('600x200')

# tkinter textboxes
inputtxt = tk.Text(frame, height=5, width=50)
inputtxt.pack()

blue = tk.Text(frame, height=2, width=10)
blue.pack()

green = tk.Text(frame, height=2, width=10)
green.pack()

red = tk.Text(frame, height=2, width=10)
red.pack()

# enter button
printButton = tk.Button(frame, text="Enter",
                        command=image)
printButton.pack()

# tkinter label
lbl = tk.Label(frame, text="")
lbl.pack()
frame.mainloop()
