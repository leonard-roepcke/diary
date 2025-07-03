import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit, QPushButton, QMessageBox
)
from PyQt5.QtCore import Qt

# --- Diary Logic ---
class DiaryManager:
    def __init__(self):
        self.entries = []  # Später durch Datei/DB ersetzbar

    def add_entry(self, text):
        self.entries.append(text)

    def get_entries(self):
        return self.entries

# --- Diary Entry Widget ---
class DiaryEntryWidget(QWidget):
    def __init__(self, diary_manager):
        super().__init__()
        self.diary_manager = diary_manager
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.text_edit = QTextEdit()
        self.save_button = QPushButton("Eintrag speichern")
        self.save_button.clicked.connect(self.save_entry)
        self.layout.addWidget(self.text_edit)
        self.layout.addWidget(self.save_button)
        self.setLayout(self.layout)

    def save_entry(self):
        text = self.text_edit.toPlainText().strip()
        if text:
            self.diary_manager.add_entry(text)
            self.text_edit.clear()
            QMessageBox.information(self, "Gespeichert", "Eintrag wurde gespeichert.")
        else:
            QMessageBox.warning(self, "Fehler", "Der Eintrag ist leer.")

# --- Main Window ---
class MainWindow(QMainWindow):
    def __init__(self, diary_manager):
        super().__init__()
        self.setWindowTitle("My Diary")
        self.diary_manager = diary_manager
        self.entry_widget = DiaryEntryWidget(self.diary_manager)
        self.setCentralWidget(self.entry_widget)


def main():
    app = QApplication(sys.argv)
    diary_manager = DiaryManager()
    window = MainWindow(diary_manager)
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()