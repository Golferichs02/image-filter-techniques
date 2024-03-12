""" apply_geometric_transformations.py
This scripts reads and applies geometric transformations
to an image which the user enters with the argparse command.

Authors: Emilio Arredondo Payán (628971) & Jorge Alberto Rosales de Golferichs (625544) 
Contacts: emilio.arredondop@udem.edu, jorge.rosalesd@udem.edu
Organisation: Universidad de Monterrey
First created on Tuesday 06 February 2024
"""

#Import standard libraries
import numpy as np 
import cv2 
  

#Function to load the previous input image 
def load_image(filename):
    img = cv2.imread(filename)
    if img is None:
        print(f"The following image:{filename} could not be found!")
        exit (-1)
    return img

#Function to rotate the image
def apply_rotation(img:cv2)->cv2:
    # get heigth and width of image, (we dont need de channel)
    height, width = img.shape[:2]
    # Get the centroid of the image
    centroid = (width / 2, height / 2)
    # Apply some angule to the RotationMatrix    
    rotation_matrix = cv2.getRotationMatrix2D(centroid, 45,1)
    # Apply the rotation to the image.
    image_rotated = cv2.warpAffine(img, rotation_matrix, (width, height))
    return image_rotated

#Function to translate the image
def apply_translation(img:cv2)->cv2:
    M = np.float32([[1,0,50],[0,1,0]]) #Aplicamos una martríz de traslación
    image_translated = cv2.warpAffine(img,M,(img.shape[1], img.shape[0])) #Aplicamos la matríz
    return image_translated #Retornamos la imágen


def apply_reflection (img:cv2)->cv2:
    img_reflected =cv2.flip(img,1)
    # Return reflected image
    return img_reflected

#Function to visualize the image
def visualise_image (img:cv2 , title:str)->None:
    cv2.imshow(title,img)
    return None

#Function to close all windows
def close_windows():
    cv2.waitKey(0) #Comando para que se cierren las ventanas hasta 
    cv2.destroyAllWindows()