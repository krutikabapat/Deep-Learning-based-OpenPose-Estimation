import cv2

protofile = "/home/krutika/Documents/Open_Pose/pose.prototxt"
weightsfile = "/home/krutika/Documents/Open_Pose/pose.caffemodel "

net = cv2.dnn.readnetFromCaffe(protofile, weightsfile)

frame = cv2.imread('/home/krutika/Documents/Open_Pose/single.jpeg')

width = 368
height = 368

blob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (width, height), (0, 0, 0), swapRB=False, crop=False)

net.setInput(blob)

output = net.forward()

H = out.shape[2]
W = out.shape[3]

points = []
for i in range(len()):
	probMap = output[0, i, :, :]
 
	# Find global maxima of the probMap.
	minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)
	 
	# Scale the point to fit on the original image
	x = (frameWidth * point[0]) / W
	y = (frameHeight * point[1]) / H
 
	if prob > threshold : 
		cv2.circle(frame, (int(x), int(y)), 15, (0, 255, 255), thickness=-1, lineType=cv.FILLED)
		cv2.putText(frame, "{}".format(i), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1.4, (0, 0, 255), 3, lineType=cv2.LINE_AA)
 
		# Add the point to the list if the probability is greater than the threshold
		points.append((int(x), int(y)))
	else :
		points.append(None)
 
cv2.imshow("Output-Keypoints",frame)
cv2.waitKey(0)
cv2.destroyAllWindows()


for pair in POSE_PAIRS:
	partA = pair[0]
	partB = pair[1]
 
	if points[partA] and points[partB]:
		cv2.line(frameCopy, points[partA], points[partB], (0, 255, 0), 3)