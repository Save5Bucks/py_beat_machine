import sys
import pygame
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QSlider
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPalette, QFont

class BeatMachine(QWidget):
    def __init__(self):
        super().__init__(flags=Qt.FramelessWindowHint)  # Make the window frameless
        pygame.init()
        self.initUI()

    def initUI(self):
        self.setFixedSize(800, 600)  # Set fixed size for the window
        self.setStyleSheet("background-color: #2d2d2d;")  # Set the background color to dark grey
        grid = QGridLayout()
        self.setLayout(grid)

        # Button styling
        button_size = 75  # Define a standard button size
        button_style = ("QPushButton {"
                        "background-color: #333;"
                        "color: white;"
                        "border-radius: 10px;"
                        "font-size: 16px;"
                        "font-weight: bold;"
                        "}"
                        "QPushButton:pressed {"
                        "background-color: #555;"
                        "}")

        # Create a 4x4 grid of buttons
        positions = [(i, j) for i in range(4) for j in range(4)]
        for position in positions:
            pad = QPushButton(f'Pad {position[0]*4 + position[1] + 1}')
            pad.setFixedSize(button_size, button_size)  # Use the defined button size
            pad.setStyleSheet(button_style)
            pad.clicked.connect(self.playSound)
            grid.addWidget(pad, *position)

        # Volume control
        self.volumeSlider = QSlider(Qt.Horizontal, self)
        self.volumeSlider.setRange(0, 100)  # Set volume range from 0 to 100
        self.volumeSlider.setValue(50)  # Default volume set to 50%
        self.volumeSlider.setStyleSheet("QSlider::groove:horizontal {"
                                        "border: 1px solid #bbb;"
                                        "background: white;"
                                        "height: 10px;"
                                        "border-radius: 4px;"
                                        "}"
                                        "QSlider::handle:horizontal {"
                                        "background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #eee, stop:1 #ccc);"
                                        "border: 1px solid #777;"
                                        "width: 18px;"
                                        "margin-top: -2px;"
                                        "margin-bottom: -2px;"
                                        "border-radius: 4px;"
                                        "}")
        self.volumeSlider.valueChanged[int].connect(self.setVolume)
        grid.addWidget(self.volumeSlider, 4, 0, 1, 4)

        self.setWindowTitle('Beat Machine Simulator')

    def playSound(self):
        sender = self.sender()
        print(f'{sender.text()} was pressed')
        # Integrate playing a sound here
        # pygame.mixer.Sound('path_to_sound.wav').play()

    def setVolume(self, value):
        pygame.mixer.music.set_volume(value / 100)  # Adjust volume

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BeatMachine()
    ex.show()  # Use show to better control the window display
    sys.exit(app.exec_())
