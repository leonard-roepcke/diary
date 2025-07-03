import sys, os, time
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit, QPushButton, QMessageBox, QLabel, QHBoxLayout
)
from PyQt5.QtCore import Qt

def update_vision_layout(vision_layout, entry_name):
    # Clear the existing layout
    for i in reversed(range(vision_layout.count())):
        widget = vision_layout.itemAt(i).widget()
        if widget is not None:
            widget.deleteLater()

    for i in sorted(os.listdir("entries/")):
        label = QLabel()
        label.setText(f"{i}")
        vision_layout.addWidget(label)

    entry_name.setText(f"Diary Entry Nr.{len(os.listdir('entries/'))+1} - {time.strftime('%Y-%m-%d')}")


def save_entry(entry_text, diary_folder, entry_name, vision_layout):
    raw_name = entry_name.toPlainText()
    safe_name = raw_name.strip().replace("\n", "_").replace(" ", "_")
    file_name = f"{diary_folder}{safe_name}.txt"

    if not os.path.exists(diary_folder):
        os.makedirs(diary_folder)
    try:
        with open(file_name, 'w') as file:
            file.write(entry_text)
        QMessageBox.information(None, "Success", f"Entry saved as {file_name}")
    except Exception as e:
        QMessageBox.critical(None, "Error", f"Failed to save entry: {e}")
    
    update_vision_layout(vision_layout, entry_name)

def main():
    app = QApplication([])

    diary_folder = "entries/"

    fenster = QMainWindow()
    fenster.setWindowTitle("Your Diary")
    window_width = 1000
    window_height = 600
    fenster.setGeometry(0, 0, window_width, window_height)


    entry_name = QTextEdit()
    entry_name.setText(f"Diary Entry Nr.{len(os.listdir(diary_folder))} - {time.strftime('%Y-%m-%d')}")

    textfeld = QTextEdit()
    textfeld.setPlaceholderText("Write your diary entry here...")

    button = QPushButton("Save Entry")
    button.clicked.connect(lambda: save_entry(textfeld.toPlainText(), diary_folder, entry_name, vision_layout))

    vision_layout = QHBoxLayout()
    update_vision_layout(vision_layout, entry_name)

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