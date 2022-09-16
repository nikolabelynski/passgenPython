import sys
import random
import string
import pyperclip
from ui_passgen import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow


class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Slider.valueChanged.connect(self.change)
        self.ui.Copy.clicked.connect(self.copystr)
        self.ui.Refresh.clicked.connect(self.refresh)

    def change(self):
        self.ui.Slider_amount.setText(str(self.ui.Slider.value()))

    def copystr(self):
        pyperclip.copy(self.ui.Password.text())
        test = pyperclip.paste()

    def refresh(self):
        ch = self.ui.Slider.value()

        if (self.ui.Uppercase.isChecked() and self.ui.Lowercase.isChecked() == False) and (self.ui.Numbers.isChecked() == False and self.ui.Symbols.isChecked() == False):
            passw = ''.join(random.choice(string.ascii_uppercase) for i in range(ch))
            return self.ui.Password.setText(str(passw))
            #Only Uppercase
        elif (self.ui.Uppercase.isChecked() == False and self.ui.Lowercase.isChecked()) and (self.ui.Numbers.isChecked() and self.ui.Symbols.isChecked()) == False:
            passw = ''.join(random.choice(string.ascii_lowercase) for i in range(ch))
            return self.ui.Password.setText(str(passw))
            #Only Lowercase
        elif (self.ui.Uppercase.isChecked() and self.ui.Lowercase.isChecked()) == False and (self.ui.Numbers.isChecked() and self.ui.Symbols.isChecked() == False):
            passw = ''.join(random.choice(string.digits) for i in range(ch))
            return self.ui.Password.setText(str(passw))
            #Only Numbers
        elif (self.ui.Uppercase.isChecked() and self.ui.Lowercase.isChecked()) == False and (self.ui.Numbers.isChecked() == False and self.ui.Symbols.isChecked()):
            passw = ''.join(random.choice(string.punctuation) for i in range(ch))
            return self.ui.Password.setText(str(passw))
            #Only Symbols
        elif (self.ui.Uppercase.isChecked() and self.ui.Lowercase.isChecked()) and (self.ui.Symbols.isChecked() == False and self.ui.Numbers.isChecked() == False):
            passw = ''.join(random.choice(string.ascii_letters) for i in range(ch))
            return self.ui.Password.setText(str(passw))
            #Uppercase and Lowercase
        elif (self.ui.Uppercase.isChecked() == False and self.ui.Lowercase.isChecked() == False) and (self.ui.Numbers.isChecked() and self.ui.Symbols.isChecked()):
            passw = ''.join(random.choice(string.digits + string.punctuation) for i in range(ch))
            return self.ui.Password.setText(str(passw))
            #Numbers and Symbols
        elif (self.ui.Uppercase.isChecked() and self.ui.Lowercase.isChecked() == False) and (self.ui.Numbers.isChecked() and self.ui.Symbols.isChecked() == False):
            passw = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(ch))
            return self.ui.Password.setText(str(passw))
            #Uppercase and Numbers
        elif (self.ui.Uppercase.isChecked() and self.ui.Lowercase.isChecked() == False) and (self.ui.Numbers.isChecked() == False and self.ui.Symbols.isChecked()):
            passw = ''.join(random.choice(string.ascii_uppercase + string.punctuation) for i in range(ch))
            return self.ui.Password.setText(str(passw))
            #Uppercase and Symbols
        elif (self.ui.Uppercase.isChecked() == False and self.ui.Lowercase.isChecked()) and (self.ui.Numbers.isChecked() and self.ui.Symbols.isChecked() == False):
            passw = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(ch))
            return self.ui.Password.setText(str(passw))
            #Lowercase and Numbers
        elif (self.ui.Uppercase.isChecked() == False and self.ui.Lowercase.isChecked()) and (self.ui.Numbers.isChecked() == False and self.ui.Symbols.isChecked()):
            passw = ''.join(random.choice(string.ascii_lowercase + string.punctuation) for i in range(ch))
            return self.ui.Password.setText(str(passw))
            #Lowercase and Symbols
        elif (self.ui.Uppercase.isChecked() and self.ui.Lowercase.isChecked()) and (self.ui.Numbers.isChecked() and self.ui.Symbols.isChecked() == False):
            passw = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(ch))
            return self.ui.Password.setText(str(passw))
            #Letters and Numbers
        elif (self.ui.Uppercase.isChecked() and self.ui.Lowercase.isChecked()) and (self.ui.Numbers.isChecked() == False and self.ui.Symbols.isChecked()):
            passw = ''.join(random.choice(string.ascii_letters + string.punctuation) for i in range(ch))
            return self.ui.Password.setText(str(passw))
            #Letters and Symbols
        elif (self.ui.Uppercase.isChecked() and self.ui.Lowercase.isChecked() == False) and (self.ui.Numbers.isChecked() and self.ui.Symbols.isChecked()):
            passw = ''.join(random.choice(string.ascii_uppercase + string.punctuation + string.digits) for i in range(ch))
            return self.ui.Password.setText(str(passw))
            #Uppercase, Numbers and Symbols
        elif (self.ui.Uppercase.isChecked() == False and self.ui.Lowercase.isChecked()) and (self.ui.Numbers.isChecked() and self.ui.Symbols.isChecked()):
            passw = ''.join(random.choice(string.ascii_lowercase + string.punctuation + string.digits) for i in range(ch))
            return self.ui.Password.setText(str(passw))
            #Lowercase, Numbers and Symbols
        elif (self.ui.Uppercase.isChecked() and self.ui.Lowercase.isChecked()) and (self.ui.Numbers.isChecked() and self.ui.Symbols.isChecked()):
            passw = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(ch))
            return self.ui.Password.setText(str(passw))
            #All checked
        else:
            print("something went wrong")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    app.exec()
