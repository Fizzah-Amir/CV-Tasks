import cv2
cap = cv2.VideoCapture("9095572-uhd_2160_3840_25fps.mp4")
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
out = cv2.VideoWriter("output.mp4", fourcc, fps, (width, height))
while True:
    ret, frame = cap.read()
 #ret shows true or fals eis there a frame,frame stores a frame from cap
    if not ret:
        break
    cv2.rectangle(frame, (100, 100), (500, 400), (0, 255, 0), 3)
    cv2.putText(
    frame,
    "Computer Vision Week 1",
    (100, 80),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0, 255, 0),
    2 )
    out.write(frame)
cap.release()
out.release()