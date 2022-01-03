import cv2

from config import CASCADES


def is_user_wants_quit() -> bool:
    """
    Check if 'q' key is pressed
    """
    # 0xFF for masking the last 8 bits of keycode
    return cv2.waitKey(1) & 0xFF == ord("q")


def show_frame(frame) -> None:
    """
    Open 'Video' window with a single frame captured from a webcam
    """
    cv2.imshow("Video", frame)


def draw_sqare(frame, color) -> None:
    """
    Draw a rectangle around detected object with 2 pixels line thickness
    """
    cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)


def get_cascades() -> list[tuple]:
    """
    Get pre-trained cascades from config.py with 'draw' key == True
    """
    cascades = [
        (cv2.CascadeClassifier(cascade["path"]), cascade["color"])
        for title, cascade in CASCADES.items()
        if cascade["draw"]
    ]
    return cascades


if __name__ == "__main__":
    # load pre-trained cascades
    cascades = get_cascades()

    # start video capture from a default webcam
    video_capture = cv2.VideoCapture(0)  # [0] for default webcam

    # main loop
    while True:

        # check if video is available
        if not video_capture.isOpened():
            print("Couldn't find your webcam... Sorry :c")

        # capture video frame by frame
        _, webcam_frame = video_capture.read()

        # convert BlueGreenRed colored frame into a black and white mode
        gray_frame = cv2.cvtColor(webcam_frame, cv2.COLOR_BGR2GRAY)

        # loop through loaded cascades
        for cascade, color in cascades:

            # place detected objects coordinates in captures variable
            captures = [
                cascade.detectMultiScale(
                    gray_frame, scaleFactor=1.1, minNeighbors=10, minSize=(30, 30)
                )
            ]

            # loop through detected objects coordinates
            for capture in captures:

                # draw a rectangle with given coordinates and color
                for (x, y, w, h) in capture:
                    draw_sqare(webcam_frame, color)

        # draw each frame in 'Video' window
        show_frame(webcam_frame)

        # exit if 'q' key is pressed
        if is_user_wants_quit():
            break

    # release webcam before quitting
    video_capture.release()

    # close 'Video' window
    cv2.destroyAllWindows()
