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

* 2_2_1 스위치값 입력받기 72  

```
from gpiozero import Button
import time

SW1 = Button(5, pull_up=False)

try:
    while True:
        sw1_value = SW1.is_pressed
        print(sw1_value)
        time.sleep(0.1)

except KeyboardInterrupt:
    print("end")
```

* 2_2_2 스위치를 누를 때만 출력하기 74

```
  from gpiozero import Button
import time

SW1 = Button(5, pull_up=False)

old_value = 0
new_value = 0

try:
    while True:
        new_value = SW1.is_pressed
        if new_value != old_value:
            old_value = new_value
            print("click")
            time.sleep(0.2)

except KeyboardInterrupt:
    print("end")

```
* 2_2_3 스위치를 누르면 한 번만 출력하기 75  

```
from gpiozero import Button
import time

SW1 = Button(5, pull_up=False)

old_value = 0
new_value = 0

try:
    while True:
        new_value = SW1.is_pressed
        if new_value != old_value:
            old_value = new_value
            
            if new_value == 1:
                print("click")
            
            time.sleep(0.2)

except KeyboardInterrupt:
    print("end")


```

* 2_2_4 이벤트 방식으로 간단하게 버튼 입력받기 78  

```
from gpiozero import Button

SW1 = Button(5, pull_up=False)

def on_click():
    print("click")

SW1.when_pressed = on_click

try:
    while True :
        pass

except KeyboardInterrupt:
    print("end")
```

* 2_2_5 이벤트 방식으로 여러 개의 버튼 입력받기 78  

```
from gpiozero import Button

SW1 = Button(5, pull_up=False)
SW2 = Button(6, pull_up=False)
SW3 = Button(13, pull_up=False)
SW4 = Button(19, pull_up=False)

def handle_sw1():
    print("SW1 pressed")

def handle_sw2():
    print("SW2 pressed")

def handle_sw3():
    print("SW3 pressed")

def handle_sw4():
    print("SW4 pressed")

SW1.when_pressed = handle_sw1
SW2.when_pressed = handle_sw2
SW3.when_pressed = handle_sw3
SW4.when_pressed = handle_sw4

try:
    while True :
        pass

except KeyboardInterrupt:
    print("end")

```

### 2.3 PWM으로 RGB LED 제어하기 80

* 2_3_1 빨간색 LED의 밝기 조절하기 81 

```
from gpiozero import PWMLED
import time

led = PWMLED(10)  

try:
    while True:
        led.value = 0.0
        time.sleep(1.0)
        
        led.value = 0.3
        time.sleep(1.0)
        
        led.value = 0.6
        time.sleep(1.0)
        
        led.value = 1.0
        time.sleep(1.0)

except KeyboardInterrupt:
    led.off()
    print("end")

```

* 2_3_2 RGB 모두 켜서 밝기 조절하기 82

```
from gpiozero import PWMLED
import time

led_R = PWMLED(10)
led_G = PWMLED(9)
led_B = PWMLED(11)

try:
    while True:
        led_R.value = 0.0
        led_G.value = 0.0
        led_B.value = 0.0
        time.sleep(1.0)
        
        led_R.value = 0.5
        led_G.value = 0.5
        led_B.value = 0.5
        time.sleep(1.0)
        
        led_R.value = 1.0
        led_G.value = 1.0
        led_B.value = 1.0
        time.sleep(1.0)

except KeyboardInterrupt:
    led_R.off()
    led_G.off()
    led_B.off()
    print("end")


```

* 2_3_3 RGB 조절하여 무지개 색상 표현하기 84

```
from gpiozero import PWMLED
import time

led_R = PWMLED(10)
led_G = PWMLED(9)
led_B = PWMLED(11)

colors = [
    (1.0, 0.0, 0.0),  
    (1.0, 0.5, 0.0),  
    (1.0, 1.0, 0.0),  
    (0.0, 1.0, 0.0), 
    (0.0, 0.0, 1.0), 
    (0.3, 0.0, 0.5),  
    (0.6, 0.0, 1.0), 
]

try:
    while True:
        for r, g, b in colors:
            led_R.value = r
            led_G.value = g
            led_B.value = b
            time.sleep(1.0)

except KeyboardInterrupt:
    led_R.off()
    led_G.off()
    led_B.off()
    print("end")

```
 
* 2_3_4 PWMOutputDevice 사용하기 86  

```
from gpiozero import PWMOutputDevice
import time

led_R = PWMOutputDevice(10)

try:
    while True:
        led_R.value = 0.0 
        time.sleep(1)
        led_R.value = 0.5 
        time.sleep(1)
        led_R.value = 1.0 
        time.sleep(1)

except KeyboardInterrupt:
    led_R.off()
    print("end")

```


### 2.4 피에조 부저 출력하기 87
도레미파솔라시도 음 출력하기 88  
노래 출력하기 90  

### 2.5 아날로그 입력으로 센서값 입력받기 92
라즈베리파이 설정 93  
MPC3208 칩을 이용해서 아날로그 입력받기 94  
전압으로 환산하여 입력받기 95  
