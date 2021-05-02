import cv2 

clicked = False
def onMouse(event,x,y,flags,param):
    global clicked
    if event == cv2.cv.CV_EVENT_LBUTTONUP:
        clicked = True

cameraCapture = cv2.VideoCapture(0)
cv2.namedWindow('Mywindow')
cv2.setMouseCallback('mywindow',onMouse)

print('Showing camera feed. Click wondow oe press any key to stop.')
success, frame = cameraCapture.read()
while success and cv2.waitKey(1) == -1 and not clicked:
    cv2.imshow('mywindow',frame)
    success, frame = cameraCapture.read()

cv2.destroyWindow('mywindow')