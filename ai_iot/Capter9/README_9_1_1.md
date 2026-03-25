# 라즈베리파이로 만드는 인공지능과 사물인터넷

## 챕터9. Yolo를 활용한 인공지능 객체인식

### 9.1 YOLOv8으로 객체 검출하기 285
* 회로 연결 285  
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

검출된 객체로 조건 설정하여 부저 울리기 291  

### 9-2.사용자 모델 만들기 294
라즈베리파이에서 버튼을 눌러 사진 찍어 저장하기 294  
압축하기 296  

### 9.2 사용자 학습 모델 만들기 299
데이터 라벨링 299  
나만의 모델 만들기 (ultralytics hub) 311  

### 9.3 사용자 학습 모델 적용하여 객체 검출하기 320
회로 연결 320  
모델 파일 라즈베리파이로 이동 321  
내가 만든 모델로 객체 인식하기 322  
객체가 검출되면 LED 깜빡이기 324  

</details>
