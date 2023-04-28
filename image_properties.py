'''
Code for extracting object properties on images using Regionprops 
Main goal is to find flow patterns in vuggy porous media

-The loops to analyse each image case runs in parallel

Created on Fri Apr 28 16:59:41 2023
@author: Monique Dali 
'''

##########################

from skimage.io import imread, imshow
from skimage import filters, util
from skimage.filters import gaussian, threshold_otsu
#from skimage import measure
from skimage.segmentation import clear_border
from skimage.measure import label, regionprops,regionprops_table
from skimage.color import rgb2gray,rgba2rgb
import matplotlib.pyplot as plt
from skimage.morphology import closing, square
from skimage.transform import rotate

import pandas as pd

################# Files ######################
# Rock samples
sample = ["5","8"]
# tomographic slices
# initial image
s_init = 150
# number of images
s_tot = 1641
# tag of image segmentation
threshold = ["1","2","3","4"]

############### Images ########################
def image_props(ind_i,sample,threshold,s_init,dir_name,folder):
    ### Loops to define filenames
    s = s_init + ind_i
    if (s/1000) < 1:
   		sl = "0"+str(s)
    else:
        sl = str(s)
    for am in sample:
        for th in threshold:
            #image name
            input_file = "Images/am" + am + "_c" + th + "_final-" + sl
            
            # one .csv file per image
            output_file_name = "am" + am + "_c" + th + "_s-" + sl
            data_output = output_file_name + "_image-data.csv"
            # Y direction
            #data_output = dir_name + folder + output_file_name + "_Y_image-data.csv"
            
            exists = os.path.isfile(input_file + ".tif")
            if exists:

                ### Image ###
                # filename
                z = input_file + ".tif"
                # Load image
                image = imread(z)
                
                '''
                # if image is rgb
          
                grayscale_crop = rgb2gray(rgba2rgb(image))
                thresh = threshold_otsu(grayscale_crop)
                bw2 = closing(grayscale_crop > thresh)
                '''
                
                # the input is a binary image
                bw2 = image

                ## Build table with image properties using Regionprops 
                label_image = label(bw2)
                
                # Selected measurements
                info_table = pd.DataFrame(
                    regionprops_table(
                        label_image,
                        properties=['label','area','bbox','bbox_area','centroid','convex_area','eccentricity','equivalent_diameter','euler_number','extent','filled_area','inertia_tensor','inertia_tensor_eigvals','local_centroid','major_axis_length','minor_axis_length','moments','moments_central','moments_hu','moments_normalized','orientation','perimeter','solidity'],
                    )
                ).set_index('label')

                # Save properties of each object on image
                info_table.to_csv(data_output, sep=',')
            else:
                print("Could not find file")
                pass
    

### Multiprocessing

from joblib import Parallel, delayed, parallel_backend
import os

# Loop
with parallel_backend('multiprocessing', n_jobs=8):
    Parallel()(delayed(image_props)(ind_i,sample,threshold,s_init,dir_name,folder) for ind_i in range(s_tot))
