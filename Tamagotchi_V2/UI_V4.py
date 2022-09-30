import sys
import time

from Tama import Tamagotchi

from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import QtCore


class TWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tamagotchi")
        self.setWindowIcon(QIcon("qt.png"))
        self.setFixedWidth(350)
        self.setFixedHeight(350)
        #self.setStyleSheet('background-color:blue') #can be set as a variable
        self.create_details()

    #set up the UI pieces, Bars, Buttons, etc.
    #Icon is a temp file.

    def feed_properties(self):
        self.feed_progressbar = QProgressBar(self)
        self.feed_progressbar.setGeometry(15,175,100,50)
        self.feed_progressbar.setMaximum(100)
        self.feed_progressbar.setTextVisible(False)
        self.feed_progressbar.setFixedHeight(5)
        self.feed_progressbar.setValue(5)

        self.feed_Button = QPushButton("Feed Me", self)
        self.feed_Button.setGeometry(15,200,100,50)
        self.feed_Button.clicked.connect(self.feedme)
        self.feed_Button.setIcon(QIcon("tamaicon.png"))

    def sleep_properties(self):
        self.sleep_progressbar = QProgressBar(self)
        self.sleep_progressbar.setGeometry(120,175,100,50)
        self.sleep_progressbar.setMaximum(100)
        self.sleep_progressbar.setTextVisible(False)
        self.sleep_progressbar.setFixedHeight(5)
        self.sleep_progressbar.setValue(5)

        self.sleep_button = QPushButton("Sleep Me", self)
        self.sleep_button.setGeometry(120,200,100,50)
        self.sleep_button.clicked.connect(self.sleepy)
        self.sleep_button.setIcon(QIcon("tamaicon.png"))

    def hydrate_properties(self):
        self.hydrate_progressbar = QProgressBar(self)
        self.hydrate_progressbar.setGeometry(225,175,100,50)
        self.hydrate_progressbar.setMaximum(100)
        self.hydrate_progressbar.setValue(5)
        self.hydrate_progressbar.setFixedHeight(5)
        self.hydrate_progressbar.setTextVisible(False)

        hydrate_button = QPushButton("Hydrate Me", self)
        hydrate_button.setGeometry(225,200,100,50)
        hydrate_button.clicked.connect(self.drink)
        hydrate_button.setIcon(QIcon("tamaicon.png"))

    def quit_properties(self):
        quit_button = QPushButton("Save & Quit", self)
        quit_button.setGeometry(120,275,100,50)
        quit_button.setIcon(QIcon("tamaicon.png"))

        quit_button.clicked.connect(self.saveandquit)

# begin creating objects

    def create_details(self):

        #create all the UI on the Widget
        self.feed_properties()
        self.sleep_properties()
        self.hydrate_properties()
        self.quit_properties()

    #functions

# Update the color of the bar based on its current stat

    def chngeclr(self, color):

        cde = """
            ::chunk {{
                background: {0};
                border-radius: 2px;
            }}

        """.format(color)

        return cde

##Feed the Tamagotchi - later will update to use Stats - just wanted to make sure it works

    def feedme(self):
        print("Fed")
        value = self.feed_progressbar.value()
        self.feed_progressbar.setValue(value + 5)

        if value < 30:
            self.feed_progressbar.setStyleSheet(self.chngeclr('red'))
        elif 50 > value > 30:
            self.feed_progressbar.setStyleSheet(self.chngeclr('yellow'))
        elif value > 50:
            self.feed_progressbar.setStyleSheet(self.chngeclr('green'))

# Make the Tamagotchi Sleep - later will update to use Stats - just wanted to make sure it works and using UI

    def sleepy(self):
        print("ZzZz")
        
        value = self.sleep_progressbar.value()
        self.sleep_progressbar.setValue(value + 5)

        if value < 30:
            self.sleep_progressbar.setStyleSheet(self.chngeclr('red'))
        elif 50 > value > 30:
            self.sleep_progressbar.setStyleSheet(self.chngeclr('yellow'))
        elif value > 50:
            self.sleep_progressbar.setStyleSheet(self.chngeclr('green'))

# Give the Tamagotchi a drink - later will update to use Stats - just wanted to make sure it works and using UI

    def drink(self):
        print("gulpgulpgulp")
        value = self.hydrate_progressbar.value()
        self.hydrate_progressbar.setValue(value + 5)

        if value < 30:
            self.hydrate_progressbar.setStyleSheet(self.chngeclr('red'))
        elif 50 > value > 30:
            self.hydrate_progressbar.setStyleSheet(self.chngeclr('yellow'))
        elif value > 50:
            self.hydrate_progressbar.setStyleSheet(self.chngeclr('green'))

    def saveandquit(self):
        ### Update the DB prior to saving.
        print("Fine, Leave me.")
        QApplication.instance().quit()


def main():
  #  threaditall.run(0)
    tama_app = QApplication([])
    window = TWindow()
    window.show()
    sys.exit(tama_app.exec())


if __name__ == '__main__':
    main()


