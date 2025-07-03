import sys, os, time
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit, QPushButton, QMessageBox, QLabel, QHBoxLayout
)
from PyQt5.QtCore import Qt

def update_vision_layout(vision_layout):
    for i in os.listdir("entries/"):
        label = QLabel()
        label.setText(f"{i}")
        vision_layout.addWidget(label)

    return vision_layout

def save_entry(entry_text, diary_folder, entry_name, vision_layout):
    if not os.path.exists(diary_folder):
        os.makedirs(diary_folder)
    vision_layout = update_vision_layout(vision_layout)
    file_name = f"{diary_folder}{entry_name}.txt"
    try:
        with open(file_name, 'w') as file:
            file.write(entry_text)
        QMessageBox.information(None, "Success", f"Entry saved as {file_name}")
    except Exception as e:
        QMessageBox.critical(None, "Error", f"Failed to save entry: {e}")
    return vision_layout

def main():
    app = QApplication([])

    diary_folder = "entries/"

    fenster = QMainWindow()
    fenster.setWindowTitle("Your Diary")
    window_width = 1000
    window_height = 600
    fenster.setGeometry(0, 0, window_width, window_height)


    entry_name = QTextEdit()
    entry_name.setText(f"Diary Entry - {time.strftime('%Y-%m-%d')}")

    textfeld = QTextEdit()
    textfeld.setPlaceholderText("Write your diary entry here...")

    button = QPushButton("Save Entry")
    button.clicked.connect(lambda: vision_layout = save_entry(textfeld.toPlainText(), diary_folder, entry_name.toPlainText(), vision_layout))

    vision_layout = QHBoxLayout()

    layout = QVBoxLayout()
    layout.addLayout(vision_layout)
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