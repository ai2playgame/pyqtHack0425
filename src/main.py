import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, pyqtSignal


class MyWidget(QWidget):
    # シグナルを作成
    pressedA = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.show()
        
    def init_ui(self):
        # シグナルとスロットを接続
        # Aボタンが押された->閉じる
        self.pressedA.connect(self.close)
    
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_A:
            # Aボタンが押されたときシグナルを発行
            self.pressedA.emit()

           
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    sys.exit(app.exec_())