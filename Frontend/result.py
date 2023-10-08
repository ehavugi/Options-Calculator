from PyQt5.QtWidgets import QLabel, QLineEdit


def result(page):
    # title
    label_main = QLabel()
    label_main.setFont(page.font_main)
    label_main.setText("stimulating text")
    page.grid.addWidget(label_main, 0, 0, 1, 2)
    # Word
    label_hint = QLabel()
    label_hint.setFont(page.font_content)
    label_hint.setText(" Sort out the calculation results of option prices for you")
    page.grid.addWidget(label_hint, 1, 0, 1, 2)

    # BS price
    label_content = QLabel()
    label_content.setFont(page.font_content)
    label_content.setText("BS method to calculate price")
    page.grid.addWidget(label_content, 2, 0)
    page.line_bs = QLineEdit(page.widget)
    page.line_bs.setEnabled(False)
    page.line_bs.setStyleSheet("QLineEdit{background-color:white;color:black}")
    page.grid.addWidget(page.line_bs, 2, 1)

    #MCPrice
    label_mc = QLabel()
    label_mc.setFont(page.font_content)
    label_mc.setText("Monte Carlo method to calculate price")
    page.grid.addWidget(label_mc, 3, 0)
    page.line_mc = QLineEdit(page.widget)
    page.line_mc.setEnabled(False)
    page.line_mc.setStyleSheet("QLineEdit{background-color:white;color:black}")
    page.grid.addWidget(page.line_mc, 3, 1)

    # Binary tree price
    label_bt = QLabel()
    label_bt.setFont(page.font_content)
    label_bt.setText("Binary number method to calculate price")
    page.grid.addWidget(label_bt, 4, 0)
    page.line_bt = QLineEdit(page.widget)
    page.line_bt.setEnabled(False)
    page.line_bt.setStyleSheet("QLineEdit{background-color:white;color:black}")
    page.grid.addWidget(page.line_bt, 4, 1)