import cv2

# Open USB camera
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if not cap.isOpened():
    print("Error: Could not open USB camera")
    exit()
    
print("Camera started. Press 'q' to quit.")

while True:
    # Capture a frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame")
        break

    # Display the frame
    cv2.imshow("USB Camera", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release camera and close window
cap.release()
cv2.destroyAllWindows()
