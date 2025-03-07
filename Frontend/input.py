from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit, QComboBox, QDateTimeEdit
from PyQt5.QtCore import QDate, QDateTime, QTime


def input(page):
    # 标题
    label_main = QLabel()
    label_main.setFont(page.font_main)
    label_main.setText(" Guiding the country")
    page.grid.addWidget(label_main, 0, 0, 1, 4)

    # 选择当前时间
    label_t0 = QLabel()
    label_t0.setFont(page.font_content)
    label_t0.setText("Current Date")
    page.grid.addWidget(label_t0, 1, 0)
    page.date_edit_t0 = QDateTimeEdit(QDate.currentDate(), page.widget)
    page.date_edit_t0.setDisplayFormat('yyyy-MM-dd')
    page.date_edit_t0.setCalendarPopup(True)
    page.grid.addWidget(page.date_edit_t0, 1, 1)

    # 选择到期时间
    label_t1 = QLabel()
    label_t1.setFont(page.font_content)
    label_t1.setText("Date of Expiry")
    page.grid.addWidget(label_t1, 1, 2)
    page.date_edit_t1 = QDateTimeEdit(QDate.currentDate().addDays(10), page.widget)
    page.date_edit_t1.setDisplayFormat('yyyy-MM-dd')
    page.date_edit_t1.setCalendarPopup(True)
    page.grid.addWidget(page.date_edit_t1, 1, 3)

    # 期权类型 美式欧式
    label_european = QLabel()
    label_european.setFont(page.font_content)
    label_european.setText("American European style")
    page.combo_european = QComboBox(page.widget)
    page.combo_european.addItem("European options")
    page.combo_european.addItem("American options")
    page.grid.addWidget(label_european, 2, 0)
    page.grid.addWidget(page.combo_european, 2, 1)

    # 期权类型 看涨看跌
    label_kind = QLabel()
    label_kind.setFont(page.font_content)
    label_kind.setText("Bullish or Bearish")
    page.combo_kind = QComboBox(page.widget)
    page.combo_kind.addItem("Bullish")
    page.combo_kind.addItem("Bearish")
    page.grid.addWidget(label_kind, 2, 2)
    page.grid.addWidget(page.combo_kind, 2, 3)

    # 标的资产现价
    label_s0 = QLabel()
    label_s0.setFont(page.font_content)
    label_s0.setText("Current price of the underlying asset")
    page.s0 = QLineEdit(page.widget)
    page.s0.setText('100')
    page.grid.addWidget(label_s0, 3, 0)
    page.grid.addWidget(page.s0, 3, 1)

    # 适用的波动率
    label_sigma = QLabel()
    label_sigma.setFont(page.font_content)
    label_sigma.setText("One-year volatility (%）")
    page.sigma = QLineEdit(page.widget)
    page.sigma.setText('1')
    page.grid.addWidget(label_sigma, 3, 2 )
    page.grid.addWidget(page.sigma, 3, 3)

    # 期权执行价
    label_k = QLabel()
    label_k.setFont(page.font_content)
    label_k.setText("option strike price")
    page.k = QLineEdit(page.widget)
    page.k.setText('100')
    page.grid.addWidget(label_k, 4, 0)
    page.grid.addWidget(page.k, 4, 1)

    # 适用的无风险利率
    label_r = QLabel()
    label_r.setFont(page.font_content)
    label_r.setText("One-year simple interest risk-free interest rate (%)")
    page.r = QLineEdit(page.widget)
    page.r.setText('1')
    page.grid.addWidget(label_r, 4, 2)
    page.grid.addWidget(page.r, 4, 3)

    # 股利
    label_dv = QLabel()
    label_dv.setFont(page.font_content)
    label_dv.setText("One-year simple dividend interest rate (%)")
    page.dv = QLineEdit(page.widget)
    page.dv.setText('0')
    page.grid.addWidget(label_dv, 5, 0)
    page.grid.addWidget(page.dv, 5, 1)

    # 占空位
    label_blank = QLabel()
    page.grid.addWidget(label_blank,6,0,1,4)

    # 蒙特卡罗迭代次数
    label_mc = QLabel()
    label_mc.setFont(page.font_content)
    label_mc.setText("Number of Monte Carlo iterations")
    page.mc = QLineEdit(page.widget)
    page.mc.setText('100000')
    page.grid.addWidget(label_mc, 7, 0)
    page.grid.addWidget(page.mc, 7, 1)

    # 二叉树迭代次数
    label_bt = QLabel()
    label_bt.setFont(page.font_content)
    label_bt.setText("Number of binary tree iterations")
    page.bt = QLineEdit(page.widget)
    page.bt.setText('500')
    page.grid.addWidget(label_bt, 7, 2)
    page.grid.addWidget(page.bt, 7, 3)

    # 确定输入按键
    btn_confirm = QPushButton('Confirm input')
    page.grid.addWidget(btn_confirm, 8, 0, 1, 4)
    btn_confirm.setStyleSheet('''
            QPushButton:hover{color:red}
            QPushButton{font-size:18px;
                        font-weight:200;
            }''')
    btn_confirm.clicked.connect(page.confirm)
