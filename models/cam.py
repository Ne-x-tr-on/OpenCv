import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot access the webcam.")
    exit()

print("Press 'q' to quit.")

while True:
 
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame.")
        break
    
    cv2.imshow("Live Camera Feed", frame)
 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
