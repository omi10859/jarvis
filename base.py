from PyQt5.QtWidgets import QApplication
from faceUnlocker import unlock
from texttospeech import speak_this
import sys
 

from Gui import Groot_Ui


if __name__ == '__main__':
    app = QApplication(sys.argv)
    groot = Groot_Ui()   #! Groot UI defined in the Gui.py file
    sys.exit(app.exec_())
