from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QTextEdit,QVBoxLayout,QGridLayout,QPushButton,QLineEdit,QSizePolicy,QScrollArea,QMessageBox
from PyQt5.QtGui import QIcon,QImage,QPixmap
from PyQt5.QtCore import Qt
import sys

from asset.modules.notesLib.authenticator import createFile,getGrootFolderContent

class noteCreationBox(QWidget):
 
    def __init__(self):
        super(noteCreationBox,self).__init__()
        self.title = 'Note Maker Google Docs'
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.Layout = noteCreationWidgetLayout()
        self.setLayout(self.Layout.noteLayout)
        self.setGeometry(150,150,800,400)
        self.show()


class noteCreationWidgetLayout(QWidget):
    def __init__(self,parent=None):
        super(noteCreationWidgetLayout,self).__init__()
        
        #Elements Present on Note Creation GUI
        self.title = QLabel('Title')
        self.titleEdit = QLineEdit()
        self.summary = QLabel('Summary')
        self.summaryEdit = QTextEdit()
        self.saveButton = QPushButton("Save")
        self.saveButton.clicked.connect(self.createNewFile)
        self.notesList = QPushButton("Notes")
        self.notesList.clicked.connect(self.createNotesList)

        #Main Layout
        self.noteLayout = QGridLayout()

        #Position of Widgets/Elements on Main Layout
        self.noteLayout.addWidget(self.title, 1, 0)
        self.noteLayout.addWidget(self.titleEdit, 1, 1)

        self.noteLayout.addWidget(self.summary, 2, 0)
        self.noteLayout.addWidget(self.summaryEdit, 2, 1, 10, 1)
        
        self.noteLayout.addWidget(self.saveButton,12,0)
        self.noteLayout.addWidget(self.notesList,13,0)

    def createNewFile(self):
        """File is created in Groot/ in Google Drive
        heading: file with title in the GUI is passed as heading
        summary: file content"""

        result = createFile(self.titleEdit.text(),self.summaryEdit.toPlainText())
        if result == 'Successful':
            QMessageBox.about(self, "Successful","File Creation Successful")
        else:
            QMessageBox.about(self,"Warning",result)

    
    def createNotesList(self):
        "Called when note button is clicked.Create scrollable list of notes in new Window"
        
        self.content = getGrootFolderContent()
        print(self.content)
        self.noteWindow = noteShowBox(self.content)
        self.noteWindow.show()


class noteShowBox(QWidget):
    """Class to display already created notes in a window"""

    def __init__(self,content):
        super(noteShowBox,self).__init__()
        self.title = 'Created Notes'
        self.noteContents = content
        self.initUI()
        
    def initUI(self):
        self.mainLayout = QVBoxLayout()
        self.setWindowTitle(self.title)
        self.setGeometry(150,150,800,400)

        self.notes = QScrollArea()
        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_layout.setSpacing(20.0)

        #List Generation of all the notes
        for key,value in self.noteContents.items():
            self.notetile = noteTile(key,value)
            self.scroll_layout.addLayout(self.notetile.noteTileLayout)


        self.notes.setWidget(self.scroll_widget)
        self.mainLayout.addWidget(self.notes)
        self.setLayout(self.mainLayout)
        self.show()
    


class noteTile(QWidget):
    def __init__(self,heading,summary):
        super(noteTile,self).__init__()
        self.heading = QLabel('<b>%s</b>'%heading)
        self.summary = QLabel(summary)

        self.noteTileLayout = QVBoxLayout()

        self.noteTileLayout.addWidget(self.heading)
        self.noteTileLayout.addWidget(self.summary)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = noteCreationBox()
    sys.exit(app.exec_())