import cv2
import imutils
import numpy as np
import os
def draw_color_mask(img, borders, color=(0, 0, 0)):
    h = img.shape[0]
    w = img.shape[1]

    x_min = int(borders[0] * w / 100)
    x_max = w - int(borders[2] * w / 100)
    y_min = int(borders[1] * h / 100)
    y_max = h - int(borders[3] * h / 100)

    img = cv2.rectangle(img, (0, 0), (x_min, h), color, -1)
    img = cv2.rectangle(img, (0, 0), (w, y_min), color, -1)
    img = cv2.rectangle(img, (x_max, 0), (w, h), color, -1)
    img = cv2.rectangle(img, (0, y_max), (w, h), color, -1)
    #cv2.imshow("draw_color_mask",img)
    return img


def preprocess_image_change_detection(img, gaussian_blur_radius_list=None, black_mask=(5, 10, 5, 0)):
    gaussian_blur_radius_list = [15, 17, 25]
    gray = img.copy()
    gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
    if gaussian_blur_radius_list is not None:
        for radius in gaussian_blur_radius_list:
            gray = cv2.GaussianBlur(gray, (radius, radius), 0)
    #cv2.imshow("grayb4",gray)
    gray = draw_color_mask(gray, black_mask)
    #cv2.imshow("gray",gray)
    return gray


def compare_frames_change_detection(prev_frame, next_frame, min_contour_area):
    frame_delta = cv2.absdiff(prev_frame, next_frame)
    #cv2.imshow('frame_delta', frame_delta)

    thresh = cv2.threshold(frame_delta, 45, 255, cv2.THRESH_BINARY)[1]
    #cv2.imshow('thresh1', thresh)
    thresh = cv2.dilate(thresh, None, iterations=2)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    score = 0
    res_cnts = []
    for c in cnts:
        #print(cv2.contourArea(c))
        if cv2.contourArea(c) < min_contour_area:
            continue
        cv2.drawContours(next_frame, [c], -1, (255, 255, 0), 2)
        res_cnts.append(c)
        score += cv2.contourArea(c)

    return score, res_cnts, thresh


