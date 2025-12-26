# Name: Sunyoung Chung
# UID: u1577102

import math

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

# PURPOSE: load a series of sprite images stored in a folder with a
# consistent naming pattern: sprite_# or sprite_##.
# Returns a list of the images.
def load_sprite(sprite_folder_name, number_of_frames):
    frames = []
    padding = math.ceil(math.log(number_of_frames - 1, 10))
    for frame in range(number_of_frames):
        folder_and_file_name = (
            sprite_folder_name
            + "/sprite_"
            + str(frame).rjust(padding, "0")
            + ".png"
        )
        frames.append(QPixmap(folder_and_file_name))
    return frames

class SpritePreview(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sprite Animation Preview")

        # This loads the provided sprite and would need to be changed for your own.
        self.num_frames = 21
        self.frames = load_sprite('sprite_images',self.num_frames)

        # Animation state
        self.current_index = 0
        self.fps = 10
        self.delay_ms = int(1000 / self.fps)

        # Timer for animation
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.advance_frame)

        # UI-related instance variables (will be set in setupUI)
        self.image_label = None
        self.fps_label = None
        self.slider = None
        self.start_button = None

        # Make the GUI in the setupUI method
        self.setupUI()

    # PURPOSE: create application window
    def setupUI(self):
        # An application needs a central widget - often a QFrame
        frame = QFrame()
        main_layout = QVBoxLayout(frame)

        # 1) NEW: image + slider horizontal Layout
        top_layout = QHBoxLayout()

        # sprite display area
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        if self.frames:
            self.image_label.setPixmap(self.frames[self.current_index])

        top_layout.addWidget(self.image_label)

        # Right vertical slider
        right_layout = QVBoxLayout()

        self.fps_label = QLabel(f"{self.fps} Fps")

        self.slider = QSlider(Qt.Orientation.Vertical)
        self.slider.setRange(1, 100)
        self.slider.setValue(self.fps)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(10)
        self.slider.valueChanged.connect(self.slider_changed)

        right_layout.addWidget(self.slider)
        right_layout.addWidget(self.fps_label)

        top_layout.addLayout(right_layout)

        # Add top_layout in main_layout
        main_layout.addLayout(top_layout)

        # 2) the button in the bottom
        control_frame = QFrame()
        control_layout = QVBoxLayout(control_frame)

        # Title Name
        title_name = QLabel("Frames Per Second")
        control_layout.addWidget(title_name)

        # Start / Stop Button
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_or_stop)
        control_layout.addWidget(self.start_button)

        main_layout.addWidget(control_frame)

        self.setCentralWidget(frame)

        # menu bar
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        pause_action = QAction("Pause", self)
        pause_action.triggered.connect(self.pause_animation)
        file_menu.addAction(pause_action)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

    # TODO: add methods to act as slots to connect to signals

    # SLOT: called when the slider value changes
    def slider_changed(self, value: int):
        self.fps = value
        self.fps_label.setText(f"{value} FPS")
        self.delay_ms = int(1000 / self.fps)
        if self.timer.isActive():
            self.timer.setInterval(self.delay_ms)

    # SLOT: start or stop the animation when the button is clicked
    def start_or_stop(self):
        if self.timer.isActive():
            self.timer.stop()
            self.start_button.setText("Start")
        else:
            self.timer.start(self.delay_ms)
            self.start_button.setText("Stop")

    # SLOT: pause the animation from the menu
    def pause_animation(self):
        if self.timer.isActive():
            self.timer.stop()
            self.start_button.setText("Start")

    # SLOT: advance to the next frame and update the label
    def advance_frame(self):
        if not self.frames:
            return
        self.current_index = (self.current_index + 1) % self.num_frames
        self.image_label.setPixmap(self.frames[self.current_index])

def main():
    app = QApplication([])
    # Create our custom application
    window = SpritePreview()
    # And show it
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
