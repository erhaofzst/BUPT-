import numpy as np
from numpy import linalg
import matplotlib.pyplot as plt
import math
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,  QLineEdit , QWidget ,QFormLayout,QPushButton,QMainWindow
import sys 






#时间长度
t_len = 15
#分割时间
t = np.linspace(0, t_len, 1000)
#傅里叶变换原函数g_t(t)
g_t = []
for i in range(len(t)):
    #测试函数
    temp = 2*math.sin(2*np.pi*0.5*t[i])+math.sin(2*np.pi*t[i])+3*math.sin(2*np.pi*1.5*t[i])
    g_t.append(temp)

#频率范围
f_len = 3
#分割频率
f = np.linspace(0, f_len, 1000)
#傅里叶变换函数轴函数g_sin(f)，x轴函数
g_sin = []
#傅里叶变换函数虚轴函数g_cos(f)，y轴函数
g_cos = []
#傅里叶变换 复数模 函数g_f(f)，偏离中心距离函数
g_f = []
#傅里叶函数虚轴和实轴存在的意义在于区分振动中不同方向的增益效果
#所谓虚函数只是一种区分方向的方式，不让cos()与sin()在积分前混合
#傅里叶变换，时间进行积分
for c_f in range(len(f)):
    sinsum = 0
    cossum = 0
    for c_t in range(len(t)):
        tempsin = g_t[c_t] * math.sin(f[c_f] * t[c_t] * (-2 * math.pi))
        tempcos = g_t[c_t] * math.cos(f[c_f] * t[c_t] * (-2 * math.pi))
        sinsum = sinsum + tempsin
        cossum = cossum + tempcos
    g_f.append(math.sqrt((cossum/len(t))**2 + (sinsum/len(t))**2))
    g_sin.append(sinsum/len(t))
    g_cos.append(cossum/len(t))

g_sin = list(map(lambda x:(0.5)*np.pi*x,g_sin))
g_sin1 = list(map(lambda x:(-1)*x,g_sin))
g_sin1 = g_sin1[::-1]
g_sin1.extend(g_sin)
g_f1 = list(map(lambda x:2*x,g_f))


g_f2 = g_f[::-1]
g_f2.extend(g_f)
f1 = np.linspace((-1)*f_len, f_len, 2000)


#逆傅里叶变换还原后函数f_g(t)
f_g = []

for c_t in range(len(t)):
    sinsum = 0
    cossum = 0
    for c_f in range(len(f)):
        tempsin = g_sin[c_f] * math.sin(f[c_f] * t[c_t] * (-2 * math.pi))
        tempcos = g_cos[c_f] * math.cos(f[c_f] * t[c_t] * (-2 * math.pi))
        sinsum = sinsum + tempsin
        cossum = cossum + tempcos
    f_g.append(2*f_len*t_len*sinsum/len(f) + 2*f_len*t_len*cossum/len(f))
fig = plt.figure("Fourier",figsize=(12, 6.5))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'one.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(293, 319)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 110, 231, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 160, 231, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 50, 271, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 20, 171, 31))
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 210, 231, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 260, 231, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(80, 80, 121, 16))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.yuanbo)
        self.pushButton_2.clicked.connect(self.fupin)
        self.pushButton_3.clicked.connect(self.xiangpin)
        self.pushButton_4.clicked.connect(self.fanbianhuan)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "看看原始波形"))
        self.pushButton_2.setText(_translate("Form", "看看变换后频域结果幅度谱"))
        self.label.setText(_translate("Form", "2sin(pi*t)+sin(2pi*t)+3sin(3pi*t)"))
        self.label_2.setText(_translate("Form", "傅里叶变换代码演示"))
        self.pushButton_3.setText(_translate("Form", "看看变换后频域结果频谱谱"))
        self.pushButton_4.setText(_translate("Form", "看看傅里叶反变换后波形"))
        self.label_3.setText(_translate("Form", "以此函数进行演示"))

    def yuanbo(self):
        plt.close()
        plt.plot(t, g_t, color='red')
        plt.title("Original f(t)")
        plt.show()
    def fupin(self):
        plt.close()
        plt.plot(f1, g_f2, color='teal')
        plt.title("Amplitude Frequency Characteristic |F(w)|")
        plt.show()
    def xiangpin(self):
        plt.close()
        plt.plot(f1, g_sin1,  color='teal')
        plt.title("Phase Frequency Characteristic φ(w) ")
        plt.show()
    def fanbianhuan(self):
        plt.close()
        plt.plot(t, f_g, color='blue')
        plt.title("Fourier Inversion f(t)")
        plt.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QWidget()
    main_ui = Ui_Form()
    main_ui.setupUi(main)
    main.show()
    sys.exit(app.exec_())
