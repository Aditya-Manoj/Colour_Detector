# ADITYA MANOJ S - Computer Vision & IoT Intern at The Sparks Foundation
# COLOR DETECTION USING PYTHON 
# Detecting the Name of the Closest Defined color to the color of Clicked Pixel from the Image

import cv2
import numpy as np
import webcolors

# Function to find the Closest Color for the passed RGB Value
def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():  # All the Defined Color Names
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        # Euclidian Distance Formula for finding the Closest Colors in the List
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]  # Returning the Closest Color

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)  # Checking if the RGB Value is exactly of a predefined color
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name


def mouseRGB(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:  # Checks mouse left button down condition
        global image
        image = mainimg.copy()
        colorsB = str(image[y,x,0]).zfill(3)
        colorsG = str(image[y,x,1]).zfill(3)
        colorsR = str(image[y,x,2]).zfill(3)
        colors = image[y,x]
        # print("Red: ",colorsR)
        # print("Green: ",colorsG)
        # print("Blue: ",colorsB)
        # print("BRG Format: ",colors)
        # print("Coordinates of pixel: X: ",x,"Y: ",y)

        text = "R: {} G: {} B: {}".format(colorsR, colorsG, colorsB)
        org = (30, 30)
        font = cv2.FONT_HERSHEY_PLAIN
        fontScale = 2
        color = (255, 0, 0)
        thickness = 2

        requested_colour = (int(colorsR), int(colorsG), int(colorsB))
        actual_name, closest_name = get_colour_name(requested_colour)
        # print(actual_name)
        cv2.circle(image,(x,y),10,(255,0,0),1)  # Circling the Clicked pixel
        # RGB Value Rectangle
        cv2.rectangle(image, (25, 5), (400, 35), (int(colorsB), int(colorsG), int(colorsR)), -1)
        # Color Name backdrop Rectangle - Thickness(-1) for Color Fill
        cv2.rectangle(image, (25, image.shape[0] - 5), (400, image.shape[0] - 35), (int(colorsB), int(colorsG), int(colorsR)), -1)
        cv2.putText(image, text, org, font, 
                   fontScale, (255 - int(colorsB), 255 - int(colorsG), 255 - int(colorsR)), thickness, cv2.LINE_AA)
        cv2.putText(image, closest_name, (30, image.shape[0] - 10), font, 
                   fontScale, (255 - int(colorsB), 255 - int(colorsG), 255 - int(colorsR)), thickness, cv2.LINE_AA)


# Read an image, a window and bind the function to window
mainimg = image = cv2.imread("umbrella.jpg")  # Mainimg is the Backup copy of the Actual Image
cv2.namedWindow('mouseRGB')
cv2.setMouseCallback('mouseRGB',mouseRGB)

#Do until esc pressed
while(1):
    cv2.imshow('mouseRGB',image)
    if cv2.waitKey(20) & 0xFF == 27:
        break
#if esc pressed, finish.
cv2.destroyAllWindows()