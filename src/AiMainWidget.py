from PyQt5.QtWidgets import QWidget, QLabel
import pickItem
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap


class MainWidget(QWidget):

    tateCoords = [0, 50, 100, 150, 200]
    playeryokoCoord = 700
    yokoCoords = [0, 100, 200, 300, 400, 500, 600, 700]

    def __init__(self):
        super().__init__()
        self.title = 'PyQt Project'
        self.left = 300
        self.top = 300
        self.width = 250
        self.height = 900
        self.preLoadImg()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        # TODO: timerのスピードを変える
        self.timer.start(100)
        self.updateCount = 0
        # TODO: updateCountLimitを乱数に
        self.updateCountLimit = 2
        self.itemLabels = []

        self.playerLabel = QLabel()
        self.playerLabel.setPixmap(QPixmap('../img/normalStudent.png'))

        self.show()

    def preLoadImg(self):
        self.plusItemsPix = pickItem.PlusItem()
        self.minusItemsPix = pickItem.MinusItem()

    def update(self):
        pass
