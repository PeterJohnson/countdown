#!/usr/bin/env python
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import datetime

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # Center widget
        self.label = QLabel()
        self.label.setScaledContents(True)
        self.setCentralWidget(self.label)
        self.label.show()

        self.setWindowTitle("Countdown")

        # Update counter once a second
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.updateCounter)
        self.timer.start()

    def updateCounter(self):
        deadline = datetime.datetime(2018, 2, 21, 4, 59)
        remaining = deadline - datetime.datetime.utcnow()
        hours = int(remaining.seconds / 3600)
        mins = int((remaining.seconds - hours * 3600) / 60)
        secs = int(remaining.seconds % 60)
        self.label.setText("%d days, %d:%02d:%02d remaining" % (remaining.days, hours, mins, secs))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    with open("countdown.css") as f:
        app.setStyleSheet(f.read())
    form = MainWindow()
    form.show()
    app.exec_()
