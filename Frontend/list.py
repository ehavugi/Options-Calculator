from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QLabel


def list(page):
    # Title
    label_main = QLabel()
    label_main.setFont(page.font_main)
    label_main.setText("-A bird's eye view")
    page.grid.addWidget(label_main, 0, 0)
    # text
    label_content = QLabel()
    label_content.setFont(page.font_content)
    label_content.setText("      This is an Algorithm exhbition\n")
    page.grid.addWidget(label_content, 1, 0)
    # B-S Model
    label_bs = QLabel()
    label_bs.setFont(page.font_content)
    label_bs.setText("      B-S Model\n")
    page.grid.addWidget(label_bs, 3, 0)
    webview_bs = QWebEngineView()
    webview_bs.setUrl(
        QUrl('https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model'))  # Add an english version. Another way would be to translate
    # webview_bs.setUrl(
    #     QUrl('https://wiki.mbalib.com/wiki/Black-Scholes%E6%9C%9F%E6%9D%83%E5%AE%9A%E4%BB%B7%E6%A8%A1%E5%9E%8B'))
    webview_bs.show()
    page.grid.addWidget(webview_bs, 4, 0)
    # Blank
    label_empty = QLabel()
    page.grid.addWidget(label_empty, 4, 0)
