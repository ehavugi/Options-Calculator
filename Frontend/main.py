# What is drawn here is the main interface of the UI
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QDesktopWidget,
                             QMessageBox, QMainWindow, QGridLayout, QLabel)
from PyQt5.QtGui import QIcon, QPixmap
import page
import quit
import welcome
import list
import input
import about
import result
import qtawesome


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Add Grid Layout
        # Layout can only be added to Widget
        # Add Widget First
        grid = QGridLayout()
        # This wiedget is the main widget
        # On the left is a column of function keys, and on the right is the page
        self.widget = QWidget()
        self.widget.setObjectName("main")
        self.widget.setLayout(grid)
        self.setCentralWidget(self.widget)
        grid.setSpacing(15)

        # Functions keys on the left
        self.btn_welcome = QPushButton(qtawesome.icon('fa.sellsy'), 'Welcome', self)
        self.btn_welcome.clicked[bool].connect(self.button_clicked)
        self.btn_welcome.setObjectName("left")
        self.btn_input = QPushButton(qtawesome.icon('fa.music'), 'Option parameters', self)
        self.btn_input.clicked[bool].connect(self.button_clicked)
        self.btn_input.setObjectName("left")
        self.btn_result = QPushButton(qtawesome.icon('fa.download'), 'Check price', self)
        self.btn_result.clicked[bool].connect(self.button_clicked)
        self.btn_result.setObjectName("left")
        self.btn_result.setEnabled(False)
        # self.btn_result.setEnabled(True)
        self.btn_list = QPushButton(qtawesome.icon('fa.film'), 'Algorithm review', self)
        self.btn_list.clicked[bool].connect(self.button_clicked)
        self.btn_list.setObjectName("left")
        self.btn_about = QPushButton(qtawesome.icon('fa.star'), 'about Us', self)
        self.btn_about.clicked[bool].connect(self.button_clicked)
        self.btn_about.setObjectName("left")
        self.btn_quit = QPushButton(qtawesome.icon('fa.question'), 'Exit system', self)
        self.btn_quit.clicked[bool].connect(self.button_clicked)
        self.btn_quit.setObjectName("left")
        grid.addWidget(self.btn_welcome, 4, 0)
        grid.addWidget(self.btn_input, 5, 0)
        grid.addWidget(self.btn_result, 6, 0)
        grid.addWidget(self.btn_list, 7, 0)
        grid.addWidget(self.btn_about, 8, 0)
        grid.addWidget(self.btn_quit, 9, 0)

        # Page for each function key
        self.page_welcome = page.page(grid, self)
        welcome.welcome(self.page_welcome)
        self.page_result = page.page(grid, self)
        result.result(self.page_result)
        self.page_list = page.page(grid, self)
        list.list(self.page_list)
        self.page_about = page.page(grid, self)
        about.about(self.page_about)
        self.page_quit = page.page(grid, self)
        quit.quit(self.page_quit)
        self.page_input = page.page(grid, self)
        input.input(self.page_input)
        self.page_welcome.show(self)

        # Add Left function keyss and LOGO to layout
        logo = QLabel(self)
        directory = "img/logo2.png"
        pix = QPixmap(directory)
        logo.setPixmap(pix)
        grid.addWidget(logo, 1, 0, 3, 1)

        # set the title logo
        self.setWindowIcon(QIcon(directory))
        # Center and Draw
        self.resize(1280, 720)
        self.center()
        self.setWindowTitle('MiniSQL')
        # import qss style
        directory = "style.qss"
        with open(directory, 'r') as f:
            qss_style = f.read()
        self.setStyleSheet(qss_style)
        self.show()
        self.button_change(self.btn_welcome)

    def button_change(self, btn):
        self.btn_welcome.setStyleSheet('''QPushButton#left{background-color:}''')
        self.btn_input.setStyleSheet('''QPushButton#left{background-color:}''')
        self.btn_result.setStyleSheet('''QPushButton#left{background-color:}''')
        self.btn_list.setStyleSheet('''QPushButton#left{background-color:}''')
        self.btn_about.setStyleSheet('''QPushButton#left{background-color:}''')
        self.btn_quit.setStyleSheet('''QPushButton#left{background-color:}''')
        btn.setStyleSheet('''QPushButton#left{background-color:white;
                            border-color: red;
                            }''')

    # The effect of pressing each of the left function keys
    def button_clicked(self):
        sender = self.sender()
        if sender.text() == 'Welcome':
            self.page_welcome.show(self)
            self.widget.setStyleSheet('''QWidget#main{border-image:url(img/background.png)}''')
            self.button_change(self.btn_welcome)
        if sender.text() == 'Option parameters':
            self.page_input.show(self)
            self.widget.setStyleSheet('''QWidget#main{border-image:url(img/background_2.png)}''')
            self.button_change(self.btn_input)
        if sender.text() == 'Check price':
            self.page_result.show(self)
            self.widget.setStyleSheet('''QWidget#main{border-image:url(img/background_3.png)}''')
            self.button_change(self.btn_result)
        if sender.text() == 'Algorithm review':
            self.page_list.show(self)
            self.widget.setStyleSheet('''QWidget#main{border-image:url(img/background.png)}''')
            list.list(self.page_list)
            self.button_change(self.btn_list)
        if sender.text() == 'about Us':
            self.page_about.show(self)
            self.widget.setStyleSheet('''QWidget#main{border-image:url(img/background_2.png)}''')
            self.button_change(self.btn_about)
        if sender.text() == 'Exit system':
            self.page_quit.show(self)
            self.widget.setStyleSheet('''QWidget#main{border-image:url(img/background_3.png)}''')
            self.button_change(self.btn_quit)

    # Press the exit key to pop up a confirmation window
    def close_event(self, event):

        reply = QMessageBox.question(self, 'quit',
                                     "Are you sure you want to exit", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    #Centered on startup
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
