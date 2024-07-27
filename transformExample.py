import transform
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help="path to the image file")
ap.add_argument("-c", "--coords", help="comma separated list of source points")
args = vars(ap.parse_args())


img = cv2.imread(args["image"])
pts = np.array(eval(args["coords"]), dtype="float32")

warped = transform.fourPointTransform(img, pts)

cv2.imshow("Original", img)
cv2.imshow("Warped", warped)
cv2.waitKey(0)