import cv2
import numpy as np

# Locate face in image. Using cv2 functions
def detect_face(image):
 
    # Specify the trained cascade classifier
    face_cascade_name = "/Users/grub/Desktop/Yale/makemebabies/haarcascade_frontalface_alt.xml"
 
    # Create a cascade classifier
    face_cascade = cv2.CascadeClassifier()
 
    # Load the specified classifier
    face_cascade.load(face_cascade_name)
 
    #Preprocess the image
    grayimg = cv2.cvtColor(image, cv2.cv.CV_BGR2GRAY)
    grayimg = cv2.equalizeHist(grayimg)
 
    #Run the classifiers
    faces = face_cascade.detectMultiScale(grayimg, 1.1, 2, 0|cv2.cv.CV_HAAR_SCALE_IMAGE, (30, 30))
 
    print "Faces detected"
 
    if len(faces) != 0:            # If there are faces in the images
        for face in faces:         # For each face in the image
 
            # Get the origin co-ordinates and the length and width till where the face extends
            x, y, lx, ly = face[0], face[1], face[2], face[3]
 
            # Draw rectangles around all the faces
            cv2.rectangle(image, (x, y), (x + lx, y + ly), cv2.cv.RGB(155, 255, 25), 2)
 
    # Display the images with the faces marked
    # cv2.imshow("Detected face", image)
 
    # cv2.waitKey(0)
 
    return (x, x+lx, y, y+ly)
 
 
def getRGB(im):
 
    # Specify the image to process and pass it to the function
    a,b,c,d = detect_face(im)

    totR = totG = totB = count = 0
    for i in range(len(im)):
        for j in range(len(im[i])):
            if (i < c or i > d or j < a or j > b):
                    im[i][j][0] = 255
                    im[i][j][1] = 255
                    im[i][j][2] = 255
            else:
                totR += im[i][j][0]
                totG += im[i][j][1]
                totB += im[i][j][2]
                count+= 1

    # cv2.imshow('im',im)
    # cv2.waitKey(0)

    return totR/count, totG/count, totB/count
 

def main():
    im1 = cv2.imread('/Users/grub/Desktop/Yale/BabyBlendr/python/image.jpg')
    im2 = cv2.imread('/Users/grub/Desktop/Yale/BabyBlendr/python/image3.jpg')

    avgR1, avgG1, avgB1 = getRGB(im1)
    avgR2, avgG2, avgB2 = getRGB(im2)

    avgR = (avgR1+avgR2)/2
    avgG = (avgG1+avgG2)/2
    avgB = (avgB1+avgB2)/2
    result = np.array([avgR, avgG, avgB])

    light = np.array([255, 218, 190])
    medium = np.array([180, 138, 120])
    dark = np.array([60, 46, 40])
    
    light_diff = np.linalg.norm(result-light)
    medium_diff = np.linalg.norm(result-medium)
    dark_diff = np.linalg.norm(result-dark)

    result_diff = [light_diff, medium_diff, dark_diff]

    if (min(result_diff) == light_diff):
        print "Light skin tone"
    elif (min(result_diff) == medium_diff):
        print "Medium skin tone"
    elif (min(result_diff) == dark_diff):
        print "Dark skin tone"


if __name__ == "__main__":
    main()