import sys, os, time
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit, QPushButton, QMessageBox, QLabel
)
from PyQt5.QtCore import Qt

def save_entry(entry_text, diary_folder, entry_name):
    file_name = f"{diary_folder}{entry_name}.txt"
    try:
        with open(file_name, 'w') as file:
            file.write(entry_text)
        QMessageBox.information(None, "Success", f"Entry saved as {file_name}")
    except Exception as e:
        QMessageBox.critical(None, "Error", f"Failed to save entry: {e}")

def main():
    app = QApplication([])

    diary_folder = "entries/"

    fenster = QMainWindow()
    fenster.setWindowTitle("Your Diary")
    window_width = 1000
    window_height = 600
    fenster.setGeometry(0, 0, window_width, window_height)

    label = QLabel()
    label.setStyleSheet("background-color: lightgray;")
    label.setFixedSize(200, 100)
    label.setText("This is a label")

    entry_name = QTextEdit()
    entry_name.setText(f"Diary Entry - {time.strftime('%Y-%m-%d')}")

    textfeld = QTextEdit()
    textfeld.setPlaceholderText("Write your diary entry here...")

    button = QPushButton("Save Entry")
    button.clicked.connect(lambda: save_entry(textfeld.toPlainText(), diary_folder, entry_name.toPlainText()))

    layout = QVBoxLayout()


    layout.addWidget(label)
    layout.addWidget(entry_name)
    layout.addWidget(textfeld)
    layout.addWidget(button)

    central_widget = QWidget()
    central_widget.setLayout(layout)

    fenster.setCentralWidget(central_widget)

    fenster.show()



    app.exec_()


if __name__ == "__main__":
    main()