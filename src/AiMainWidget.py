from PyQt5.QtWidgets import QWidget, QLabel
import pickItem
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPixmap
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
        self.dummy()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        # TODO: timerのスピードを変える
        # self.timer.start(1000)
        self.updateCount = 0

        # TODO: updateCountLimitを乱数に
        self.updateCountLimit = 1

        # item用のラベルを保持する配列
        self.itemLabels = []

        self.playerPix = QPixmap('../img/normalStudent.png')
        self.playerLabel = QLabel(self)
        self.playerLabel.setPixmap(self.playerPix)

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
            if random.random() <= 0.5:
                # 8割の確率で障害物が降ってくる
                print("minus")
                label.setPixmap(self.minusItemsPix.getRandomImgCopy())
                # self.itemLabels.append(label)
            else:
                print("plus")
                label.setPixmap(self.plusItemsPix.getRandomImgCopy())
                self.itemLabels.append(label)
        else:
            self.updateCount += 1

        self.allItemsMove()
        self.ItemDelete()

        self.show()

    def selectYokoCoord(self):
        return random.choice(MainWidget.yokoCoords)

    def allItemsMove(self):
        for label in self.itemLabels:
            label.move(label.x(), label.y() + 100)

    def ItemDelete(self):
        for label in self.itemLabels[:]:
            if label.y() >= MainWidget.playeryokoCoord:
                print("Delete {0}, {1}".format(label.x(), label.y()))
                self.itemLabels.remove(label)

    def selectStartX(self):
        return random.choice(MainWidget.tateCoords)

    def dummy(self):

        if True:
            tLabel = QLabel(self)
            tLabel.setPixmap(self.plusItemsPix.getRandomImgCopy())
            tLabel.move(0, 0)

    def keyPressEvent(self, event):
        key = event.key()

        if key == Qt.Key_Left:
            if self.playerLabel.x() > MainWidget.tateCoords[0]:
                self.playerLabel.move(
                    self.playerLabel.x() - 100, self.playerLabel.y())
        if key == Qt.Key_Right:
            if self.playerLabel.x() < MainWidget.tateCoords[4]:
                self.playerLabel.move(
                    self.playerLabel.x() + 100, self.playerLabel.y()
                )
