# recolor_black_pixels

This project uses OpenCV for basic computer vision, NumPy to handle images as numpy arrays, and Tkinter for the GUI.

The GUI presents 4 text input boxes.
The first and largest of those boxes is where the user inputs an image url.
The following 3 boxes represent BGR (color) values. (note: values from 0-255 must be entered in that specific order)

When the enter button in the GUI is clicked an altered version of your input image is returned.
Press any key to close that image.
Code terminates when GUI window is closed.

Example:

Box1: https://artprojectsforkids.org/wp-content/uploads/2020/05/Penguin-791x1024.jpg

Box2: 255

Box3: 255

Box4: 255

Click: "Enter"

These inputs take the given image of a penguin and convert the black pixels to white
