import cv2
from django.http import StreamingHttpResponse
from django.views.decorators import gzip
from django.shortcuts import render

# Create a cascade classifier for detecting faces
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to capture video from the default camera and detect faces
def detect_faces():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        # Convert the frame to grayscale and detect faces
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        # Draw a rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "You are ugly", (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


        # Convert the frame to JPEG format
        _, jpeg = cv2.imencode('.jpg', frame)

        # Yield the frame as bytes
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')

    cap.release()

# Function to stream the video feed from the webcam
@gzip.gzip_page
def webcam_feed(request):
    return StreamingHttpResponse(detect_faces(), content_type='multipart/x-mixed-replace; boundary=frame')

# Function to render the index.html template
def index(request):
    return render(request, 'Detection/index.html')
