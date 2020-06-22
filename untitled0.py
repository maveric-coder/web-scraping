# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:57:52 2019

@author: 1604201
"""

#!/usr/bin/env python

import cv2 
  
# Save image in set directory 
# Read RGB image 
img = cv2.imread('Eat-half-walk-double.jpg')  
  
# Output img with window name as 'image' 
cv2.imshow('image', img)  
  
# Maintain output window utill 
# user presses a key 
cv2.waitKey(0)         
  
# Destroying present windows on screen 
cv2.destroyAllWindows()  