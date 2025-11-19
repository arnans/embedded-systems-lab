- [เป้าหมายของการทดลองบน Wokwi](#เป้าหมายของการทดลองบน-wokwi)
- [LAB 1.1 - Hello World (Serial Monitor)](#lab-11---hello-world-serial-monitor)
  - [ขั้นตอน](#ขั้นตอน)
  - [สิ่งที่ต้องส่ง](#สิ่งที่ต้องส่ง)
- [LAB 1.2 - ไฟกระพริบ (Blink LED)](#lab-12---ไฟกระพริบ-blink-led)
  - [ขั้นตอน](#ขั้นตอน-1)
  - [สิ่งที่ต้องส่ง](#สิ่งที่ต้องส่ง-1)
- [LAB 1.3 - ปุ่มกดและการอ่านสัญญาณ](#lab-13---ปุ่มกดและการอ่านสัญญาณ)
  - [1) กดติด-ปล่อยดับ (Basic Button Control)](#1-กดติด-ปล่อยดับ-basic-button-control)
    - [ขั้นตอน](#ขั้นตอน-2)
  - [สิ่งที่ต้องส่ง](#สิ่งที่ต้องส่ง-2)
- [LAB 1.3.2 - นับจำนวนครั้งที่กดปุ่ม](#lab-132---นับจำนวนครั้งที่กดปุ่ม)
  - [เป้าหมาย](#เป้าหมาย)
  - [ขั้นตอน](#ขั้นตอน-3)
  - [สิ่งที่ต้องส่ง](#สิ่งที่ต้องส่ง-3)
- [LAB 1.3.3 - ดูสัญญาณ Bounce ด้วย Logic Analyzer](#lab-133---ดูสัญญาณ-bounce-ด้วย-logic-analyzer)
  - [ขั้นตอน](#ขั้นตอน-4)
  - [สิ่งที่ต้องส่ง](#สิ่งที่ต้องส่ง-4)
- [รายการส่งทั้งหมด](#รายการส่งทั้งหมด)

# LAB 1 - การทดลองบน Wokwi (ESP32)
ใช้จำลองร่วมกับการทำปฏิบัติการจริง เพื่อช่วยให้เข้าใจหลักการ I/O, Pull-up, การอ่านปุ่ม, และ Bounce ของสัญญาณได้ชัดเจนขึ้น

**บอร์ดที่ใช้:** `wokwi-esp32-devkit-v1`  
**เว็บไซต์:** https://wokwi.com

---

# เป้าหมายของการทดลองบน Wokwi
- ฝึกใช้เครื่องมือจำลองการทำงาน ESP32  
- สังเกตพฤติกรรมโปรแกรมที่เขียนบน Arduino  
- ทดลอง LED, ปุ่มกด, Pull-up, Internal Pull-up  
- สังเกตสัญญาณ Bounce โดยใช้ Logic Analyzer  
- ดาวน์โหลด VCD และเปิดใน PulseView

---

# LAB 1.1 - Hello World (Serial Monitor)

## ขั้นตอน
1. เปิด Wokwi → สร้างโปรเจกต์ใหม่ → ESP32  
2. ใช้โค้ดต่อไปนี้:

```cpp
void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println("Hello World!");
  delay(1000);
}
```

3. กด "Start"  
4. เปิด Serial Monitor ของ Wokwi  
5. ตรวจสอบว่ามีข้อความแสดงทุก 1 วินาที

## สิ่งที่ต้องส่ง
- ภาพหน้าจอ Serial Monitor แสดงผล “Hello World”

---

# LAB 1.2 - ไฟกระพริบ (Blink LED)



## ขั้นตอน
1. เพิ่ม LED และตัวต้านทานใน Wokwi  
2. ต่อวงจรให้ LED อยู่ที่ GPIO23  
3. ใช้โค้ด:

```cpp
#define LED 23
#define DELAY_TIME 1000

void setup() {
  pinMode(LED, OUTPUT);
}

void loop() {
  digitalWrite(LED, HIGH);
  delay(DELAY_TIME);
  digitalWrite(LED, LOW);
  delay(DELAY_TIME);
}
```

4. รันและสังเกตการกระพริบ

## สิ่งที่ต้องส่ง
- ภาพวงจรบน Wokwi  
- ภาพ LED กระพริบ

---

# LAB 1.3 - ปุ่มกดและการอ่านสัญญาณ

## 1) กดติด-ปล่อยดับ (Basic Button Control)

### ขั้นตอน
1. เพิ่ม Pushbutton  
2. ต่อปุ่มเข้ากับ GPIO32 + external pull-up  
3. เปิด **bounce: ON** ใน properties ของปุ่ม  
4. ใช้โค้ด:

```cpp
#define LED 23
#define BUTTON 32

void setup() {
  pinMode(LED, OUTPUT);
  pinMode(BUTTON, INPUT);
}

void loop() {
  if (digitalRead(BUTTON) == LOW) {
    digitalWrite(LED, HIGH);
  } else {
    digitalWrite(LED, LOW);
  }
}
```

5. ทดลอง Internal Pull-up:

```cpp
pinMode(BUTTON, INPUT_PULLUP);
```

## สิ่งที่ต้องส่ง
- ภาพวงจร  
- โค้ด  
- คำอธิบาย external vs internal pull-up

---

# LAB 1.3.2 - นับจำนวนครั้งที่กดปุ่ม

## เป้าหมาย
ป้องกันการนับรัวเมื่อกดค้าง

## ขั้นตอน
1. ใช้วงจรเดิม  
2. ตรวจจับ HIGH→LOW transition  
3. นับครั้งละ 1  
4. พิมพ์ค่าลง Serial Monitor

## สิ่งที่ต้องส่ง
- โค้ดนับปุ่ม  
- Screenshot Serial Monitor

---

# LAB 1.3.3 - ดูสัญญาณ Bounce ด้วย Logic Analyzer

## ขั้นตอน
1. เพิ่ม Logic Analyzer  
2. ต่อ CH0 → GPIO32  
3. เปิด bounce: ON  
4. Run → กดปุ่ม → Stop  
5. ดาวน์โหลด VCD  
6. เปิดใน PulseView  
7. เลือก sampling rate  
8. ดู Bounce

## สิ่งที่ต้องส่ง
- ภาพ Bounce จาก PulseView  
- อธิบายปัญหา Bounce

---

# รายการส่งทั้งหมด
1. LAB 1.1 - ผล Serial Monitor  
2. LAB 1.2 - วงจร + LED กระพริบ  
3. LAB 1.3.1 - วงจรปุ่ม + ผลกดติดปล่อยดับ  
4. LAB 1.3.1 - อธิบาย external vs internal pull-up  
5. LAB 1.3.2 - โค้ดนับปุ่ม + screenshot  
6. LAB 1.3.3 - Bounce ใน PulseView
