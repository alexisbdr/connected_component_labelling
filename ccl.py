import cv2 
import numpy as np
from union_find_array import *
import itertools
import math, sys, random

paths = (
        'face.bmp',
        'face_old.bmp',
        'gun.bmp',
        'test.bmp')

def CCL(img): 
    
    height, width = img.shape
    union_find = UFarray()
    print(height, width)
    # First pass
    labels = {}
    for  y in range(width):
        for x in range(height):
    
            if img[x,y] == 255:
                pass
            
            elif x+1 < width and img[x+1, y-1] == 0:
                c = labels[(x+1, y-1)]
                labels[x, y] = c
            
                if img[x-1, y-1] == 0:
                    a = labels[(x-1, y-1)]
                    union_find.union(c, a)
                
                elif img[x-1, y] == 0:
                    d = labels[(x-1, y)]
                    union_find.union(c, d)
            
            elif img[x-1, y-1] == 0:
                labels[x, y] = labels[(x-1, y-1)]
            
            elif img[x, y-1] == 0:
                labels[x, y] = labels[(x, y-1)]

            elif img[x-1, y] == 0:
                labels[x, y] = labels[(x-1, y)]
            
            else: 
                labels[x, y] = union_find.makeLabel()
            
    union_find.flatten()
    
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    color = {}
    for (x, y) in labels:
        labels[(x, y)] = union_find.find(labels[(x, y)])

        if labels[(x,y)] not in color: 
            color[labels[(x,y)]] = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        
        img[x, y] = color[labels[(x,y)]]
                
    return labels, img                                                                             

def main():
   
    #Read in the images
    for path in paths: 
        img = cv2.imread(path, 0)
        img = 255-img
        cv2.imshow(path , img)
        labels, labeled_img = CCL(img)
        cv2.imshow(path + '/labeled', labeled_img) 
        #cv2.imwrite("images/" + path, labeled_img)

    key = cv2.waitKey(0)
    
    if key == 27 or key == 'q': 
        cv2.destroyAllWindows() 


if __name__ == "__main__":
    main()
