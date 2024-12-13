import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QLineEdit, QSplashScreen
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QTimer

# Create a QGuiApplication instance
app = QApplication(sys.argv)
app.setWindowIcon(QIcon('icon.png'))  # Replace 'your_icon.ico' with the path to your icon

# Create a QPixmap object with your splash screen image
splash_pixmap = QPixmap('blaksplash.png')  # Replace 'splash.png' with the path to your image

# Create and display the splash screen
splash = QSplashScreen(splash_pixmap, Qt.WindowStaysOnTopHint)
splash.show()

# Add a timer to control how long the splash screen is displayed (e.g., 3 seconds)
timer = QTimer()
timer.singleShot(3000, splash.close)  # Close the splash screen after 3000 milliseconds (3 seconds)

class CSVSuffixApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle("Contact Suffixer By Blak")

        self.label = QLabel("Select a CSV file and enter a suffix:", self)
        self.label.setGeometry(20, 20, 360, 20)

        self.select_button = QPushButton("Select CSV File", self)
        self.select_button.setGeometry(20, 50, 150, 30)
        self.select_button.clicked.connect(self.select_csv_file)

        self.suffix_input = QLineEdit(self)
        self.suffix_input.setGeometry(180, 50, 150, 30)

        self.process_button = QPushButton("Process CSV", self)
        self.process_button.setGeometry(20, 90, 150, 30)
        self.process_button.clicked.connect(self.process_csv)

    def select_csv_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(self, "Select CSV File", "", "CSV Files (*.csv)", options=options)
        if file_path:
            self.csv_file_path = file_path

    def process_csv(self):
        try:
            suffix = self.suffix_input.text()
            if hasattr(self, 'csv_file_path') and suffix:
                df = pd.read_csv(self.csv_file_path)
                df['Name'] = df['Name'].apply(lambda x: f"{x}({suffix})")
                output_file_path = "output.csv"
                df.to_csv(output_file_path, index=False)
                self.label.setText(f"Modified data saved to {output_file_path}")
            else:
                self.label.setText("Please select a CSV file and enter a suffix.")
        except Exception as e:
            self.label.setText(f"Error: {str(e)}")

def main():
    window = CSVSuffixApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
