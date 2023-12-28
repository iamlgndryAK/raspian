import cv2
import picamera
import picamera.array
import numpy as np

def capture_camera():
    with picamera.PiCamera() as camera:
        # Set the camera resolution (adjust as needed)
        camera.resolution = (640, 480)

        # Use a NumPy array to hold the image data
        image_array = np.empty((camera.resolution[1] * camera.resolution[0] * 3,), dtype=np.uint8)

        with picamera.array.PiRGBArray(camera, size=camera.resolution) as stream:
            # Capture a frame from the camera
            camera.capture(stream, format='bgr', use_video_port=True)

            # Access the NumPy array and use it with OpenCV
            frame = stream.array

            # Display the captured frame using OpenCV
            cv2.imshow('Camera Capture', frame)
            cv2.waitKey(0)  # Wait for a key press to close the window

if __name__ == "__main__":
    capture_camera()
