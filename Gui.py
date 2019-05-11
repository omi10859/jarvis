from PyQt5.QtWidgets import QWidget,QLabel,QLineEdit,QGridLayout,QPushButton,QMessageBox,QComboBox,QApplication,QVBoxLayout,QTabWidget,QScrollArea,QFormLayout,QSizePolicy
from PyQt5.QtGui import QIcon,QImage,QPixmap
from PyQt5.QtCore import Qt

from speechtotext import listen
from texttospeech import speak_this
from groot import input_taking
from newsWindow import newsBox

from mailWindow import mailWin

from notesWindow import noteCreationBox

from asset.modules.newsLib.newsLibrary import news_func
from bored import boredomKiller


class Groot_Ui(QWidget):
    def __init__(self):
        super(Groot_Ui,self).__init__()
        self.initUI()

    def initUI(self):
        self.mainLayout = QVBoxLayout()
        self.upperLayout = inpOutWidgetLayout()
        self.mainLayout.addLayout(self.upperLayout.inpOutLayout)
        self.mainLayout.addStretch(1)
        
        self.setLayout(self.mainLayout)
        self.setWindowTitle('GROOT')
        self.setWindowIcon(QIcon('asset/img/groot.png'))
        self.setGeometry(150,150,800,100)
        self.show()

        #Other Functions:
        self.upperLayout.speaker.clicked.connect(self.listen_reply)
        self.upperLayout.inputEdit.returnPressed.connect(self.callGroot)


    


    def createAdditionalLayout(self, keywords,type):
        if type == "news":
            print(keywords)
            self.newsWindow = newsBox(keywords)
            self.newsWindow.show() 
        

        if type == "mail":
            print("Showing notes")
            self.mailWindow = mailWin()
            self.mailWindow.show()

    def createNewsLayout(self, keywords):
        print(keywords)
        self.newsWindow = newsBox(keywords)
        self.newsWindow.show() 

        if type == "notes":
            print("Showing notes")
            self.noteWindow = noteCreationBox()
            self.noteWindow.show()



    #Function for typing in the input Field
    def callGroot(self):
        typed = str(self.upperLayout.inputEdit.text())
        reply = input_taking(typed)
        if reply[0] == 'news':
            speak_this("Showing news")
            self.upperLayout.outputEdit.setText("Showing news")


        
        elif reply[0] == 'notes':
            speak_this("Opening Notes")
            self.upperLayout.outputEdit.setText("Showing Note Widget")
            self.createAdditionalLayout(["No need"],type="notes")
        
        else:    
            self.upperLayout.outputEdit.setText(reply[1])


        elif reply[0] == 'mail':
            speak_this("Opening Mail Service")
            self.upperLayout.outputEdit.setText("Mail Service")
            self.createAdditionalLayout(reply[1],type="mail")

        else:
            self.upperLayout.outputEdit.setText(reply[1])
            
    def listen_reply(self):
        spoken = listen()
        reply = input_taking(spoken)
        if reply[0] == 'news':
            self.upperLayout.outputEdit.setText("Showing news")
            speak_this("Showing news")
            print(reply[1])
            self.createAdditionalLayout(reply[1],type="news")

        
        elif reply[0] == 'mail':
            self.upperLayout.outputEdit.setText("Mail Service")
            speak_this("Opening Mail Service")
            self.createAdditionalLayout(reply[1],type="mail")

               
        elif reply[0] == 'notes':
            speak_this("Opening Notes")
            self.upperLayout.outputEdit.setText("Showing Note Widget")
            self.createAdditionalLayout(["No need"],type="notes")

        elif reply[0] == 'surprise':
            speak_this("I have a cure for Boredom")
            self.upperLayout.outputEdit.setText("Check Your Browser")
            self.bore()


        else:
            self.upperLayout.outputEdit.setText(reply[1])



    def bore(self):
        boredomKiller()



    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:                
            self.close()

    #Function to display warning message for quitting
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?",
        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class inpOutWidgetLayout(QVBoxLayout):
    def __init__(self,parent=None):
        super(inpOutWidgetLayout,self).__init__()
        #Grid Layout for the upper part.
        self.inpOutLayout = QGridLayout()

        self.inputLabel = QLabel('Input')
        self.inputLabel.setMinimumSize(self.sizeHint())
        self.outputLabel = QLabel('Output')
        self.inputLabel.setMinimumSize(self.sizeHint())
        #Speaker Widget
        self.speaker = QPushButton('Speak')
        self.speaker.setMinimumSize(self.sizeHint())
        #Text Field for Input
        self.inputEdit = QLineEdit()
        self.inputEdit.setMinimumSize(self.sizeHint()) 
        #Text Field for Output
        self.outputEdit = QLineEdit()
        self.outputEdit.setMinimumSize(self.sizeHint())
        #Spacing between the widgets
        self.inpOutLayout.setSpacing(20)
        #Positioning Inner Widgets
        self.inpOutLayout.addWidget(self.inputLabel, 1, 0)
        self.inpOutLayout.addWidget(self.inputEdit, 1, 1)
        self.inpOutLayout.addWidget(self.speaker,1,2)
        self.inpOutLayout.addWidget(self.outputLabel, 2, 0)
        self.inpOutLayout.addWidget(self.outputEdit, 2, 1)

        #Button is needed in parallel.
        
        


