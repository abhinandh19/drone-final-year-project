import picamera
import time
import cv2
import cv2.aruco as aruco
 
 
#cap = cv2.VideoCapture(0)
camera = picamera.PICamera()
 
while(True):
    # Capture frame-by-frame
    #ret, frame = cap.read()
    ret, frame = camera.capture()

    #print(frame.shape) #480x640
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get((aruco.DICT_4X4_1000)or(aruco.DICT_5X5_1000)or(aruco.DICT_6X6_1000)or(aruco.DICT_7X7_1000))
    parameters =  aruco.DetectorParameters_create()
 
    #print(parameters)
 
    '''    detectMarkers(...)z
        detectMarkers(image, dictionary[, corners[, ids[, parameters[, rejectedI
        mgPoints]]]]) -> corners, ids, rejectedImgPoints
        '''
        #lists of ids and the corners beloning to each id
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    print(corners)
 
    #It's working.
    # my problem was that the cellphone put black all around it. The alrogithm
    # depends very much upon finding rectangular black blobs
 
    gray = aruco.drawDetectedMarkers(gray, corners)
 
    #print(rejectedImgPoints)
    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
