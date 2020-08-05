import numpy as np
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication,  QLineEdit , QWidget ,QFormLayout,QPushButton,QMessageBox,QLabel,QVBoxLayout,QSizePolicy
import sys 
import random
import matplotlib.pyplot as plt
from numpy.linalg import cholesky
 
Alist=[]
Blist=[]
Clist=[]
Astr=[]
Bstr=[]
q=[]

#事实上UI的设计直接运用PyQt5-tools中的designer可以自动生成代码
class initUI(QWidget):
	def __init__(self):
		super(initUI, self).__init__()    #继承QWidget的父类的所有方法和属性
		self.setWindowTitle("数字波形生成器")  #自定义标题控件
		self.resize(300,250)   #自定义界面长宽
		flo = QFormLayout()    #垂直布局管理
		#设置四行单行文本框
		self.Asequence = QLineEdit()   
		self.Bsequence = QLineEdit()
		self.Fexpression = QLineEdit()
		self.Csequence = QLineEdit()
                #后置一个标签
		self.bupt = QLabel("by 李子桐 2020.4.20")
		#设置按钮
		self.btn_1 = QPushButton('运算') 
		self.btn_2 = QPushButton("画图")
		#设置掩码，B表示允许三十二进制字符，此处最大为32位
		self.Asequence.setInputMask("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
		self.Bsequence.setInputMask("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
		#把文本框添加到布局，第一个参数为左侧的说明标签
		flo.addRow("A序列",self.Asequence)
		flo.addRow("B序列", self.Bsequence)
		flo.addRow("F表达式",self.Fexpression)
		flo.addRow("运算结果",self.Csequence)
		#把按钮与标签添加到布局
		flo.addWidget(self.btn_1) 
		flo.addWidget(self.btn_2)
		flo.addWidget(self.bupt)
		#渲染到框内
		self.setLayout(flo)
		#渲染click控件
		self.btn_1.clicked.connect(self.on_click)
		self.btn_2.clicked.connect(self.paintA)

	#点击计算的算法
	def  on_click(self):
            
		Astr=self.Asequence.text()
		Bstr=self.Bsequence.text()
		
		#清除上一次列表中的记录，使程序可以重复工作
		Alist.clear()
		Blist.clear()
		q.clear()

		#生成元组，将每一位一一对应加入列表
		for(i,j) in zip(Astr,Bstr):
			Alist.append(int(i))
			Blist.append(int(j))
                
		F=self.Fexpression.text()       #取出F的表达式，用A，B做变量名
		for (A,B) in zip(Alist,Blist):
			q.append(eval(F))       #计算F的值，并加入列表
		i = 0
		print(q)
		#while(i < len(q)):
		#	if (q[i] == 1 | q[i] == -1):
		#		q[i] = 1
		#	else:
		#		q[i] = 0
		#	i = i + 1

		num_list_new = [str(x) for x in q] #生成一个列表，元素为q中的元素
		re=" ".join(num_list_new)       #在num_list_new中加入空格
		self.Csequence.setText(re)      #设置框中的内容

        #点击画图的算法
	def paintA(self):
		yA=[]
		yB=[]
		yC=[]
		#生成外框
		plt.figure()
		#生成列表，从1开始，上式输入的位数，间隔为0.1的列表，相当于做了一次取样
		x=np.arange(1,len(Alist),0.01)
		#进行多次赋值，频率为0.01，确保精度
		for i in x:
			if(Alist[int(i)]==1):
				yA.append(1)
			else :
				yA.append(0)
		for j in x:
			if(Blist[int(j)]==1):
				yB.append(1)
			else :
				yB.append(0)
		for k in x:
			if(q[int(k)]==1):
				yC.append(1)
			else :
				yC.append(0)
		#进行布局与标签，再画出图像，与matlab一样
		ax1=plt.subplot(221)
		ax1.set_title("A")
		plt.plot(x,yA)
		ax2 = plt.subplot(222)
		ax2.set_title("B")
		plt.plot(x,yB)
		ax3 = plt.subplot(212)
		ax3.set_title("C")
		plt.plot(x,yC)
		
		plt.show()
		
 
if __name__ == "__main__":       
	app = QApplication(sys.argv)    #实例化引用对象
	first= initUI()         #实例化initUI
	first.show()            #显示大UI
	sys.exit(app.exec_())   #退出程序

