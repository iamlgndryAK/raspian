import cv2

def capture_video():
    # Open the video capture device (Raspberry Pi camera)
    cap = cv2.VideoCapture('/dev/video0')

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    try:
        while True:
            # Read a frame from the camera
            ret, frame = cap.read()

            # Check if the frame was successfully read
            if not ret:
                print("Error: Could not read frame.")
                break

            # Display the frame
            cv2.imshow('Video Capture', frame)

            # Break the loop if 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        # Release the video capture object and close the OpenCV window
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_video()
