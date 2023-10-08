from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QPushButton, QLabel


def quit(page):
    # title
    label_main = QLabel()
    label_main.setFont(page.font_main)
    label_main.setText("Goodbye Jianghu")
    page.grid.addWidget(label_main, 0, 0)
    # text
    label_content = QLabel()
    label_content.setFont(page.font_content)
    label_content.setText("I have no intention of leaving or leaving, just look at the clouds rolling in the sky.\n I have passed through thousands of waters and look forward to a gentle reunion with you.")
    page.grid.addWidget(label_content, 1, 0)
    # Hold the blank space
    label_empty = QLabel()
    page.grid.addWidget(label_empty, 2, 0, 2, 1)
    # Exit title
    qbtn = QPushButton('Decided to leave')
    qbtn.clicked.connect(QCoreApplication.instance().quit)
    qbtn.setStyleSheet('''
        QPushButton:hover{color:red}
        QPushButton{font-size:30px;
                    font-weight:200;
        }''')
    page.grid.addWidget(qbtn, 4, 0)