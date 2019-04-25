from PyQt5.QtWidgets import QWidget, QLabel
import pickItem


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt Project'
        self.left = 300
        self.top = 300
        self.width = 1000
        self.height = 800
        self.preLoadImg()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create Widget
        label = QLabel(self)
        label.setPixmap(self.items.getRandomImgCopy())
        label.move(500, 50)
        self.show()

    def preLoadImg(self):
        self.items = pickItem.PlusItem()
