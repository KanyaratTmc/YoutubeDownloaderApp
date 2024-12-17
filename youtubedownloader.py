import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QProgressBar, QMessageBox
)
from PyQt6.QtCore import Qt
import yt_dlp

class YoutubeDownloaderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('YouTube Downloader App')
        self.setGeometry(100, 100, 500, 300)  # ขยายขนาดหน้าต่าง
        self.UI()

    def UI(self):
        layout = QVBoxLayout()
        layout.setSpacing(15)  # เพิ่มช่องว่างระหว่างองค์ประกอบ

        # Label
        self.urlLabel = QLabel('YouTube URL:', self)
        self.urlLabel.setStyleSheet("font-size: 16px; font-weight: bold; color: #2c3e50;")
        layout.addWidget(self.urlLabel)

        # Input
        self.urlInput = QLineEdit(self)
        self.urlInput.setPlaceholderText("Enter YouTube URL here...")
        self.urlInput.setStyleSheet("""
            QLineEdit {
                font-size: 14px;
                padding: 8px;
                border: 2px solid #3498db;
                border-radius: 5px;
            }
            QLineEdit:focus {
                border: 2px solid #2980b9;
            }
        """)
        layout.addWidget(self.urlInput)

        # Download Button
        self.downloadButton = QPushButton('Download', self)
        self.downloadButton.clicked.connect(self.downloadVideo)
        self.downloadButton.setStyleSheet("""
            QPushButton {
                font-size: 14px;
                padding: 10px;
                background-color: #3498db;
                color: white;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #1c6d9e;
            }
        """)
        layout.addWidget(self.downloadButton)

        # Progress Bar
        self.progressBar = QProgressBar(self)
        self.progressBar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progressBar.setStyleSheet("""
            QProgressBar {
                border: 2px solid #3498db;
                border-radius: 5px;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #3498db;
                width: 20px;
            }
        """)
        layout.addWidget(self.progressBar)

        self.setLayout(layout)

    def downloadVideo(self):
        url = self.urlInput.text()
        try:
            # ตั้งค่าการดาวน์โหลด
            ydl_opts = {
                'outtmpl': 'downloads/%(title)s.%(ext)s',  # กำหนดโฟลเดอร์สำหรับไฟล์ที่ดาวน์โหลด
                'progress_hooks': [self.onProgress],       # เชื่อมฟังก์ชัน progress
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])  # เริ่มดาวน์โหลดวิดีโอ
            QMessageBox.information(self, 'Success', 'Download completed!')
        except Exception as e:
            QMessageBox.warning(self, 'Error', f'Failed to download video.\n{str(e)}')

    def onProgress(self, d):
        if d['status'] == 'downloading':
            total_bytes = d.get('total_bytes', 1)
            downloaded_bytes = d.get('downloaded_bytes', 0)
            percentage = int(downloaded_bytes / total_bytes * 100)
            self.progressBar.setValue(percentage)

def main():
    app = QApplication(sys.argv)
    window = YoutubeDownloaderApp()
    window.setStyleSheet("""
        QWidget {
            background-color: #ecf0f1;
        }
    """)
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()