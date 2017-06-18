# this thing will detect your face via webcam with
# pre-trained haarcascade model from opencv

import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while(True):
	# capture frame by frame
	ret, img = cap.read()
	# turn it into grayscale
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# find faces
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

	# locate face and draw rectangle
	for (x,y,w,h) in faces:
		img = cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 1)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]
		# and eyes
		eyes = eye_cascade.detectMultiScale(roi_gray)
		for(ex, ey, ew, eh) in eyes:
			cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0), 1)

	# show the video
	cv2.imshow('YourFace', img)

	# exit when 'q' is pressed
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()