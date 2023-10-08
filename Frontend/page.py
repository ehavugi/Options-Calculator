# 存放按下每个功能键的主页面
import sys
from threading import Thread

sys.path.append("..")
from PyQt5.QtWidgets import (QWidget, QMessageBox, QGridLayout)
from PyQt5.QtGui import QFont
from Backend.Option import Option
import numpy as np


class Calculatebt(Thread):

    def __init__(self, option, btstep):
        super().__init__()
        self.option = option
        self.btstep = btstep

    def run(self):
        self.option.bt(self.btstep)

class Calculatemc(Thread):

    def __init__(self, option, mcstep):
        super().__init__()
        self.option = option
        self.mcstep = mcstep

    def run(self):
        self.option.mc(self.mcstep)

class Calculatebs(Thread):

    def __init__(self, option):
        super().__init__()
        self.option = option

    def run(self):
        self.option.bs()

class page:
    def __init__(self, grid, mw):
        self.mw = mw
        self.widget = QWidget()
        self.grid = QGridLayout()
        self.grid.setSpacing(20)
        self.widget.setLayout(self.grid)
        grid.addWidget(self.widget, 1, 1, 13, 4)
        #Set title font
        self.font_main = QFont()
        self.font_main.setFamily('Microsoft Yahei')
        self.font_main.setPointSize(70)
        self.font_main.setWeight(40)
        # Set text font
        self.font_content = QFont()
        self.font_content.setFamily('Microsoft Yahei')
        self.font_content.setPointSize(15)
        self.font_content.setWeight(40)
        # Properties of some option parameters
        self.combo_kind = None
        self.combo_european = None
        self.s0 = None
        self.date_edit_t1 = None
        self.sigma = None
        self.date_edit_t0 = None
        self.r = None
        self.k = None
        self.dv = None
        self.bsprice = None
        self.mcprice = None
        self.btprice = None
        self.mc = None
        self.bt = None

    def show(self, mw):
        mw.page_quit.widget.hide()
        mw.page_welcome.widget.hide()
        mw.page_input.widget.hide()
        mw.page_result.widget.hide()
        mw.page_list.widget.hide()
        mw.page_about.widget.hide()
        self.widget.show()

# Confirm input
    def confirm(self):
        try:
            if self.combo_kind.currentText() == "bullish":
                kind = 1
            else:
                kind=-1
            if self.combo_european.currentText() == "American Option":
                european=False
            else:
                european=True
            s0 = float(self.s0.text())
            k = float(self.k.text())
            sigma = float(self.sigma.text()) / 100
            r = float(self.r.text()) / 100
            r = np.log(1 + r)
            t1 = self.date_edit_t1.date()
            t0 = self.date_edit_t0.date()
            t = t0.daysTo(t1)
            dv = float(self.dv.text()) / 100
            dv = np.log(1 + dv)
            mcstep = int(self.mc.text())
            btstep = int(self.bt.text())
            option = Option(european, kind, s0, k, t, r, sigma, dv)
            t1 = Calculatebs(option)
            t2 = Calculatebt(option,btstep)
            t3 = Calculatemc(option,mcstep)
            t1.start()
            t2.start()
            t3.start()
            QMessageBox.about(self.widget,
                              "hint",
                              "Calculating option prices...\nPlease wait patiently!")

            t1.join()
            t2.join()
            t3.join()
            QMessageBox.about(self.widget,
                             "hint",
                              "The option price has been calculated\nCheck it out in the View Results tab!")
            self.mw.page_result.line_bs.setText(str(option.bsprice))
            self.mw.page_result.line_mc.setText(str(option.mcprice))
            self.mw.page_result.line_bt.setText(str(option.btprice))
            self.mw.page_result.show(self.mw)
            self.mw.widget.setStyleSheet('''QWidget#main{border-image:url(img/background_3.png)}''')
            self.mw.button_change(self.mw.btn_result)
            self.mw.btn_result.setEnabled(True)
        except ValueError:
            QMessageBox.about(self.widget,
                              "hint",
                              "Your input is incorrect...\nPlease check carefully!")
        except ZeroDivisionError:
            QMessageBox.about(self.widget,
                              "hint",
                              "The two dates should be set to different times\nThe volatility cannot be 0\nThe option strike price cannot be 0")
