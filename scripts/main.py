import numpy as np
import cv2
from skimage import morphology

def detect_players(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_green = np.array([30, 40, 40])
    upper_green = np.array([70, 255, 255])

    #blue range
    lower_blue = np.array([90,50,50])
    upper_blue = np.array([140,255,255])

    #Red range
    lower_red = np.array([0,50,50])
    upper_red = np.array([10,255,255])
    mask = cv2.inRange(hsv, lower_green, upper_green)
    
    res = cv2.bitwise_and(img, img, mask=mask)
    res_bgr = cv2.cvtColor(res, cv2.COLOR_HSV2BGR)
    res_gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    
    kernel = morphology.disk(5).astype(np.uint8)
    thresh = cv2.threshold(res_gray, 127, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)[1]

    closed_image = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    opened_image = cv2.morphologyEx(closed_image, cv2.MORPH_OPEN, kernel)
    
    _, contours, hierarchy = cv2.findContours(closed_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    font = cv2.FONT_HERSHEY_SIMPLEX

    output_img = img.copy()
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        if h >= (1.2) * w:
            if w > 5 and h >= 5:
                player_img = img[y : y + h, x : x + w]
                player_hsv = cv2.cvtColor(player_img, cv2.COLOR_BGR2HSV)

                #If player has blue jersy
                mask1 = cv2.inRange(player_hsv, lower_blue, upper_blue)
                res1 = cv2.bitwise_and(player_img, player_img, mask=mask1)
                res1 = cv2.cvtColor(res1,cv2.COLOR_HSV2BGR)
                res1 = cv2.cvtColor(res1,cv2.COLOR_BGR2GRAY)
                nzCountBlue = cv2.countNonZero(res1)

                #If player has red jersy
                mask2 = cv2.inRange(player_hsv, lower_red, upper_red)
                res2 = cv2.bitwise_and(player_img, player_img, mask=mask2)
                res2 = cv2.cvtColor(res2,cv2.COLOR_HSV2BGR)
                res2 = cv2.cvtColor(res2,cv2.COLOR_BGR2GRAY)
                nzCountRed = cv2.countNonZero(res2)

                if(nzCountBlue >=15):
                    #cv2.putText(output_img, 'Time A', (x-2, y-2), font, 0.8, (255,0,0), 3, cv2.LINE_AA)
                    cv2.rectangle(output_img,(x,y),(x+w,y+h),(255,0,0),3)
                elif(nzCountRed >=15):
                    #cv2.putText(output_img, 'Time B', (x-3, y-2), font, 0.8, (0,0,255), 1, cv2.LINE_AA)
                    cv2.rectangle(output_img,(x,y),(x+w,y+h),(0,0,255),2)
                    
    return output_img
vidcap = cv2.VideoCapture('./videos/Bélgica 3 x 2 japão - Corte 1.mp4')
success,image = vidcap.read()
success = True
while success:
    output_img = detect_players(image)
    cv2.imshow('Match Detection',output_img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    success,image = vidcap.read()
vidcap.release()
cv2.destroyAllWindows()