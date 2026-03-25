# 라즈베리파이로 만드는 인공지능과 사물인터넷

## 챕터9. Yolo를 활용한 인공지능 객체인식

### 9.1 YOLOv8으로 객체 검출하기 285

* 회로 연결 285

| 라즈베리파이 핀 | 부품 | 
|:-------:|:-------:|
| GPIO 18 |  BUZZER

* 라이브러리 설치 286  

```
pip install torch opencv-python ultralytics --break-system-packages

1단계: 기존 torch 완전 제거
pip uninstall torch torchvision triton --break-system-packages -y

2단계: ARM CPU용 torch 설치 
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu --break-system-packages

3단계: 확인 
python3 -c "import torch; print(torch.__version__)"
```

* 9_1_1 라이브러리 확인 286

```
import cv2
import torch
import ultralytics
import numpy

print("cv2:", cv2.__version__)
print("torch:", torch.__version__)
print("ultralytics:", ultralytics.__version__)
print("numpy:", numpy.__version__)
```

* 9_1_2 기본 예제로 객체 검출하기 287  

```
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
        cv2.putText(
            frame,
            label,
            (x1, max(10, y1 - 6)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 255, 0),
            1,
        )
    return frame

if __name__ == "__main__":
    model = YOLO("yolov8n.pt")
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise SystemExit("Camera open failed")

    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                break

            results = model(
                frame,
                imgsz=320,
                conf=0.5,
                iou=0.5,
                device="cpu",
            )[0]

            out = draw_detections(frame, results, model.names)
            cv2.imshow("YOLOv8 (OpenCV)", out)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()
```


## 📌 YOLO v8에서 기본 예제로 제공되는 80개의 인식 리스트

| ID | Class           | ID | Class           | ID | Class           | ID | Class           | ID | Class           |
|----|----------------|----|----------------|----|----------------|----|----------------|----|----------------|
| 0  | person         | 1  | bicycle        | 2  | car            | 3  | motorcycle     | 4  | airplane       |
| 5  | bus            | 6  | train          | 7  | truck          | 8  | boat           | 9  | traffic light  |
| 10 | fire hydrant   | 11 | stop sign      | 12 | parking meter  | 13 | bench          | 14 | bird           |
| 15 | cat            | 16 | dog            | 17 | horse          | 18 | sheep          | 19 | cow            |
| 20 | elephant       | 21 | bear           | 22 | zebra          | 23 | giraffe        | 24 | backpack       |
| 25 | umbrella       | 26 | handbag        | 27 | tie            | 28 | suitcase       | 29 | frisbee        |
| 30 | skis           | 31 | snowboard      | 32 | sports ball    | 33 | kite           | 34 | baseball bat   |
| 35 | baseball glove | 36 | skateboard     | 37 | surfboard      | 38 | tennis racket  | 39 | bottle         |
| 40 | wine glass     | 41 | cup            | 42 | fork           | 43 | knife          | 44 | spoon          |
| 45 | bowl           | 46 | banana         | 47 | apple          | 48 | sandwich       | 49 | orange         |
| 50 | broccoli       | 51 | carrot         | 52 | hot dog        | 53 | pizza          | 54 | donut          |
| 55 | cake           | 56 | chair          | 57 | couch          | 58 | potted plant   | 59 | bed            |
| 60 | dining table   | 61 | toilet         | 62 | tv             | 63 | laptop         | 64 | mouse          |
| 65 | remote         | 66 | keyboard       | 67 | cell phone     | 68 | microwave      | 69 | oven           |
| 70 | toaster        | 71 | sink           | 72 | refrigerator   | 73 | book           | 74 | clock          |
| 75 | vase           | 76 | scissors       | 77 | teddy bear     | 78 | hair drier     | 79 | toothbrush     |


* 9_1_3 검출된 객체로 조건 설정하여 부저 울리기 291

```
import cv2
from ultralytics import YOLO
from gpiozero import PWMOutputDevice
from time import sleep

buzzer = PWMOutputDevice(18)

def beep():
    buzzer.frequency = 440
    buzzer.value = 0.5
    sleep(0.3)
    buzzer.value = 0

def draw_detections(frame, results, names):
    if results is None:
        return frame
    for b in results.boxes:
        cls_id = int(b.cls.item())
        conf = float(b.conf.item())
        x1, y1, x2, y2 = map(int, b.xyxy[0].tolist())
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        label = f"{names[cls_id]} {conf:.2f}"
        cv2.putText(
            frame,
            label,
            (x1, max(10, y1 - 6)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 255, 0),
            1,
        )
    return frame

if __name__ == "__main__":
    model = YOLO("yolov8n.pt")
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise SystemExit("Camera open failed")

    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                break

            results = model(frame, imgsz=320, conf=0.5, iou=0.5, device="cpu")[0]

            person_detected = False
            for b in results.boxes:
                if int(b.cls.item()) == 0:
                    person_detected = True
                    break

            if person_detected:
                beep()

            out = draw_detections(frame, results, model.names)
            cv2.imshow("YOLOv8 (OpenCV)", out)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        buzzer.off()
        cap.release()
        cv2.destroyAllWindows()
```

### 9-2.사용자 모델 만들기 294

* 9_2_1 라즈베리파이에서 버튼을 눌러 사진 찍어 저장하기 294

```
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
```

* 9_2_2 압축하기 296

```
import os
import zipfile

def zip_pictures_folder():
    base_dir = os.path.dirname(__file__)
    pictures_dir = os.path.join(base_dir, "pictures")
    zip_path = os.path.join(base_dir, "pictures.zip")

    if not os.path.exists(pictures_dir):
        print("pictures folder not found.")
        return

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(pictures_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, pictures_dir)
                zipf.write(file_path, arcname)
    print(f"zip created: {zip_path}")

if __name__ == "__main__":
    zip_pictures_folder()
```


### 9.3 사용자 학습 모델 만들기 299
데이터 라벨링 299  

```
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
```

나만의 모델 만들기 (ultralytics hub) 311  

### 9.4 사용자 학습 모델 적용하여 객체 검출하기 320
회로 연결 320  
모델 파일 라즈베리파이로 이동 321  
내가 만든 모델로 객체 인식하기 322  

```
import cv2
from ultralytics import YOLO
from gpiozero import LEDBoard
import time

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
    target_names = {"ultrasonic", "vr", "led", "ble"}

    leds = LEDBoard(4, 17, 27, 22)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise SystemExit("Camera error")

    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                break

            results = model(frame, imgsz=320, conf=0.5, iou=0.5, device="cpu")[0]

            detected = any(
                model.names[int(b.cls.item())] in target_names
                for b in results.boxes
            )

            if detected:
                leds.on()
                time.sleep(0.2)
                leds.off()
                time.sleep(0.2)

            out = draw_detections(frame, results, model.names)
            cv2.imshow("YOLOv8", out)

            if cv2.waitKey(1) == ord('q'):
                break
    finally:
        leds.off()
        cap.release()
        cv2.destroyAllWindows()
```

객체가 검출되면 LED 깜빡이기 324  

</details>
