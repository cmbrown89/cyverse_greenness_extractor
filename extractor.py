#!/usr/bin/env python

"""Extractor algorithm implementation file
"""

def calculate(pxarray):
    """Algorithm
    Args:
        pxarray(numpy array): RGB pixel data at the plot level
    Returns:
    """

    # Extract the mean red, green, and blue values from the image bands
    r = pxarray[:,:,0].mean()
    g = pxarray[:,:,1].mean()
    b = pxarray[:,:,2].mean()   
    
    a = 0.667 # Veg index

    # Formulas
    veg_ind = g/(r**a*b**(1-a))
    exg = 2*g-(r+b)
    per_green = g/(r+b+g)

    indices = [veg_ind, exg, per_green]

    return indices