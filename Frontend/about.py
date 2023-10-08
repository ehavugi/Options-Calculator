from PyQt5.QtWidgets import QLabel


def about(page):
    # title
    label_main = QLabel()
    label_main.setFont(page.font_main)
    label_main.setText("self-recommendation")
    page.grid.addWidget(label_main, 0, 0)
    # text
    label_content = QLabel()
    label_content.setFont(page.font_content)
    label_content.setText("\t\tThis is the developer of the option price calculator. \n\t\tTo protect your use. \n\t\tCome and go in a hurry, please give me some advice.")
    page.grid.addWidget(label_content, 1, 0)
    # another text
    label_content = QLabel()
    label_content.setFont(page.font_content)
    label_content.setText("\t\tYang Yuhao 3160105521\n\t\tZhang Tiannuan 3160103915\n\t\tCheng Long 3160104356")
    page.grid.addWidget(label_content, 2, 0, 1, 1)
    # Github Page
    label_empty = QLabel()
    label_empty.setFont(page.font_content)
    label_empty.setText("\t\tThis is the project's Github [SOURCE] repository page\n\t\thttps://github.com/QSCTech-Sange/Options-Calculator")
    page.grid.addWidget(label_empty, 4, 0)