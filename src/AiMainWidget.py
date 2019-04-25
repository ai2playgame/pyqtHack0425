from PyQt5.QtWidgets import QWidget, QLabel
import pickItem
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPixmap, QFont
import random


class MainWidget(QWidget):

    tateCoords = [0, 50, 100, 150, 200]
    playeryokoCoord = 600
    yokoCoords = [0, 100, 200, 300, 400, 500, 600]

    def __init__(self):
        super().__init__()
        self.title = 'PyQt Project'
        self.left = 300
        self.top = 0
        self.width = 250
        self.height = 700
        self.preLoadImg()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        # TODO: timerのスピードを変える
        self.timerspeed = 800
        self.timer.start(self.timerspeed)
        self.updateCount = 0
        self.dropCount = 0
        self.dropCountLimit = 6
        self.score = 0

        # TODO: updateCountLimitを乱数に
        self.updateCountLimit = 1

        # item用のラベルを保持する配列
        self.itemLabels = []

        self.font = QFont()
        self.font.setBold(True)
        self.font.setPointSize(20)

        # self.playerPix = QPixmap('../img/normalStudent.png')
        self.playerLabel = QLabel(self)
        self.playerLabel.setPixmap(QPixmap('../img/normalStudent.png'))

        self.playerLabel.move(MainWidget.tateCoords[2],
                              MainWidget.playeryokoCoord)

        self.show()

    def preLoadImg(self):
        self.plusItemsPix = pickItem.PlusItem()
        self.minusItemsPix = pickItem.MinusItem()

    def update(self):
        print("update! {0}".format(self.updateCount))
        if self.updateCount >= self.updateCountLimit:
            # 新規生成
            self.updateCount = 0
            label = QLabel(self)
            label.move(self.selectStartX(), MainWidget.yokoCoords[0])
            print("minus")
            # label.setPixmap(QPixmap(self.minusItemsPix.getRandomImgPath()))
            label.setFont(self.font)
            label.setText('薬物')
            self.itemLabels.append(label)
            self.dropCount += 1
        else:
            self.updateCount += 1

        if self.dropCount >= self.dropCountLimit:
            self.timerspeed *= 0.9
            self.timer.start(self.timerspeed)
            self.dropCount = 0

        self.allItemsMove()
        gameOverFlag = self.checkCross()
        self.ItemDelete()

        if gameOverFlag:
            print('socre: {}'.format(self.score))
            self.timer.stop()

    def selectYokoCoord(self):
        return random.choice(MainWidget.yokoCoords)

    def allItemsMove(self):
        for label in self.itemLabels:
            label.move(label.x(), label.y() + 100)
            label.show()

    def ItemDelete(self):
        for label in self.itemLabels[:]:
            if label.y() > MainWidget.playeryokoCoord:
                print("Delete {0}, {1}".format(label.x(), label.y()))

                self.itemLabels.remove(label)
                self.score += 1

    def selectStartX(self):
        return random.choice(MainWidget.tateCoords)

    def dummy(self):

        if True:
            print('dummy')
            tLabel = QLabel(self)
            tLabel.setPixmap(QPixmap(self.plusItemsPix.getRandomImgPath()))
            tLabel.move(0, 0)
            self.show()

    def keyPressEvent(self, event):
        key = event.key()

        if key == Qt.Key_Left:
            if self.playerLabel.x() > MainWidget.tateCoords[0]:
                self.playerLabel.move(
                    self.playerLabel.x() - 50, self.playerLabel.y())
        if key == Qt.Key_Right:
            if self.playerLabel.x() < MainWidget.tateCoords[4]:
                self.playerLabel.move(
                    self.playerLabel.x() + 50, self.playerLabel.y()
                )

    def checkCross(self):
        for label in self.itemLabels:
            print('Item:({}, {}) player({}, {})'.format(
                label.x(), label.y(), self.playerLabel.x(), self.playerLabel.y()))
            if label.x() == self.playerLabel.x() and label.y() == self.playerLabel.y():
                return True

        return False
