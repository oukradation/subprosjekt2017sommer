import numpy as numpy
import cv2

# connect to defalut camera on the PC
# front camera for a laptop
cap = cv2.VideoCapture(0)  

while(True):
	# capture a sigle frame
	ret, frame = cap.read()

	# change 'frame' into grayscale
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# put image on the gui
	cv2.imshow('frame', gray)
	cv2.imshow('org', frame)

	# finnish program when q is pressed
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# disconnect the camera
cap.release()
cv2.destroyAllWindows()
