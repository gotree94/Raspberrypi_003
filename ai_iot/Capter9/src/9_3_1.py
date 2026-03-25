import cv2
from ultralytics import YOLO

def draw_detections(frame, results, names):
    if results is None:
        return frame
    for b in results.boxes:
        cls_id = int(b.cls.item())
        conf = float(b.conf.item())
        x1, y1, x2, y2 = map(int, b.xyxy[0].tolist())
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        label = f"{names[cls_id]} {conf:.2f}"
        cv2.putText(frame, label, (x1, max(10, y1 - 6)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    return frame

if __name__ == "__main__":
    model = YOLO("iot_model.pt")
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise SystemExit("Camera error")

    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                break

            results = model(frame, imgsz=320, conf=0.5, iou=0.5, device="cpu")[0]

            out = draw_detections(frame, results, model.names)
            cv2.imshow("YOLOv8", out)

            if cv2.waitKey(1) == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()
