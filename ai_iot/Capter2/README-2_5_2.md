# \# 📘 라즈베리파이로 만드는 인공지능과 사물인터넷  

# 

# \## 챕터2. 라즈베리파이 입출력 활용  

# 

# \### 2.1 디지털 출력으로 LED 제어하기 · 64  

# \- \[실습] 2\_1\_1 LED 1개 깜빡이기 · 64  

# \- \[실습] 2\_1\_2 안전하게 프로그램 종료하기 · 67  

# \- \[실습] 2\_1\_3 LED 여러 개 깜빡이기 · 68  

# \- \[실습] 2\_1\_4 값을 직접 입력하여 LED 켜고 끄기 · 69  

# \- \[실습] 2\_1\_5 GPIO를 제어하는 코드로 LED 켜고 끄기 · 70  

# 

# \---

# 

# \### 2.1 디지털 출력으로 LED 제어하기 64

# 

# ```

# J8:

# 🔴 3V3   (1)  (2)  🔴 5V

# 🟢 GPIO2 (3)  (4)  🔴 5V

# 🟢 GPIO3 (5)  (6)  ⚫ GND

# 👉🟢 GPIO4 (7)  (8)  🟢 GPIO14

# 👉⚫ GND   (9)  (10) 🟢 GPIO15

# 🟢 GPIO17 (11) (12) 🟢 GPIO18

# 🟢 GPIO27 (13) (14) ⚫ GND

# 🟢 GPIO22 (15) (16) 🟢 GPIO23

# 🔴 3V3  (17) (18) 🟢 GPIO24

# 🟢 GPIO10 (19) (20) ⚫ GND

# 🟢 GPIO9  (21) (22) 🟢 GPIO25

# 🟢 GPIO11 (23) (24) 🟢 GPIO8

# ⚫ GND  (25) (26) 🟢 GPIO7

# 🟢 GPIO0 (27) (28) 🟢 GPIO1

# 🟢 GPIO5 (29) (30) ⚫ GND

# 🟢 GPIO6 (31) (32) 🟢 GPIO12

# 🟢 GPIO13 (33) (34) ⚫ GND

# 🟢 GPIO19 (35) (36) 🟢 GPIO16

# 🟢 GPIO26 (37) (38) 🟢 GPIO20

# ⚫ GND  (39) (40) 🟢 GPIO21

# ```

# 

# \* 2\_1\_1 LED 1개 깜빡이기 64

# 

# ```

# python 2\_1\_1.py

# ```

# 

# ```

# from gpiozero import LED

# import time

# 

# led1 = LED(4)

# 

# while True :

# &#x20;   led1.on()

# &#x20;   time.sleep(1.0)

# &#x20;   led1.off()

# &#x20;   time.sleep(1.0)

# ```

# 

# \* 2\_1\_2 안전하게 프로그램 종료하기 67  

# 

# 

# ```

# J8:

# 🔴 3V3   (1)  (2)  🔴 5V

# 🟢 GPIO2 (3)  (4)  🔴 5V

# 🟢 GPIO3 (5)  (6)  ⚫ GND

# 👉🟢 GPIO4 (7)  (8)  🟢 GPIO14

# 👉⚫ GND   (9)  (10) 🟢 GPIO15

# 🟢 GPIO17 (11) (12) 🟢 GPIO18

# 🟢 GPIO27 (13) (14) ⚫ GND

# 🟢 GPIO22 (15) (16) 🟢 GPIO23

# 🔴 3V3  (17) (18) 🟢 GPIO24

# 🟢 GPIO10 (19) (20) ⚫ GND

# 🟢 GPIO9  (21) (22) 🟢 GPIO25

# 🟢 GPIO11 (23) (24) 🟢 GPIO8

# ⚫ GND  (25) (26) 🟢 GPIO7

# 🟢 GPIO0 (27) (28) 🟢 GPIO1

# 🟢 GPIO5 (29) (30) ⚫ GND

# 🟢 GPIO6 (31) (32) 🟢 GPIO12

# 🟢 GPIO13 (33) (34) ⚫ GND

# 🟢 GPIO19 (35) (36) 🟢 GPIO16

# 🟢 GPIO26 (37) (38) 🟢 GPIO20

# ⚫ GND  (39) (40) 🟢 GPIO21

# ```

# 

# ```

# python 2\_1\_2.py

# ```

# 

# ```

# from gpiozero import LED

# import time

# 

# led1 = LED(4)

# 

# try :

# &#x20;   while True :

# &#x20;       led1.on()

# &#x20;       time.sleep(1.0)

# &#x20;       led1.off()

# &#x20;       time.sleep(1.0)

# 

# except KeyboardInterrupt:

# &#x20;   led1.off()

# &#x20;   print("end")

# ```

# 

# \* 2\_1\_3 LED 여러 개 깜빡이기 68  

# 

# 

# ```

# J8:

# 🔴 3V3   (1)  (2)  🔴 5V

# 🟢 GPIO2 (3)  (4)  🔴 5V

# 🟢 GPIO3 (5)  (6)  ⚫ GND

