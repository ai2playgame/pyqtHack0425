import random

from PyQt5.QtGui import QPixmap


class PickItemBase():
    def __init__(self, *args):
        self.imgs = []
        for i in args:
            self.imgs.append(QPixmap(i))
        self.imgsPath = args

    def getImgCopy(self, index):
        return (self.__imgs.getImg())

    def getRandomImgCopy(self):
        return (random.choice(self.imgs))

    def getRandomImgPath(self):
        return random.choice(self.imgs)


class PlusItem(PickItemBase):
    def __init__(self):
        super(PlusItem, self).__init__("../img/math.png",
                                       "../img/kokugo.png",
                                       "../img/english.png",
                                       "../img/science.png",
                                       "../img/shakai.png")


class MinusItem(PickItemBase):
    def __init__(self):
        super(MinusItem, self).__init__("../img/mayaku.png",
                                        "../img/shounenin.png")
