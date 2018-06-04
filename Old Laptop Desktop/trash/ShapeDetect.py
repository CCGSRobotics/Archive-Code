# import the necessary packages
import cv2
 
class ShapeDetector:
	def __init__(self):
		pass
 
	def detect(self, c):
		# initialize the shape name and approximate the contour
		shape = "unidentified"
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.04 * peri, True)
       		# if the shape is a triangle, it will have 3 vertices
		if len(approx) == 3:
			shape = "triangle"
 
		# if the shape has 4 vertices, it is either a square or
		# a rectangle
		elif len(approx) == 4:
			# compute the bounding box of the contour and use the
			# bounding box to compute the aspect ratio
			(x, y, w, h) = cv2.boundingRect(approx)
			ar = w / float(h)
 
			# a square will have an aspect ratio that is approximately
			# equal to one, otherwise, the shape is a rectangle
			shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"
 
		# if the shape is a pentagon, it will have 5 vertices
		elif len(approx) == 5:
			shape = "pentagon"
 
		# otherwise, we assume the shape is a circle
		else:
			shape = "circle"
 
		# return the name of the shape
		return shape

#-------------------------------------------------------------------------#
#-------------------------------------------------------------------------#

import argparse
import imutils
#import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i','--image', required=True, help="path to the input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
#cv2.imshow("image",image)
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])

gray = cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5,5), 0)
thresh = cv2.threshold(blurred, 90, 255, cv2.THRESH_BINARY)[1]
#print(thresh)
cnts = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
sd = ShapeDetector()
#print(cnts)
im = image

for c in cnts:
 #   print("shape")
  #  print(cnts)
    M = cv2.moments(c)
    if M["m00"] != 0:
        #print(M["m00"])
        cX = int((M["m10"]/M['m00'])*ratio) + 100
        cY = int((M["m01"]/M['m00'])*ratio) + 130
        shape = sd.detect(c)
        print(M['m10']/M['m00']*ratio)

        c = c.astype("float")
        #c *= ratio
        c = c.astype('int')
        cv2.drawContours(im,[c], -1, (0,255,0),2)
        cv2.putText(im, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255,0,0),2)
       # f = open("image.txt", "wb")
       # f.write(im)
       # f.close()
    else:
        print(M["m00"])
    cv2.imshow("image",im)
    cv2.waitKey(0)