# 👉🟢 GPIO4 (7)  (8)  🟢 GPIO14

# 👉⚫ GND   (9)  (10) 🟢 GPIO15

# 👉🟢 GPIO17 (11) (12) 🟢 GPIO18

# 👉🟢 GPIO27 (13) (14) ⚫ GND

# 👉🟢 GPIO22 (15) (16) 🟢 GPIO23

# 🔴 3V3  (17) (18) 🟢 GPIO24

# 🟢 GPIO10 (19) (20) ⚫ GND

# 🟢 GPIO9  (21) (22) 🟢 GPIO25

# 🟢 GPIO11 (23) (24) 🟢 GPIO8

# ⚫ GND  (25) (26) 🟢 GPIO7

# 🟢 GPIO0 (27) (28) 🟢 GPIO1

# 🟢 GPIO5 (29) (30) ⚫ GND

# 🟢 GPIO6 (31) (32) 🟢 GPIO12

# 🟢 GPIO13 (33) (34) ⚫ GND

# 🟢 GPIO19 (35) (36) 🟢 GPIO16

# 🟢 GPIO26 (37) (38) 🟢 GPIO20

# ⚫ GND  (39) (40) 🟢 GPIO21

# ```

# 

# ```

# python 2\_1\_3.py

# ```

# 

# ```

# from gpiozero import LED

# import time

# 

# led1 = LED(4)

# led2 = LED(17)

# led3 = LED(27)

# led4 = LED(22)

# 

# try :

# &#x20;   while True :

# &#x20;       led1.on()

# &#x20;       led2.on()

# &#x20;       led3.on()

# &#x20;       led4.on()

# &#x20;       time.sleep(1.0)

# &#x20;       led1.off()

# &#x20;       led2.off()

# &#x20;       led3.off()

# &#x20;       led4.off()

# &#x20;       time.sleep(1.0)

# 

# except KeyboardInterrupt:

# &#x20;   led1.off()

# &#x20;   led2.off()

# &#x20;   led3.off()

# &#x20;   led4.off()

# &#x20;   print("end")

# 

# ```

# 

# \* 2\_1\_4 값을 직접 입력하여 LED 켜고 끄기 69  

# 

# ```

# J8:

# 🔴 3V3   (1)  (2)  🔴 5V

# 🟢 GPIO2 (3)  (4)  🔴 5V

# 🟢 GPIO3 (5)  (6)  ⚫ GND

# 👉🟢 GPIO4 (7)  (8)  🟢 GPIO14

# 👉⚫ GND   (9)  (10) 🟢 GPIO15

# 🟢 GPIO17 (11) (12) 🟢 GPIO18

# 🟢 GPIO27 (13) (14) ⚫ GND

# 🟢 GPIO22 (15) (16) 🟢 GPIO23

# 🔴 3V3  (17) (18) 🟢 GPIO24

# 🟢 GPIO10 (19) (20) ⚫ GND

# 🟢 GPIO9  (21) (22) 🟢 GPIO25

# 🟢 GPIO11 (23) (24) 🟢 GPIO8

# ⚫ GND  (25) (26) 🟢 GPIO7

# 🟢 GPIO0 (27) (28) 🟢 GPIO1

# 🟢 GPIO5 (29) (30) ⚫ GND

# 🟢 GPIO6 (31) (32) 🟢 GPIO12

# 🟢 GPIO13 (33) (34) ⚫ GND

# 🟢 GPIO19 (35) (36) 🟢 GPIO16

# 🟢 GPIO26 (37) (38) 🟢 GPIO20

# ⚫ GND  (39) (40) 🟢 GPIO21

# ```

# 

# ```

# python 2\_1\_4.py

# ```

# 

# ```

# from gpiozero import LED

# import time

# 

# led1 = LED(4)

# 

# try :

# &#x20;   while True :

# &#x20;       led1.value = 1

# &#x20;       time.sleep(1.0)

# &#x20;       led1.value = 0

# &#x20;       time.sleep(1.0)

# 

# except KeyboardInterrupt:

# &#x20;   led1.value = 0

# &#x20;   print("end")

# 

# ```

# 

# \* 2\_1\_5 GPIO를 제어하는 코드로 LED 켜고 끄기 70  

# 

# ```

# J8:

# 🔴 3V3   (1)  (2)  🔴 5V

# 🟢 GPIO2 (3)  (4)  🔴 5V

# 🟢 GPIO3 (5)  (6)  ⚫ GND

# 👉🟢 GPIO4 (7)  (8)  🟢 GPIO14

# 👉⚫ GND   (9)  (10) 🟢 GPIO15

# 🟢 GPIO17 (11) (12) 🟢 GPIO18

# 🟢 GPIO27 (13) (14) ⚫ GND

# 🟢 GPIO22 (15) (16) 🟢 GPIO23

# 🔴 3V3  (17) (18) 🟢 GPIO24

# 🟢 GPIO10 (19) (20) ⚫ GND

# 🟢 GPIO9  (21) (22) 🟢 GPIO25

# 🟢 GPIO11 (23) (24) 🟢 GPIO8

# ⚫ GND  (25) (26) 🟢 GPIO7

