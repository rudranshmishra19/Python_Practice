import cv2

# Load the video
video_path = r"C:\Users\rudransh mishra\Videos\movies\F0rr35t.G7mp.94.br.sdm0v13sp01nt.cl7b.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Cannot open video file.")
else:
    print("Playing video...")
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Video", frame)  # Display each frame
        if cv2.waitKey(20) & 0xFF == ord("q"):  # Press 'q' to quit
            break

    cap.release()
    cv2.destroyAllWindows()
