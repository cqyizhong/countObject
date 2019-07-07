from matplotlib import pyplot as plt
from skimage import data,io
from skimage.feature import  blob_dog,blob_log,blob_doh
from math import  sqrt
from skimage.color import rgb2gray
import glob
from skimage.io import imread


image = io.imread("./cell.jpeg")
im = rgb2gray(image)


blobs_log = blob_log(im,min_sigma=1,max_sigma = 15,num_sigma = 10,threshold = 0.1)
#计算第3列中的半径。
blobs_log [:,2] = blobs_log [:,2] * sqrt(2)
numrows = len(blobs_log)
print("统计的总数量：",numrows)

fig, ax = plt.subplots(1, 1)
plt.imshow(im, cmap=plt.cm.gray)
for blob in blobs_log:
    y, x, r = blob
    c = plt.Circle((x, y), r+5, color='lime', linewidth=2, fill=False)
    ax.add_patch(c)

plt.show()
