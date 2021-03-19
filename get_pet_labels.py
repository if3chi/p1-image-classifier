#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Ifesinachi Chukwuemeka
# DATE CREATED: 19/03/2021             
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

def get_pet_labels(image_dir):
	"""
    Parameters:
    image_dir - The (full) path to the folder of images that are to be
                classified by the classifier function (string)
    Returns:
        results_dic - Dictionary with 'key' as image filename and 'value' as a 
        List. The list contains for following item:
        index 0 = pet image label (string)
    """
	
	results_dic = dict()
	filenames_list = listdir(image_dir)

	for filename in filenames_list:
		pet_label = ''

		for name in filename.lower().split('_'):
			if name.isalpha():
				pet_label += name + ' '
			
		if filename not in results_dic:
			results_dic[filename] = pet_label.strip()
		else:
			print("** Warning: Key=", filename, 
				"already exists in results_dic with value =",
				results_dic[filename])

	return results_dic