# 🟢 GPIO0 (27) (28) 🟢 GPIO1

# 🟢 GPIO5 (29) (30) ⚫ GND

# 🟢 GPIO6 (31) (32) 🟢 GPIO12

# 🟢 GPIO13 (33) (34) ⚫ GND

# 🟢 GPIO19 (35) (36) 🟢 GPIO16

# 🟢 GPIO26 (37) (38) 🟢 GPIO20

# ⚫ GND  (39) (40) 🟢 GPIO21

# ```

# 

# ```

# python 2\_1\_5.py

# ```

# 

# ```

# from gpiozero import OutputDevice

# import time

# 

# led1 = OutputDevice(4)

# 

# try:

# &#x20;   while True:

# &#x20;       led1.on()

# &#x20;       time.sleep(1.0)

# &#x20;       led1.off()

# &#x20;       time.sleep(1.0)

# 

# except KeyboardInterrupt:

# &#x20;   led1.off()

# &#x20;   print("end")

# ```

# \---

# 

# \### 2.2 디지털 입력으로 버튼 입력받기 · 71  

# \- 회로연결 · 71  

# \- \[실습] 2\_2\_1 스위치값 입력받기 · 72  

# \- \[실습] 2\_2\_2 스위치를 누를 때만 출력하기 · 74  

# \- \[실습] 2\_2\_3 스위치를 누르면 한 번만 출력하기 · 75  

# \- \[실습] 2\_2\_4 이벤트 방식으로 간단하게 버튼 입력받기 · 78  

# \- 2\_2\_5 이벤트 방식으로 여러 개의 버튼 입력받기 · 78  

# 

# \---

# 

# \### 2.2 디지털 입력으로 버튼 입력받기 71

# 회로연결 71  

# 

# \* 2\_2\_1 스위치값 입력받기 72  

# 

# ```

# J8:

# 🔴 3V3   (1)  (2)  🔴 5V

# 🟢 GPIO2 (3)  (4)  🔴 5V

# 🟢 GPIO3 (5)  (6)  ⚫ GND

# 🟢 GPIO4 (7)  (8)  🟢 GPIO14

# 👉⚫ GND   (9)  (10) 🟢 GPIO15

# 🟢 GPIO17 (11) (12) 🟢 GPIO18

# 🟢 GPIO27 (13) (14) ⚫ GND

# 🟢 GPIO22 (15) (16) 🟢 GPIO23

# 🔴 3V3  (17) (18) 🟢 GPIO24

# 🟢 GPIO10 (19) (20) ⚫ GND

# 🟢 GPIO9  (21) (22) 🟢 GPIO25

# 🟢 GPIO11 (23) (24) 🟢 GPIO8

# ⚫ GND  (25) (26) 🟢 GPIO7

# 🟢 GPIO0 (27) (28) 🟢 GPIO1

# 👉🟢 GPIO5 (29) (30) ⚫ GND

# 🟢 GPIO6 (31) (32) 🟢 GPIO12

# 🟢 GPIO13 (33) (34) ⚫ GND

# 🟢 GPIO19 (35) (36) 🟢 GPIO16

# 🟢 GPIO26 (37) (38) 🟢 GPIO20

# ⚫ GND  (39) (40) 🟢 GPIO21

# ```

# 

# ```

# python 2\_2\_1.py

# ```

# 

# ```

# from gpiozero import Button

# import time

# 

# SW1 = Button(5, pull\_up=False)

# 

# try:

# &#x20;   while True:

# &#x20;       sw1\_value = SW1.is\_pressed

# &#x20;       print(sw1\_value)

# &#x20;       time.sleep(0.1)

# 

# except KeyboardInterrupt:

# &#x20;   print("end")

# ```

# 

# \* 2\_2\_2 스위치를 누를 때만 출력하기 74

# 

# ```

# J8:

# 🔴 3V3   (1)  (2)  🔴 5V

# 🟢 GPIO2 (3)  (4)  🔴 5V

# 🟢 GPIO3 (5)  (6)  ⚫ GND

# 🟢 GPIO4 (7)  (8)  🟢 GPIO14

# 👉⚫ GND   (9)  (10) 🟢 GPIO15

# 🟢 GPIO17 (11) (12) 🟢 GPIO18

# 🟢 GPIO27 (13) (14) ⚫ GND

# 🟢 GPIO22 (15) (16) 🟢 GPIO23

# 🔴 3V3  (17) (18) 🟢 GPIO24

# 🟢 GPIO10 (19) (20) ⚫ GND

# 🟢 GPIO9  (21) (22) 🟢 GPIO25

# 🟢 GPIO11 (23) (24) 🟢 GPIO8

# ⚫ GND  (25) (26) 🟢 GPIO7

# 🟢 GPIO0 (27) (28) 🟢 GPIO1

# 👉🟢 GPIO5 (29) (30) ⚫ GND

# 🟢 GPIO6 (31) (32) 🟢 GPIO12

# 🟢 GPIO13 (33) (34) ⚫ GND

# 🟢 GPIO19 (35) (36) 🟢 GPIO16

