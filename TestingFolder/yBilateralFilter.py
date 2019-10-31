import cv2
from matplotlib import pyplot as plt

image = cv2.imread("/home/pc/Documents/BiDirectionalCascadeEdge/images/wrongImages/bdcn/26.jpg")
img_0 = cv2.blur(image, ksize = (7, 7))
img_1 = cv2.GaussianBlur(image, ksize = (7, 7), sigmaX = 0)
img_2 = cv2.medianBlur(image, 7)
img_3 = cv2.bilateralFilter(image, 20, sigmaSpace = 75, sigmaColor =75)# Plot the images
img_3 = cv2.Canny(image, 20, sigmaSpace = 75, sigmaColor =75)# Plot the images
images = [img_0, img_1, img_2, img_3]

fig, axs = plt.subplots(nrows = 1, ncols = 4, figsize = (20, 20))
for ind, p in enumerate(images):
    ax = axs[ind]
    ax.imshow(p)
    ax.axis('off')
plt.show()


