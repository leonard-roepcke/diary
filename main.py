import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit, QPushButton, QMessageBox, QLabel
)
from PyQt5.QtCore import Qt

def main():
    app = QApplication([])

    fenster = QMainWindow()
    fenster.setWindowTitle("Your Diary")
    fenster.setGeometry(100, 100, 800, 600)

    label = QLabel()
    label.setStyleSheet("background-color: lightgray;")
    label.setFixedSize(200, 100)
    label.setText("This is a label")

    layout = QVBoxLayout()

    layout.addWidget(label)

    central_widget = QWidget()
    central_widget.setLayout(layout)

    fenster.setCentralWidget(central_widget)

    fenster.show()



    app.exec_()


if __name__ == "__main__":
    main()