import numpy as np
import cv2 
import sys
import argparse
import cvlib as cl

def parse_user_data()->argparse.Namespace:    

    # Create ArgumentParser object    
    parser = argparse.ArgumentParser(description='Apply image '
                                    'filtering and geometric transformation')

    # Add arguments    
    parser.add_argument('-i','--input_image',
                                    type=str, 
                                    required=True,
                                    help='Input image to be filtered')
                                
    parser.add_argument('-f','--filter_name',
                                    type=str,
                                    required=True,
                                    help="Filter name used as Kernel"
                                    "[average, gaussian, median,none]")
    # Add arguments    
    parser.add_argument('-k','--input_kernel',
                                    type=int, 
                                    required=False,
                                    help='Input kernel size')
                                
    parser.add_argument('-gt','--geometric_transformation',
                                    type=str,
                                    required=True,
                                    help="Geometric transformation required"
                                    "[none, traslation, rotation, flip]")
    args = parser.parse_args()

    if args.filter_name.lower() != "none" and args.input_kernel is not None and args.input_kernel % 2 == 0:
        parser.error("Kernel size must be an odd number.")
    
    if args.filter_name.lower() != "none" and args.input_kernel is None:
        parser.error("Kernel size must be an odd number, not a None value.")

    # Return parsed data entered by the user    
    return args

def Filter(img:cv2,filter:str,kernel:int)->cv2:
    if filter.lower() == "average":
        img_fil = average_fil(img, kernel)
    elif filter.lower() == "gaussian":
        img_fil = gaussian_fil(img, kernel)
    elif filter.lower() == "median":
        img_fil = median_fil(img, kernel)
    elif filter.lower() == "none":
        img_fil = img
    else:
        raise ValueError("Unknown filter name, we just have"+ 
                         "average, gaussian, median")    
    return img_fil

def Geometric_transformation(img:cv2,geotransform:str)->cv2:
    if geotransform.lower() == "none":
        img_fil = img
    elif geotransform.lower() == "traslation":
        img_fil = cl.apply_translation(img)
    elif geotransform.lower() == "rotation":
        img_fil = cl.apply_rotation(img)
    elif geotransform.lower() == "flip":
        img_fil = cl.apply_reflection(img)
    else:
        raise ValueError("Unknown tranformation name, we just have"
                         +"none, traslation, rotation, flip")  
    return img_fil

def average_fil(img:cv2,kernel:int)->cv2:
    average_blur = cv2.blur(img, (kernel, kernel))
    return average_blur


def gaussian_fil(img:cv2,kernel:int)->cv2:
    gaussian_blur = cv2.GaussianBlur(img, (kernel, kernel), 0)
    return gaussian_blur

def median_fil(img:cv2,kernel:int)->cv2:
    median_blur = cv2.medianBlur(img, kernel)
    return median_blur

def run_pipeline(): 
    args = parse_user_data()     
    img = cl.load_image(args.input_image)
    img_filtro=Filter(img,args.filter_name,args.input_kernel)
    img_gt=Geometric_transformation(img_filtro,args.geometric_transformation)
    cl.visualise_image(img,"original")
    cl.visualise_image(img_gt,"Filter "+args.filter_name+" and geometric transformation "+args.geometric_transformation)
    cl.close_windows()

if __name__ == '__main__':   
    # Run pipeline    
    run_pipeline()