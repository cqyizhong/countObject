# from matplotlib import pyplot as plt
from skimage import data
from skimage.feature import  blob_dog,blob_log,blob_doh
from math import  sqrt
from skimage.color import rgb2gray
import glob
from skimage.io import imread

def countStars(stars_file):

    im = imread(stars_file,as_grey = True)

    blobs_log = blob_log(im,max_sigma = 30,num_sigma = 10,threshold = .1)
    #计算第3列中的半径。
    blobs_log [:,2] = blobs_log [:,2] * sqrt(2)
    numrows = len(blobs_log)
    print("星星的总数量：",numrows)
    return numrows

if __name__ == '__main__':

    stars_file = "./sky1.jpeg"

    countStars(stars_file)