# 🟢 GPIO26 (37) (38) 🟢 GPIO20

# ⚫ GND  (39) (40) 🟢 GPIO21

# ```

# 

# ```

# python 2\_2\_2.py

# ```

# 

# ```

# &#x20; from gpiozero import Button

# import time

# 

# SW1 = Button(5, pull\_up=False)

# 

# old\_value = 0

# new\_value = 0

# 

# try:

# &#x20;   while True:

# &#x20;       new\_value = SW1.is\_pressed

# &#x20;       if new\_value != old\_value:

# &#x20;           old\_value = new\_value

# &#x20;           print("click")

# &#x20;           time.sleep(0.2)

# 

# except KeyboardInterrupt:

# &#x20;   print("end")

# 

# ```

# \* 2\_2\_3 스위치를 누르면 한 번만 출력하기 75  

# 

# ```

# J8:

# 🔴 3V3   (1)  (2)  🔴 5V

# 🟢 GPIO2 (3)  (4)  🔴 5V

# 🟢 GPIO3 (5)  (6)  ⚫ GND

# 🟢 GPIO4 (7)  (8)  🟢 GPIO14

# 👉⚫ GND   (9)  (10) 🟢 GPIO15

# 🟢 GPIO17 (11) (12) 🟢 GPIO18

# 🟢 GPIO27 (13) (14) ⚫ GND

# 🟢 GPIO22 (15) (16) 🟢 GPIO23

# 🔴 3V3  (17) (18) 🟢 GPIO24

# 🟢 GPIO10 (19) (20) ⚫ GND

# 🟢 GPIO9  (21) (22) 🟢 GPIO25

# 🟢 GPIO11 (23) (24) 🟢 GPIO8

# ⚫ GND  (25) (26) 🟢 GPIO7

# 🟢 GPIO0 (27) (28) 🟢 GPIO1

# 👉🟢 GPIO5 (29) (30) ⚫ GND

# 🟢 GPIO6 (31) (32) 🟢 GPIO12

# 🟢 GPIO13 (33) (34) ⚫ GND

# 🟢 GPIO19 (35) (36) 🟢 GPIO16

# 🟢 GPIO26 (37) (38) 🟢 GPIO20

# ⚫ GND  (39) (40) 🟢 GPIO21

# ```

# 

# ```

# python 2\_2\_3.py

# ```

# 

# ```

# from gpiozero import Button

# import time

# 

# SW1 = Button(5, pull\_up=False)

# 

# old\_value = 0

# new\_value = 0

# 

# try:

# &#x20;   while True:

# &#x20;       new\_value = SW1.is\_pressed

# &#x20;       if new\_value != old\_value:

# &#x20;           old\_value = new\_value

# &#x20;           

# &#x20;           if new\_value == 1:

# &#x20;               print("click")

# &#x20;           

# &#x20;           time.sleep(0.2)

# 

# except KeyboardInterrupt:

# &#x20;   print("end")

# 

# 

# ```

# 

# \* 2\_2\_4 이벤트 방식으로 간단하게 버튼 입력받기 78  

# 

# ```

# J8:

# 🔴 3V3   (1)  (2)  🔴 5V

# 🟢 GPIO2 (3)  (4)  🔴 5V

# 🟢 GPIO3 (5)  (6)  ⚫ GND

# 🟢 GPIO4 (7)  (8)  🟢 GPIO14

# 👉⚫ GND   (9)  (10) 🟢 GPIO15

# 🟢 GPIO17 (11) (12) 🟢 GPIO18

# 🟢 GPIO27 (13) (14) ⚫ GND

# 🟢 GPIO22 (15) (16) 🟢 GPIO23

# 🔴 3V3  (17) (18) 🟢 GPIO24

# 🟢 GPIO10 (19) (20) ⚫ GND

# 🟢 GPIO9  (21) (22) 🟢 GPIO25

# 🟢 GPIO11 (23) (24) 🟢 GPIO8

# ⚫ GND  (25) (26) 🟢 GPIO7

# 🟢 GPIO0 (27) (28) 🟢 GPIO1

# 👉🟢 GPIO5 (29) (30) ⚫ GND

# 🟢 GPIO6 (31) (32) 🟢 GPIO12

# 🟢 GPIO13 (33) (34) ⚫ GND

# 🟢 GPIO19 (35) (36) 🟢 GPIO16

# 🟢 GPIO26 (37) (38) 🟢 GPIO20

# ⚫ GND  (39) (40) 🟢 GPIO21

# ```

# 

# ```

# python 2\_2\_4.py

# ```

# 

# ```

# from gpiozero import Button

# 

# SW1 = Button(5, pull\_up=False)

# 

# def on\_click():

# &#x20;   print("click")

# 

# SW1.when\_pressed = on\_click

# 

# try:

# &#x20;   while True :

# &#x20;       pass

# 

# except KeyboardInterrupt:

# &#x20;   print("end")

# ```

# 

# \* 2\_2\_5 이벤트 방식으로 여러 개의 버튼 입력받기 78  

# 

# ```

# J8:

# 🔴 3V3   (1)  (2)  🔴 5V

