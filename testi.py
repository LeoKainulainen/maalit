import cv2
import numpy as np

##Opencv lukee kuvan ja muuntaa sen grayscaleksi
img = cv2.imread('bettershapes.jpg', cv2.IMREAD_GRAYSCALE)

##Muuntaa kontrastia, että kuviot olisivat vain yhtä väriä (mustaa)
_, threshold = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)

##Etsii kuvioiden ääriviivat 
contours,hierachy=cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

font = cv2.FONT_HERSHEY_COMPLEX
triangle = 0
rectangle = 0
pentagon = 0
ellipse = 0
circle = 0

##Käy läpi ääriviivat
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength (cnt, True), True)
    cv2.drawContours(img, [approx], 0,(0), 4)
    

    ##Ottaa kaksi pisteen kuvioista (ensimmäiset x ja y -koordinaatit)
    x = approx.ravel()[0]
    y = approx.ravel()[1]

    ##käy läpi ääriviivat, kirjoittaa kuvioiden nimet ja asettaa tekstin
    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x, y), font, 1, (0))
        triangle = triangle + 1
        #print(approx.ravel())
    elif len(approx) == 4:
        cv2.putText(img, "Rectangle", (x, y), font, 1, (0))
        rectangle = rectangle + 1
        
    elif len(approx) == 5:
        cv2.putText(img, "Pentagon", (x, y), font, 1, (0))
        pentagon = pentagon + 1

    elif 6 < len(approx) < 15:
        cv2.putText(img, "Ellipse", (x, y), font, 1, (0))
        ellipse = ellipse + 1
        
    else:
        cv2.putText(img, "Circle", (x, y), font, 1, (0))
        circle = circle + 1

    
##Näyttää greyscale kuvan johon on piirretty ääriviivat ja kirjoitettu kuvioiden nimet  
cv2.imshow('image', img)
print("The number of shapes is " + str(triangle + rectangle + pentagon + ellipse + circle))

#cv2.imshow("Threshold", threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
