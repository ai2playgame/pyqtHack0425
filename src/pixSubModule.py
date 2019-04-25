from PyQt5.QtGui import QPixmap


class multiQPixMap():
    def __init__(self, *args):
        self.__imgs = []
        for item in args:
            self.__imgs.append(QPixmap(item))

    def getImg(self, index):
        return self.__imgs[index]
