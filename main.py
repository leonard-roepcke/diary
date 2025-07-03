import sys, os, time
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit, QPushButton, QMessageBox, QLabel, QHBoxLayout
)
from PyQt5.QtCore import Qt

def clear_layout(layout):
    while layout.count():
        item = layout.takeAt(0)
        widget = item.widget()
        if widget is not None:
            widget.deleteLater()
        else:
            sub_layout = item.layout()
            if sub_layout is not None:
                clear_layout(sub_layout)

def update_vision_layout(vision_layout, entry_name, textfeld, diary_folder):
    # Clear the existing layout
    for i in reversed(range(vision_layout.count())):
        item = vision_layout.itemAt(i)
        if item is not None:
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                # Wenn es ein Layout ist, auch löschen
                layout_item = item.layout()
                if layout_item is not None:
                    clear_layout(layout_item)

    files = sorted(os.listdir(diary_folder))
    for filename in files:
        label = QLabel(filename)

        open_button = QPushButton("Open")
        open_button.clicked.connect(lambda checked, f=filename: load_entry(f, diary_folder, entry_name, textfeld))

        row = QHBoxLayout()
        row.addWidget(label)
        row.addWidget(open_button)

        vision_layout.addLayout(row)

    # + New Entry Button
    new_button = QPushButton("+ New Entry")
    new_button.clicked.connect(lambda: create_new_entry(entry_name, textfeld, diary_folder))
    vision_layout.addWidget(new_button)

    # Auch Entry-Name beim Speichern hochzählen:
    entry_name.setText(f"Diary Entry Nr.{len(files)+1} - {time.strftime('%Y-%m-%d')}")

def load_entry(filename, diary_folder, entry_name, textfeld):
    file_path = os.path.join(diary_folder, filename)
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        entry_name.setText(filename.replace(".txt", ""))
        textfeld.setPlainText(content)
    except Exception as e:
        QMessageBox.critical(None, "Error", f"Could not open file: {e}")

def create_new_entry(entry_name, textfeld, diary_folder):
    files = os.listdir(diary_folder)
    new_number = len(files) + 1
    entry_name.setText(f"Diary Entry Nr.{new_number} - {time.strftime('%Y-%m-%d')}")
    textfeld.clear()


def save_entry(entry_text, diary_folder, entry_name, vision_layout, textfeld):
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

    update_vision_layout(vision_layout, entry_name, textfeld, diary_folder)
    textfeld.clear()

def main():
    app = QApplication([])

    diary_folder = "entries/"

    fenster = QMainWindow()
    fenster.setWindowTitle("Your Diary")
    window_width = 1000
    window_height = 600
    fenster.setGeometry(0, 0, window_width, window_height)

    entry_name = QTextEdit()
    entry_name.setFixedHeight(40)
    entry_name.setText(f"Diary Entry Nr.{len(os.listdir(diary_folder))+1} - {time.strftime('%Y-%m-%d')}")

    textfeld = QTextEdit()
    textfeld.setPlaceholderText("Write your diary entry here...")

    button = QPushButton("Save Entry")
    button.clicked.connect(lambda: save_entry(textfeld.toPlainText(), diary_folder, entry_name, vision_layout, textfeld))

    vision_layout = QVBoxLayout()
    update_vision_layout(vision_layout, entry_name, textfeld, diary_folder)

    # 👉 Editor-Teil: alles untereinander
    editor_layout = QVBoxLayout()
    editor_layout.addWidget(entry_name)
    editor_layout.addWidget(textfeld)
    editor_layout.addWidget(button)

    # 👉 Haupt-Layout: links & rechts nebeneinander
    main_layout = QHBoxLayout()
    main_layout.addLayout(vision_layout, stretch=1)   # links
    main_layout.addLayout(editor_layout, stretch=3)   # rechts

    central_widget = QWidget()
    central_widget.setLayout(main_layout)

    fenster.setCentralWidget(central_widget)
    fenster.show()

    app.exec_()


if __name__ == "__main__":
    main()
