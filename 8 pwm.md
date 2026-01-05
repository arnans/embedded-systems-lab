# Lab 6: Pulse Width Modulation (PWM) ด้วย ESP32

## สารบัญ (Table of Contents)

- [การส่งงาน](#overview)
- [Lab 6.1: หรี่ไฟ LED](#lab6-1-led)
  - [โจทย์](#lab6-1-challenge)
  - [ตัวอย่างโค้ด PWM บน ESP32](#lab6-1-example-code)
- [Lab 6.2: ควบคุม Servo Motor ผ่าน Library](#lab6-2-servo-library)
  - [Servo Pinout](#servo-pinout)
  - [ตัวอย่างโค้ด (ESP32Servo)](#lab6-2-example-code)
- [Lab 6.3: ควบคุม Servo Motor ด้วยการสร้าง PWM เอง](#lab6-3-servo-manual-pwm)
  - [หลักการ](#lab6-3-principles)

---

<a id="overview"></a>
## การส่งงาน

### Lab 6.1 หรี่ไฟ

- เลือกแสดงรูป pulse ที่ความสว่าง 2 ระดับ (เช่นระดับที่ duty ค่อนข้างสูง และระดับที่ค่อนข้างต่ำ)
- ใช้ Logic Analyzer วัด ความถี่และ duty ของสัญญาณ PWM
- อธิบายหลักการ PWM ที่ได้เรียนรู้ใน Lab นี้

### Lab 6.3 สร้าง PWM เอง เพื่อคุม Servo Motor 

- Lab 6.2 ไม่ต้องส่ง
- แสดงรูป pulse ที่ใช้ควบคุม servo โดยเลือกแสดงที่องศามากและน้อยที่สุด
- แสดงภาพ servo ขณะทำงานตาก pulse ข้างต้น
- ใช้ Logic Analyzer วัดความกว้าง pulse
- อธิบายความรู้ PWM ที่ได้รับใน lab นี้

---


<a id="lab6-1-led"></a>
## Lab 6.1: หรี่ไฟ LED

<a id="lab6-1-challenge"></a>
### โจทย์

- ควบคุมความสว่างของ LED ด้วยปุ่มกด  
- มีอย่างน้อย 5 ระดับ  
- ระดับต่ำสุด = Duty 0%  
- ระดับสูงสุด = Duty 100%

<a id="lab6-1-example-code"></a>
### ตัวอย่างโค้ด PWM บน ESP32

```c
const int ledPin = 16;   // GPIO16
const int freq = 1000;  // Hz
const int resolution = 8;

void setup() {
  ledcAttach(ledPin, freq, resolution);
}

void loop() {
  for (int duty = 0; duty <= 255; duty++) {
    ledcWrite(ledPin, duty);
    delay(15);
  }

  for (int duty = 255; duty >= 0; duty--) {
    ledcWrite(ledPin, duty);
    delay(15);
  }
}
```

ESP32 สามารถสร้าง PWM ได้โดยไม่ต้องใช้ Library เพิ่มเติม  
ขั้นตอนหลักคือ

1. เลือก GPIO ที่รองรับ PWM  
2. ผูก GPIO กับ PWM Channel พร้อมกำหนดความถี่และความละเอียด  
3. กำหนดค่า Duty

![ESP32 PWM Pins](/images/ESP32-PWM-Pins.png)

> GPIO ที่รองรับ PWM

---

<a id="lab6-2-servo-library"></a>
## Lab 6.2: ควบคุม Servo Motor ผ่าน Library

[![Watch on YouTube](https://img.youtube.com/vi/apVR5Htz0K4/maxresdefault.jpg)](https://www.youtube.com/watch?v=apVR5Htz0K4)
> YouTube Video  
> Click to play

[![Watch on YouTube](https://img.youtube.com/vi/jK4Lf9QVRE0/maxresdefault.jpg)](https://www.youtube.com/watch?v=jK4Lf9QVRE0)
> YouTube Video  
> Click to play

<a id="servo-pinout"></a>
### Servo Pinout

![Servo Pinout](images/Servo-Pinout.png)


> การต่อ Servo (ใช้ไฟ 5V)

<a id="lab6-2-example-code"></a>
### ตัวอย่างโค้ด (ESP32Servo)

```c
#include <ESP32Servo.h>

Servo myservo;
int servoPin = 18;
int pos = 0;

void setup() {
  myservo.attach(servoPin);
}

void loop() {
  for (pos = 0; pos <= 180; pos++) {
    myservo.write(pos);
    delay(15);
  }
  for (pos = 180; pos >= 0; pos--) {
    myservo.write(pos);
    delay(15);
  }
}
```

---

<a id="lab6-3-servo-manual-pwm"></a>
## Lab 6.3: ควบคุม Servo Motor ด้วยการสร้าง PWM เอง

![Servo PWM Signal](images/Servo-PWM-Signal.png)

> PWM ที่ใช้ควบคุม Servo (50 Hz)

<a id="lab6-3-principles"></a>
### หลักการ

- คาบ = 20 ms (50 Hz)  
- Pulse width = 1–2 ms → 0–180 องศา  
- 1 องศา ≈ 5.67 µs  

หากใช้ PWM Resolution = 8 bit

- 0° → duty ≈ 13  
- 90° → duty ≈ 19  
- 180° → duty ≈ 26  

ความละเอียดสูงขึ้น → คุมมุมได้ละเอียดขึ้น

---


