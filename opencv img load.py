# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 17:36:56 2022

@author: Dell
"""

import cv2
import numpy as np
path = r"D:\wallpaper\harry_potter_and_the_deathly_hallows_part_2_villains-wallpaper-1680x1050.jpg"
img = cv2.imread(path)
cv2.imshow('woldemot', img)
cv2.waitKey()
cv2.destroyAllWindows()