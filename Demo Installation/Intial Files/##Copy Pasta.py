##Copy Pasta

self.pushButton.clicked.connect(lambda: self.enroll(self.roll_number_edit.text(),self.password_edit.text()))
def enroll(self,id,pswd):
        call_chrome(id,pswd)


self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)