# 🟢 GPIO2 (3)  (4)  🔴 5V

# 🟢 GPIO3 (5)  (6)  ⚫ GND

# 🟢 GPIO4 (7)  (8)  🟢 GPIO14

# 👉⚫ GND   (9)  (10) 🟢 GPIO15

# 🟢 GPIO17 (11) (12) 🟢 GPIO18

# 🟢 GPIO27 (13) (14) ⚫ GND

# 🟢 GPIO22 (15) (16) 🟢 GPIO23

# 🔴 3V3  (17) (18) 🟢 GPIO24

# 🟢 GPIO10 (19) (20) ⚫ GND

# 🟢 GPIO9  (21) (22) 🟢 GPIO25

# 🟢 GPIO11 (23) (24) 🟢 GPIO8

# ⚫ GND  (25) (26) 🟢 GPIO7

# 🟢 GPIO0 (27) (28) 🟢 GPIO1

# 👉🟢 GPIO5 (29) (30) ⚫ GND

# 👉🟢 GPIO6 (31) (32) 🟢 GPIO12

# 👉🟢 GPIO13 (33) (34) ⚫ GND

# 👉🟢 GPIO19 (35) (36) 🟢 GPIO16

# 🟢 GPIO26 (37) (38) 🟢 GPIO20

# ⚫ GND  (39) (40) 🟢 GPIO21

# ```

# 

# ```

# python 2\_2\_5.py

# ```

# 

# ```

# from gpiozero import Button

# 

# SW1 = Button(5, pull\_up=False)

# SW2 = Button(6, pull\_up=False)

# SW3 = Button(13, pull\_up=False)

# SW4 = Button(19, pull\_up=False)

# 

# def handle\_sw1():

# &#x20;   print("SW1 pressed")

# 

# def handle\_sw2():

# &#x20;   print("SW2 pressed")

# 

# def handle\_sw3():

# &#x20;   print("SW3 pressed")

# 

# def handle\_sw4():

# &#x20;   print("SW4 pressed")

# 

# SW1.when\_pressed = handle\_sw1

# SW2.when\_pressed = handle\_sw2

# SW3.when\_pressed = handle\_sw3

# SW4.when\_pressed = handle\_sw4

# 

# try:

# &#x20;   while True :

# &#x20;       pass

# 

# except KeyboardInterrupt:

# &#x20;   print("end")

# 

# ```

# 

# \---

# \### 2.3 PWM으로 RGB LED 제어하기 · 80  

# \- \[실습] 2\_3\_1 빨간색 LED의 밝기 조절하기 · 81  

# \- \[실습] 2\_3\_2 RGB 모두 켜서 밝기 조절하기 · 82  

# \- \[실습] 2\_3\_3 RGB 조절하여 무지개 색상 표현하기 · 84  

# \- \[실습] 2\_3\_4 PWMOutputDevice 사용하기 · 86  

# 

# \---

# 

# \### 2.3 PWM으로 RGB LED 제어하기 80

# 

# \* 2\_3\_1 빨간색 LED의 밝기 조절하기 81 

# 

# ```

# J8:

# 🔴 3V3   (1)  (2)  🔴 5V

# 🟢 GPIO2 (3)  (4)  🔴 5V

# 🟢 GPIO3 (5)  (6)  ⚫ GND

# 🟢 GPIO4 (7)  (8)  🟢 GPIO14

# 👉⚫ GND   (9)  (10) 🟢 GPIO15

# 🟢 GPIO17 (11) (12) 🟢 GPIO18

# 🟢 GPIO27 (13) (14) ⚫ GND

# 🟢 GPIO22 (15) (16) 🟢 GPIO23

# 🔴 3V3  (17) (18) 🟢 GPIO24

# 👉🟢 GPIO10 (19) (20) ⚫ GND

# 🟢 GPIO9  (21) (22) 🟢 GPIO25

# 🟢 GPIO11 (23) (24) 🟢 GPIO8

# ⚫ GND  (25) (26) 🟢 GPIO7

# 🟢 GPIO0 (27) (28) 🟢 GPIO1

# 🟢 GPIO5 (29) (30) ⚫ GND

# 🟢 GPIO6 (31) (32) 🟢 GPIO12

# 🟢 GPIO13 (33) (34) ⚫ GND

# 🟢 GPIO19 (35) (36) 🟢 GPIO16

# 🟢 GPIO26 (37) (38) 🟢 GPIO20

# ⚫ GND  (39) (40) 🟢 GPIO21

# ```

# 

# ```

# python 2\_3\_1.py

# ```

# 

# ```

# from gpiozero import PWMLED

# import time

# 

# led = PWMLED(10)  

# 

# try:

# &#x20;   while True:

# &#x20;       led.value = 0.0

# &#x20;       time.sleep(1.0)

# &#x20;       

# &#x20;       led.value = 0.3

# &#x20;       time.sleep(1.0)

# &#x20;       

# &#x20;       led.value = 0.6

# &#x20;       time.sleep(1.0)

# &#x20;       

# &#x20;       led.value = 1.0

