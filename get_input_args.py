#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#                                                                             
# PROGRAMMER: Ifesinachi Chukwuemeka
# DATE CREATED: 19/03/2021                        
# REVISED DATE: 
# PURPOSE: Create a function that retrieves the following 3 command line inputs 
#          from the user using the Argparse Python module. If the user fails to 
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
##
# Imports python modules
import argparse

def get_input_args():
    """
    Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
    This function returns these arguments as an ArgumentParser object.
    Parameters:
      None - simply using argparse module to create & store command line arguments
    Returns:
      parse_args() -data structure that stores the command line arguments object  
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('--dir', default='pet_images/', type=str, help='Enter path to the images folder "pet_images/"')
    parser.add_argument('--arch', default='vgg', type=str, help='Choose CNN model to use. "vgg"')
    parser.add_argument('--dogfile', default='dognames.txt', type=str, help='Enter name of text file containing list of dog names. "dognames.txt"')

    return parser.parse_args()
