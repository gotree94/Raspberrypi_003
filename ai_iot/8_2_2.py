import cv2
from pyzbar import pyzbar
from gpiozero import LEDBoard

leds = LEDBoard(4, 17, 27, 22)

def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        data = barcode.data.decode('utf-8')
        t = barcode.type
        text = f"{data} ({t})"
        cv2.putText(frame, text, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        print("Detected:", data)

        if data.lower() == "ledon":
            leds.on()
        elif data.lower() == "ledoff":
            leds.off()

    return frame

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)

    while True:
        ret, img = cap.read()
        if not ret:
            break

        img = read_barcodes(img)

        cv2.imshow("qr_led_control", img)

        if cv2.waitKey(1) == ord('q'):
            break

    leds.off()
    cap.release()
    cv2.destroyAllWindows()