# &#x20;       time.sleep(1.0)

# 

# except KeyboardInterrupt:

# &#x20;   led.off()

# &#x20;   print("end")

# 

# ```

# 

# \* 2\_3\_2 RGB 모두 켜서 밝기 조절하기 82

# 

# ```

# J8:

# 🔴 3V3   (1)  (2)  🔴 5V

# 🟢 GPIO2 (3)  (4)  🔴 5V

# 🟢 GPIO3 (5)  (6)  ⚫ GND

# 🟢 GPIO4 (7)  (8)  🟢 GPIO14

# 👉⚫ GND   (9)  (10) 🟢 GPIO15

# 🟢 GPIO17 (11) (12) 🟢 GPIO18

# 🟢 GPIO27 (13) (14) ⚫ GND

# 🟢 GPIO22 (15) (16) 🟢 GPIO23

# 🔴 3V3  (17) (18) 🟢 GPIO24

# 👉🟢 GPIO10 (19) (20) ⚫ GND

# 👉🟢 GPIO9  (21) (22) 🟢 GPIO25

# 👉🟢 GPIO11 (23) (24) 🟢 GPIO8

# ⚫ GND  (25) (26) 🟢 GPIO7

# 🟢 GPIO0 (27) (28) 🟢 GPIO1

# 🟢 GPIO5 (29) (30) ⚫ GND

# 🟢 GPIO6 (31) (32) 🟢 GPIO12

# 🟢 GPIO13 (33) (34) ⚫ GND

# 🟢 GPIO19 (35) (36) 🟢 GPIO16

# 🟢 GPIO26 (37) (38) 🟢 GPIO20

# ⚫ GND  (39) (40) 🟢 GPIO21

# ```

# 

# ```

# python 2\_3\_2.py

# ```

# 

# ```

# from gpiozero import PWMLED

# import time

# 

# led\_R = PWMLED(10)

# led\_G = PWMLED(9)

# led\_B = PWMLED(11)

# 

# try:

# &#x20;   while True:

# &#x20;       led\_R.value = 0.0

# &#x20;       led\_G.value = 0.0

# &#x20;       led\_B.value = 0.0

# &#x20;       time.sleep(1.0)

# &#x20;       

# &#x20;       led\_R.value = 0.5

# &#x20;       led\_G.value = 0.5

# &#x20;       led\_B.value = 0.5

# &#x20;       time.sleep(1.0)

# &#x20;       

# &#x20;       led\_R.value = 1.0

# &#x20;       led\_G.value = 1.0

# &#x20;       led\_B.value = 1.0

# &#x20;       time.sleep(1.0)

# 

# except KeyboardInterrupt:

# &#x20;   led\_R.off()

# &#x20;   led\_G.off()

# &#x20;   led\_B.off()

# &#x20;   print("end")

# 

# 

# ```

# 

# \* 2\_3\_3 RGB 조절하여 무지개 색상 표현하기 84

# 

# ```

# J8:

# 🔴 3V3   (1)  (2)  🔴 5V

# 🟢 GPIO2 (3)  (4)  🔴 5V

# 🟢 GPIO3 (5)  (6)  ⚫ GND

# 🟢 GPIO4 (7)  (8)  🟢 GPIO14

# 👉⚫ GND   (9)  (10) 🟢 GPIO15

# 🟢 GPIO17 (11) (12) 🟢 GPIO18

# 🟢 GPIO27 (13) (14) ⚫ GND

# 🟢 GPIO22 (15) (16) 🟢 GPIO23

# 🔴 3V3  (17) (18) 🟢 GPIO24

# 👉🟢 GPIO10 (19) (20) ⚫ GND

# 👉🟢 GPIO9  (21) (22) 🟢 GPIO25

# 👉🟢 GPIO11 (23) (24) 🟢 GPIO8

# ⚫ GND  (25) (26) 🟢 GPIO7

# 🟢 GPIO0 (27) (28) 🟢 GPIO1

# 🟢 GPIO5 (29) (30) ⚫ GND

# 🟢 GPIO6 (31) (32) 🟢 GPIO12

# 🟢 GPIO13 (33) (34) ⚫ GND

# 🟢 GPIO19 (35) (36) 🟢 GPIO16

# 🟢 GPIO26 (37) (38) 🟢 GPIO20

# ⚫ GND  (39) (40) 🟢 GPIO21

# ```

# 

# ```

# python 2\_3\_3.py

# ```

# 

# ```

# from gpiozero import PWMLED

# import time

# 

# led\_R = PWMLED(10)

# led\_G = PWMLED(9)

# led\_B = PWMLED(11)

# 

# colors = \[

# &#x20;   (1.0, 0.0, 0.0),  

# &#x20;   (1.0, 0.5, 0.0),  

# &#x20;   (1.0, 1.0, 0.0),  

# &#x20;   (0.0, 1.0, 0.0), 

# &#x20;   (0.0, 0.0, 1.0), 

# &#x20;   (0.3, 0.0, 0.5),  

# &#x20;   (0.6, 0.0, 1.0), 

# ]

# 

# try:

# &#x20;   while True:

