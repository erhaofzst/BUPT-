#！/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal
import pylab as pl#导入一个绘图模块，matplotlib下的模块
#其中需要输入一个更新数据的函数来为fig提供新的绘图信息
import scipy.signal
from matplotlib.pyplot import MultipleLocator
import pylab as pl#导入一个绘图模块，matplotlib下的模块



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,  QLineEdit , QWidget ,QFormLayout,QPushButton,QMainWindow
import sys 


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(249, 305)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 60, 131, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 30, 131, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(140, 90, 81, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 131, 16))
        self.label_3.setObjectName("label_3")
        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(40, 130, 160, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 221, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 190, 161, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 240, 161, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.yuanbo)
        self.pushButton_2.clicked.connect(self.sample)
        self.horizontalSlider.setMinimum(250)
        self.horizontalSlider.setMaximum(500)
        self.horizontalSlider.setSingleStep(1)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "A*cos(2*pi*f*t)"))
        self.label_2.setText(_translate("Form", "采样定理动画演示"))
        self.label_3.setText(_translate("Form", "设置幅值A（V）："))
        self.label_4.setText(_translate("Form", "设置原波频率f（Hz）100~250"))
        self.pushButton.setText(_translate("Form", "看看原波"))
        self.pushButton_2.setText(_translate("Form", "看看采样动画"))
    def yuanbo(self):
        plt.close()
        fs_List = np.arange(99, 1000, 50)
        t = np.arange(0, 0.0101, 0.00001)
        
        A = int(self.lineEdit.text())
        f0 = self.horizontalSlider.value()
        F = A*np.cos(2*np.pi*f0*t) #原函数
        print(f0)
        plt.xlim(0, 0.01)
        plt.ylim(-A-1, A+1)
        plt.plot(t, F, "r", label="Orignal")
        plt.show()
    def sample(self):
        plt.close()
        fs_List = np.arange(99, 1000, 50)
        t = np.arange(0, 0.0101, 0.00001)
        A = int(self.lineEdit.text())
        f0 = self.horizontalSlider.value()
        print(f0)
        F = A*np.cos(2*np.pi*f0*t) #原函数
        plt.ion()#开启交互模式
        plt.figure(figsize=(12, 5))
        for fs in fs_List:
            #设置画布外观
            plt.cla()
            plt.grid(True)
            plt.xlim(0, 0.01)
            plt.ylim(-A-1, A+1)
            plt.ylabel("Amplitude")
            plt.title("fs=%ffo"%(fs/f0))
            ##设置横坐标间距
            x_major_locator=MultipleLocator(0.001)
            ax=plt.gca()
            ax.xaxis.set_major_locator(x_major_locator)
            #设置图像线条
            Ts = 1 / fs
            Points_x = np.arange(-1, 1.001, Ts)
            Points_y = A*np.cos(2*np.pi*f0*Points_x)#抽样点
            fa = []
            for tt in t:
                fa.append(np.dot(Points_y, np.sinc(fs*(tt-Points_x))))#抽样后还原函数
            #画图
            plt.plot(t, F, "r", label="Orignal")
            plt.plot(Points_x, Points_y, "ro" ,markersize=15, label="Sampling Points")
            plt.plot(t, fa, "--",color = 'teal', label="Restoration")
            ##设置图例
            plt.legend(["Orignal", "Sampling Points", "Restoration"],
                mode="expand", bbox_to_anchor=(0., 1.07, 1., .07), ncol=3, fancybox=True)
            plt.pause(0.5)
        plt.ioff()
        plt.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QWidget()
    main_ui = Ui_Form()
    main_ui.setupUi(main)
    main.show()
    sys.exit(app.exec_())