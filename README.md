# Connected Component Labelling in Python

### Contributors:

* [Alexis Baudron] (abe3897)

---

### Installing all dependencies 

Ubuntu Linux machine with python3.5 or +

$ python3 -m venv venv 
$ unset PYTHONPATH
$ source venv/bin/activate
$ pip install -r requirements.txt 

### Run the code

Activate virtual environment ($ source venv/bin/activate)
$ python ccl.py

### Algorithm 

This is an implementation of the sequential labeling algorithm as discussed in class. 

We start by loading in the image using OpenCv's imread function, we load the function in grayscale-indicated by the 0 tag passed to the imread function. We invert the image and then show it. Inverting the image changes absolutely nothing to the process we will just be doing the same algorithm but just inverted. 

The CCL algorithm will then loop through the rows and columns of each image. Before doing so we first initialize our UFarray instance, this is a clas imported from the ufarray.py file. In this file you can find an implementation of a union-find method in Python found in official documentation and adjutsed for these purposes. 
We follow the sequential part of the algorithm, at each iteration we check the pixel positions to the left, above, below, left-below and left-above and compare with the existing label. 
Additions made to the traditional algorithm: we proceed to join labels during the algorithm when the right-above and left-above are the same as well as when the right-above and left-most label are the same. Which reduces the overall union-find towards the end
If no labels have been found we make a new label. 
Once all pixels have been labelled we run a union_find on the label positions.
Each time a new component (unique label) is identified we assign it a new color using randint. The new colors are applied to the individual component ontop of the original image (that has been converted to RGB...)

### Results Analysis
The results are of the algorithm are written into the images file as 'labelled' 