# &#x20;       for r, g, b in colors:

# &#x20;           led\_R.value = r

# &#x20;           led\_G.value = g

# &#x20;           led\_B.value = b

# &#x20;           time.sleep(1.0)

# 

# except KeyboardInterrupt:

# &#x20;   led\_R.off()

# &#x20;   led\_G.off()

# &#x20;   led\_B.off()

# &#x20;   print("end")

# 

# ```

# &#x20;

# \* 2\_3\_4 PWMOutputDevice 사용하기 86  

# 

# ```

# J8:

# 🔴 3V3   (1)  (2)  🔴 5V

# 🟢 GPIO2 (3)  (4)  🔴 5V

# 🟢 GPIO3 (5)  (6)  ⚫ GND

# 🟢 GPIO4 (7)  (8)  🟢 GPIO14

# 👉⚫ GND   (9)  (10) 🟢 GPIO15

# 🟢 GPIO17 (11) (12) 🟢 GPIO18

# 🟢 GPIO27 (13) (14) ⚫ GND

# 🟢 GPIO22 (15) (16) 🟢 GPIO23

# 🔴 3V3  (17) (18) 🟢 GPIO24

# 👉🟢 GPIO10 (19) (20) ⚫ GND

# 🟢 GPIO9  (21) (22) 🟢 GPIO25

# 🟢 GPIO11 (23) (24) 🟢 GPIO8

# ⚫ GND  (25) (26) 🟢 GPIO7

# 🟢 GPIO0 (27) (28) 🟢 GPIO1

# 🟢 GPIO5 (29) (30) ⚫ GND

# 🟢 GPIO6 (31) (32) 🟢 GPIO12

# 🟢 GPIO13 (33) (34) ⚫ GND

# 🟢 GPIO19 (35) (36) 🟢 GPIO16

# 🟢 GPIO26 (37) (38) 🟢 GPIO20

# ⚫ GND  (39) (40) 🟢 GPIO21

# ```

# 

# ```

# python 2\_3\_4.py

# ```

# 

# ```

# from gpiozero import PWMOutputDevice

# import time

# 

# led\_R = PWMOutputDevice(10)

# 

# try:

# &#x20;   while True:

# &#x20;       led\_R.value = 0.0 

# &#x20;       time.sleep(1)

# &#x20;       led\_R.value = 0.5 

# &#x20;       time.sleep(1)

# &#x20;       led\_R.value = 1.0 

# &#x20;       time.sleep(1)

# 

# except KeyboardInterrupt:

# &#x20;   led\_R.off()

# &#x20;   print("end")

# 

# ```

# 

# \---

# \### 2.4 피에조 부저 출력하기 · 87  

# \- \[실습] 2\_4\_1 도레미파솔라시도 음 출력하기 · 88  

# \- \[실습] 2\_4\_2 노래 출력하기 · 90  

# 

# \---

# 

# \### 2.4 피에조 부저 출력하기 87

# \* 2\_4\_1 도레미파솔라시도 음 출력하기 88

# 

# ```

# J8:

# 🔴 3V3   (1)  (2)  🔴 5V

# 🟢 GPIO2 (3)  (4)  🔴 5V

# 🟢 GPIO3 (5)  (6)  ⚫ GND

# 🟢 GPIO4 (7)  (8)  🟢 GPIO14

# 👉⚫ GND   (9)  (10) 🟢 GPIO15

# 🟢 GPIO17 (11) (12) 👉🟢 GPIO18

# 🟢 GPIO27 (13) (14) ⚫ GND

# 🟢 GPIO22 (15) (16) 🟢 GPIO23

# 🔴 3V3  (17) (18) 🟢 GPIO24

# 🟢 GPIO10 (19) (20) ⚫ GND

# 🟢 GPIO9  (21) (22) 🟢 GPIO25

# 🟢 GPIO11 (23) (24) 🟢 GPIO8

# ⚫ GND  (25) (26) 🟢 GPIO7

# 🟢 GPIO0 (27) (28) 🟢 GPIO1

# 🟢 GPIO5 (29) (30) ⚫ GND

# 🟢 GPIO6 (31) (32) 🟢 GPIO12

# 🟢 GPIO13 (33) (34) ⚫ GND

# 🟢 GPIO19 (35) (36) 🟢 GPIO16

# 🟢 GPIO26 (37) (38) 🟢 GPIO20

# ⚫ GND  (39) (40) 🟢 GPIO21

# ```

# 

# ```

# python 2\_4\_1.py

# ```

# 

# ```

# from gpiozero import PWMOutputDevice

# from time import sleep

# 

# buzzer = PWMOutputDevice(18)

# 

# notes = {

# &#x20;   "do": 261,

# &#x20;   "re": 293,

# &#x20;   "mi": 329,

# &#x20;   "fa": 349,

# &#x20;   "sol": 392,

# &#x20;   "la": 440,

# &#x20;   "si": 493,

# &#x20;   "do'": 523

# }

# 

# try:

# &#x20;   for name, freq in notes.items():

# &#x20;       print(name)

# &#x20;       buzzer.frequency = freq

