import numpy as np
import cv2
import sys

def digitRecg():
    #im = cv2.imread('digitRcgTestImg_short.png')
    im = cv2.imread('screenshot_crop.png')
    cv2.imshow('im',im)
    cv2.waitKey(0)

    blur = cv2.GaussianBlur(im,(11,11),cv2.BORDER_CONSTANT)
    cv2.imshow('blur',blur)
    cv2.waitKey(0)
    blur = cv2.bilateralFilter(blur,50,100,150) #  (img, d, sigmaColor, sigmaSpace)
    cv2.imshow('blur',blur)
    cv2.waitKey(0)
    #blur = cv2.GaussianBlur(blur,(11,11),cv2.BORDER_CONSTANT)
    #cv2.imshow('blur',blur)
    #cv2.waitKey(0)

    gray = cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray',gray)
    cv2.waitKey(0)

    edges = cv2.Canny(gray,50,100,apertureSize = 3) # img, 
    cv2.imshow('edges',edges)
    cv2.waitKey(0)

    # erosion and dilation
    thresh = edges
    kernel = np.ones((3,3), np.uint8)
    thresh = cv2.dilate(thresh, kernel, iterations=3)
    cv2.imshow('binary',thresh)
    cv2.waitKey(0)

    thresh = cv2.erode(thresh, kernel, iterations=3)
    cv2.imshow('binary',thresh)
    cv2.waitKey(0)


    #################      Now finding Contours         ###################
    #contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    samples =  np.empty((0,100))
    responses = np.empty((0),dtype=int)
    keys = [i for i in range(48,58)]

    for cnt in contours:
        if cv2.contourArea(cnt)>50:
            [x,y,w,h] = cv2.boundingRect(cnt) # get contour rectangle
            cv2.rectangle(im,(x,y),(x+w,y+h),(0,0,255),2) # draw rectangle

            # retrive ROI and compress to small size
            roi = thresh[y:y+h,x:x+w]
            roismall = cv2.resize(roi,(10,10))
            cv2.imshow('ori',im)

            key = cv2.waitKey(0)
            if key == 27:  # quit
                sys.exit()
            elif key in keys:
                responses = np.append(responses,int(chr(key)))
                sample = roismall.reshape((1,100))
                samples = np.append(samples,sample,0)

    responses = np.reshape(responses,(responses.size, 1))

    np.savetxt('generalsamples.data',samples)
    np.savetxt('generalresponses.data',responses)

    cv2.destroyAllWindows()
