# 라즈베리파이로 만드는 인공지능과 사물인터넷

## 챕터2. 라즈베리파이 입출력 활용

### 2.1 디지털 출력으로 LED 제어하기 64

* 2_1_1 LED 1개 깜빡이기 64

```
from gpiozero import LED
import time

led1 = LED(4)

while True :
    led1.on()
    time.sleep(1.0)
    led1.off()
    time.sleep(1.0)
```

* 2_1_2 안전하게 프로그램 종료하기 67  

```
from gpiozero import LED
import time

led1 = LED(4)

try :
    while True :
        led1.on()
        time.sleep(1.0)
        led1.off()
        time.sleep(1.0)

except KeyboardInterrupt:
    led1.off()
    print("end")
```

* 2_1_3 LED 여러 개 깜빡이기 68  

```
from gpiozero import LED
import time

led1 = LED(4)
led2 = LED(17)
led3 = LED(27)
led4 = LED(22)

try :
    while True :
        led1.on()
        led2.on()
        led3.on()
        led4.on()
        time.sleep(1.0)
        led1.off()
        led2.off()
        led3.off()
        led4.off()
        time.sleep(1.0)

except KeyboardInterrupt:
    led1.off()
    led2.off()
    led3.off()
    led4.off()
    print("end")

```

* 2_1_4 값을 직접 입력하여 LED 켜고 끄기 69  

```
from gpiozero import LED
import time

led1 = LED(4)

try :
    while True :
        led1.value = 1
        time.sleep(1.0)
        led1.value = 0
        time.sleep(1.0)

except KeyboardInterrupt:
    led1.value = 0
    print("end")

```

* 2_1_5 GPIO를 제어하는 코드로 LED 켜고 끄기 70  

```
from gpiozero import OutputDevice
import time

led1 = OutputDevice(4)

try:
    while True:
        led1.on()
        time.sleep(1.0)
        led1.off()
        time.sleep(1.0)

except KeyboardInterrupt:
    led1.off()
    print("end")
```


### 2.2 디지털 입력으로 버튼 입력받기 71
회로연결 71  
스위치값 입력받기 72  
스위치를 누를 때만 출력하기 74  
스위치를 누르면 한 번만 출력하기 75  
이벤트 방식으로 여러 개의 버튼 입력받기 78  

### 2.3 PWM으로 RGB LED 제어하기 80
빨간색 LED의 밝기 조절하기 81  
RGB 모두 켜서 밝기 조절하기 82  
RGB 조절하여 무지개 색상 표현하기 84  
PWMOutputDevice 사용하기 86  

### 2.4 피에조 부저 출력하기 87
도레미파솔라시도 음 출력하기 88  
노래 출력하기 90  

### 2.5 아날로그 입력으로 센서값 입력받기 92
라즈베리파이 설정 93  
MPC3208 칩을 이용해서 아날로그 입력받기 94  
전압으로 환산하여 입력받기 95  
