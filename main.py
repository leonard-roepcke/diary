import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit, QPushButton, QMessageBox
)
from PyQt5.QtCore import Qt

def main():
    app = QApplication([])
    fenster = QMainWindow()
    fenster.setWindowTitle("Simple Diary App")
    fenster.setGeometry(100, 100, 800, 600)
    fenster.show()

    fenster_2 = QWidget()
    fenster_2.setWindowTitle("Second Window")
    fenster_2.setGeometry(200, 200, 400, 300)
    fenster_2.show()


    app.exec_()


if __name__ == "__main__":
    main()