# &#x20;       buzzer.value = 0.5

# &#x20;       sleep(0.5)

# &#x20;       buzzer.value = 0

# &#x20;       sleep(0.05)

# 

# except KeyboardInterrupt:

# &#x20;   buzzer.off()

# &#x20;   print("end")

# 

# ```

# 

# \* 2\_4\_2 노래 출력하기 90  

# 

# ```

# J8:

# 🔴 3V3   (1)  (2)  🔴 5V

# 🟢 GPIO2 (3)  (4)  🔴 5V

# 🟢 GPIO3 (5)  (6)  ⚫ GND

# 🟢 GPIO4 (7)  (8)  🟢 GPIO14

# 👉⚫ GND   (9)  (10) 🟢 GPIO15

# 🟢 GPIO17 (11) (12) 👉🟢 GPIO18

# 🟢 GPIO27 (13) (14) ⚫ GND

# 🟢 GPIO22 (15) (16) 🟢 GPIO23

# 🔴 3V3  (17) (18) 🟢 GPIO24

# 🟢 GPIO10 (19) (20) ⚫ GND

# 🟢 GPIO9  (21) (22) 🟢 GPIO25

# 🟢 GPIO11 (23) (24) 🟢 GPIO8

# ⚫ GND  (25) (26) 🟢 GPIO7

# 🟢 GPIO0 (27) (28) 🟢 GPIO1

# 🟢 GPIO5 (29) (30) ⚫ GND

# 🟢 GPIO6 (31) (32) 🟢 GPIO12

# 🟢 GPIO13 (33) (34) ⚫ GND

# 🟢 GPIO19 (35) (36) 🟢 GPIO16

# 🟢 GPIO26 (37) (38) 🟢 GPIO20

# ⚫ GND  (39) (40) 🟢 GPIO21

# ```

# 

# ```

# python 2\_4\_2.py

# ```

# 

# ```

# from gpiozero import PWMOutputDevice

# from time import sleep

# 

# buzzer = PWMOutputDevice(18)

# 

# notes = {

# &#x20;   "C": 261,

# &#x20;   "D": 293,

# &#x20;   "E": 329,

# &#x20;   "F": 349,

# &#x20;   "G": 392,

# &#x20;   "A": 440,

# &#x20;   "B": 493,

# &#x20;   "C5": 523,

# &#x20;   " ": 0

# }

# 

# melody = \[

# &#x20;   "C", "C", "G", "G", "A", "A", "G", " ",

# &#x20;   "F", "F", "E", "E", "D", "D", "C", " ",

# &#x20;   "G", "G", "F", "F", "E", "E", "D", " ",

# &#x20;   "G", "G", "F", "F", "E", "E", "D", " ",

# &#x20;   "C", "C", "G", "G", "A", "A", "G", " ",

# &#x20;   "F", "F", "E", "E", "D", "D", "C"

# ]

# 

# try:

# &#x20;   for note in melody:

# &#x20;       freq = notes\[note]

# &#x20;       if freq == 0:

# &#x20;           buzzer.value = 0

# &#x20;       else:

# &#x20;           buzzer.frequency = freq

# &#x20;           buzzer.value = 0.5

# &#x20;       sleep(0.4)

# &#x20;       buzzer.value = 0

# &#x20;       sleep(0.05)

# 

# except KeyboardInterrupt:

# &#x20;   buzzer.off()

# &#x20;   print("end")

# 

# ```

# 

# \---

# 

# \### 2.5 아날로그 입력으로 센서값 입력받기 · 92  

# \- \[실습X] 2\_5\_1 라즈베리파이 설정 · 93  

# \- \[실습X] 2\_5\_2 MPC3208 칩을 이용해서 아날로그 입력받기 · 94  

# \- \[실습X] 2\_5\_3 전압으로 환산하여 입력받기 · 95  

# 

# \---

# 

# 

# \### 2.5 아날로그 입력으로 센서값 입력받기 92

# 

# \* 2\_5\_1 라즈베리파이 설정 93  

# 

# \* 2\_5\_2 MPC3208 칩을 이용해서 아날로그 입력받기 94  

# 

# ```

# python 2\_5\_1.py

# ```

# 

# ```

# from gpiozero import MCP3208

# import time

# 

# cds = MCP3208(channel=0)

# 

# try:

# &#x20;   while 1:

# &#x20;       cds\_value = cds.value \* 100

# &#x20;       print(cds\_value)

# &#x20;       time.sleep(0.2)

# &#x20;       

# except KeyboardInterrupt:

# &#x20;   pass

# ```

# 

# \* 2\_5\_3 전압으로 환산하여 입력받기

# 

# ```

# python 2\_5\_2.py

# ```

# 

# ```

# from gpiozero import MCP3208

# import time

# 

# cds = MCP3208(channel=0)

# 

# try:

# &#x20;   while 1:

# &#x20;       cds\_value = cds.value \* 3.3

# &#x20;       print(cds\_value)

# &#x20;       time.sleep(0.2)

# &#x20;       

# except KeyboardInterrupt:

# &#x20;   pass

# ```

# 

# 

# 



