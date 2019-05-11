from PyQt5.QtWidgets import QApplication,QPushButton,QWidget, QMessageBox, QTextEdit, QLabel, QLineEdit, QGridLayout,QGridLayout
from asset.modules.mailLib.mailreply import shootMail

import sys

class mailWin(QWidget):
    def __init__(self):
        super(mailWin,self).__init__()
        self.title = 'Mail Window'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.Layout = QGridLayout()
        self.setLayout(self.Layout)
        self.setGeometry(150,150,800,400)

        details = {'From':'From','To':'To','Subject':'Subject','Message':'Message'}
        self.passwordText = ""

        self.sender = QLabel('<b>%s</b>'%details['From'])
        self.receiver = QLabel('<b>%s</b>'%details['To'])
        self.subject = QLabel('<b>%s</b>'%details['Subject'])
        self.message = QLabel('<b>%s</b>'%details['Message'])

        self.senderEdit = QLineEdit()
        self.receiverEdit = QLineEdit()
        self.subjectEdit = QLineEdit()
        self.messageEdit = QTextEdit()

        self.sendButton = QPushButton('Send')

        self.Layout.addWidget(self.sender,1,0)
        self.Layout.addWidget(self.senderEdit,1,1)
        self.Layout.addWidget(self.receiver,2,0)
        self.Layout.addWidget(self.receiverEdit,2,1)
        self.Layout.addWidget(self.subject,3,0)
        self.Layout.addWidget(self.subjectEdit,3,1)
        self.Layout.addWidget(self.message,4,0)
        self.Layout.addWidget(self.messageEdit,4,1)

        self.Layout.addWidget(self.sendButton,5,0)

        self.sendButton.clicked.connect(self.resourceCollection)

        self.show()

    def passwordCollection(self):
        details = {'Sender':self.senderEdit.text(),'Receiver':self.receiverEdit.text(),'Subject':self.subjectEdit.text(),'Message':self.messageEdit.toPlainText()}
        self.passwordText = self.confirmWindow.passwordEdit.text()
        details['Password'] = self.passwordText
        print(details['Password'])
        reply = shootMail(details)
        if reply == 'Success':
            QMessageBox.about(self, "Successful","Mail Sent Succesfully")
        else:
            QMessageBox.about(self,"Warning Error Occured",result)

    def resourceCollection(self):
        details = {'Sender':self.senderEdit.text()}
        self.confirmWindow = confirmWin(details['Sender'])
        self.confirmWindow.show()
        print("Reached Here")
        self.confirmWindow.send.clicked.connect(self.passwordCollection)

class confirmWin(QWidget):
    def __init__(self,sender):
        super(confirmWin,self).__init__()
        self.title = 'Confirmation'
        self.sender = sender
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Confirmation for Password')
        self.confirmLayout = QGridLayout()

        details = {'From':'From','Password':'Password'}

        self.frm = QLabel('<b>%s</b>'%details['From'])
        self.sender = QLabel('<b>%s</b>'%self.sender)
        self.password = QLabel('<b>%s</b>'%details['Password'])
        self.passwordEdit = QLineEdit()
        self.passwordEdit.setEchoMode(QLineEdit.Password)
        self.send = QPushButton('SEND')

        self.confirmLayout.addWidget(self.frm,1,0)
        self.confirmLayout.addWidget(self.sender,1,1)
        self.confirmLayout.addWidget(self.password,2,0)
        self.confirmLayout.addWidget(self.passwordEdit,2,1)
        self.confirmLayout.addWidget(self.send,3,0)

        self.setLayout(self.confirmLayout)
        self.setGeometry(150,150,400,200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    groot = mailWin()   #! Groot UI defined in the ui.py file
    sys.exit(app.exec_())