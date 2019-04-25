import sys
from PyQt5.QtWidgets import QApplication
from AiMainWidget import mainWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = mainWidget()
    sys.exit(app.exec_())
