import cv2
import numpy as np
import math

def getComment(img):
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	edges = cv2.Canny(gray, 80, 120)
	lines = cv2.HoughLines(edges, 1, np.pi/2, 200);

	arrays = []
	for rho,theta in lines[0]:
		a = np.cos(theta)
		b = np.sin(theta)
		x0 = a*rho
		y0 = b*rho
		x1 = int(x0 + 1000*(-b))
		y1 = int(y0 + 1000*(a))
		x2 = int(x0 - 1000*(-b))
		y2 = int(y0 - 1000*(a))
		# cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
		arrays.append([x1, y1, x2, y2])

	return arrays

	# cv2.imshow('result.jpg',img)
	# cv2.waitKey(0)

def cutoutCaption(img, arrays):
	arrays = getComment(img)
	firsty = np.round((arrays[0][1]+arrays[0][3])/2)
	secondy = np.round((arrays[1][1]+arrays[1][3])/2)

	img_edit = img[firsty:secondy-1][:]
	for i in range(len(img_edit)):
		for j in range(len(img_edit[i])):
			if (round(img_edit[i][j][0]) < 220 and round(img_edit[i][j][1]) < 220 and round(img_edit[i][j][2]) < 220):
				img_edit[i][j][0] = 0
				img_edit[i][j][1] = 0
				img_edit[i][j][2] = 0

	return img_edit

def main():
	img = cv2.imread("/Users/grub/Desktop/Yale/BabyBlendr/python/photo.PNG")
	im2 = cv2.imread("/Users/grub/Desktop/Yale/BabyBlendr/python/trial3.png")
	array1 = getComment(img)
	array2 = getComment(im2)
	res1 = cutoutCaption(img, array1)
	res2 = cutoutCaption(im2, array2)

	cv2.imwrite('res1.jpg', res1)
	cv2.imwrite('res2.jpg', res2)

if __name__ == "__main__":
	main()