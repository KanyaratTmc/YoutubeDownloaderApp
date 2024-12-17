# YouTube Downloader App 📥  

โปรแกรมนี้เป็นแอปพลิเคชันสำหรับดาวน์โหลดวิดีโอจาก YouTube ผ่านลิงก์ที่ผู้ใช้ป้อน โดยใช้ Python และ PyQt6 พร้อมแสดงแถบความคืบหน้าระหว่างการดาวน์โหลด  

---

## **คุณสมบัติหลัก** 🛠️  
- **ป้อน URL YouTube:** ป้อนลิงก์วิดีโอ YouTube เพื่อเริ่มการดาวน์โหลด  
- **ดาวน์โหลดวิดีโอ:** ดาวน์โหลดวิดีโอและบันทึกลงในโฟลเดอร์ `downloads`  
- **แสดงความคืบหน้า:** แสดงแถบความคืบหน้าระหว่างการดาวน์โหลด  
- **แจ้งเตือนสำเร็จ/ผิดพลาด:** แจ้งเตือนเมื่อการดาวน์โหลดเสร็จสิ้นหรือเกิดข้อผิดพลาด  

---

## **เทคโนโลยีที่ใช้** 💻  
- **Python 3.x**  
- **PyQt6:** ใช้สำหรับสร้างอินเทอร์เฟซกราฟิก (GUI)  
- **yt-dlp:** ใช้สำหรับดาวน์โหลดวิดีโอจาก YouTube  

---

## **วิธีติดตั้งและใช้งาน** ⚙️  

### 1. ติดตั้ง Python  
ดาวน์โหลดและติดตั้ง **Python** เวอร์ชัน 3.6 ขึ้นไปจาก [python.org](https://www.python.org/)  
ระหว่างการติดตั้ง **เลือก "Add Python to PATH"**  

### 2. ติดตั้งไลบรารีที่จำเป็น  
รันคำสั่งด้านล่างใน **Terminal** หรือ **Command Prompt**:  
```bash
pip install PyQt6 yt-dlp
```
### 3. รันโปรแกรม
บันทึกโค้ดในไฟล์ชื่อ youtube_downloader.py และรันโปรแกรมด้วยคำสั่ง:

```bash
python youtube_downloader.py
```
## การใช้งานโปรแกรม 🚀
1. เปิดโปรแกรมและป้อนลิงก์  YouTube ที่ต้องการดาวน์โหลด
2. คลิกปุ่ม "Download"
3. รอให้แถบความคืบหน้าแสดงผล และไฟล์จะถูกบันทึกในโฟลเดอร์ downloads
4. โปรแกรมจะแจ้งเตือนเมื่อดาวน์โหลดเสร็จสมบูรณ์
## ข้อแนะนำ 🔍
ตรวจสอบให้แน่ใจว่าลิงก์ YouTube ที่ป้อนเป็นลิงก์ที่ถูกต้อง
ไฟล์วิดีโอที่ดาวน์โหลดจะถูกบันทึกในโฟลเดอร์ downloads ในไดเรกทอรีเดียวกับโปรแกรม

##  เทคโนโลยีที่รองรับ
รองรับระบบปฏิบัติการ Windows, macOS, Linux
ไฟล์ที่ดาวน์โหลดจะมีชื่อไฟล์เป็นชื่อวิดีโอจาก YouTube


# YouTube Downloader App 📥
This application is a YouTube video downloader built using Python and PyQt6. It allows users to input a YouTube URL, download the video, and track progress through a progress bar.

## Features 🛠️
Input YouTube URL: Enter the link to the YouTube video
Download Video: Save the video to the downloads folder
Progress Bar: Track download progress visually
Notifications: Alert users when the download is successful or if an error occurs
Technologies Used 💻
Python 3.x
PyQt6: For building the graphical user interface (GUI)
yt-dlp: For downloading YouTube videos
## Installation and Usage ⚙️
1. Install Python
Download and install Python version 3.6 or higher from python.org.
Ensure you add Python to PATH during installation.

2. Install Required Libraries
Run the following command in Terminal or Command Prompt:

```
pip install PyQt6 yt-dlp
```
3. Run the Application
Save the code as youtube_downloader.py and run it using:

```bash
python youtube_downloader.py
```
## How to Use 🚀
Open the program and input a valid YouTube URL
Click the "Download" button
Wait for the progress bar to update and the download to complete
The video file will be saved in the downloads folder

## Supported Platforms
Works on Windows, macOS, and Linux
Videos are saved with the title of the YouTube video

---

Developer 👨‍💻
Kanyarat Thammachot
© 2024