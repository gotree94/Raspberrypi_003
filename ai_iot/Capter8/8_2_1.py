import cv2
from pyzbar import pyzbar

def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        barcode_data = barcode.data.decode('utf-8')
        barcode_type = barcode.type
        text = f"{barcode_data} ({barcode_type})"
        cv2.putText(frame, text, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        print("Detected:", text)
    return frame

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)

    while True:
        ret, image = cap.read()
        if not ret:
            break

        image = read_barcodes(image)

        cv2.imshow("mycamera", image)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
