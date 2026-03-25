import os
from datetime import datetime
import cv2

SAVE_DIR = os.path.join(os.path.dirname(__file__), "pictures")
os.makedirs(SAVE_DIR, exist_ok=True)

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ok, image = cap.read()
        if not ok:
            break

        cv2.imshow("camera", image)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("s"):
            filename = datetime.now().strftime("%Y%m%d_%H%M%S_%f") + ".png"
            path = os.path.join(SAVE_DIR, filename)
            cv2.imwrite(path, image)
            print("saved:", path)
        elif key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
