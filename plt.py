from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView, QFileSystemModel, QVBoxLayout, QPushButton, QWidget, QFileDialog
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QInputDialog, QMessageBox
import pandas
import numpy
import matplotlib.pyplot as plt

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(650, 550)
        Form.setMinimumSize(QtCore.QSize(650, 550))
        Form.setMaximumSize(QtCore.QSize(650, 550))
        Form.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.xMinPushButton = QtWidgets.QPushButton(Form)
        self.xMinPushButton.setGeometry(QtCore.QRect(60, 130, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.xMinPushButton.setFont(font)
        self.xMinPushButton.setMouseTracking(False)
        self.xMinPushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10;\n"
"border: 1px solid black;")
        self.xMinPushButton.setObjectName("xMinPushButton")
        self.xminLineEdit = QtWidgets.QLineEdit(Form)
        self.xminLineEdit.setGeometry(QtCore.QRect(200, 130, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.xminLineEdit.setFont(font)
        self.xminLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10;\n"
"border: 1px solid black;")
        self.xminLineEdit.setObjectName("xminLineEdit")
        self.xmaxLineEdit = QtWidgets.QLineEdit(Form)
        self.xmaxLineEdit.setGeometry(QtCore.QRect(200, 180, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.xmaxLineEdit.setFont(font)
        self.xmaxLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10;\n"
"border: 1px solid black;")
        self.xmaxLineEdit.setObjectName("xmaxLineEdit")
        self.browserPushButton = QtWidgets.QPushButton(Form)
        self.browserPushButton.setGeometry(QtCore.QRect(460, 30, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.browserPushButton.setFont(font)
        self.browserPushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.browserPushButton.setAutoFillBackground(False)
        self.browserPushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;\n"
"border-radius:10;")
        self.browserPushButton.setObjectName("browserPushButton")
        self.xLineInterval = QtWidgets.QLineEdit(Form)
        self.xLineInterval.setGeometry(QtCore.QRect(340, 380, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.xLineInterval.setFont(font)
        self.xLineInterval.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10;\n"
"border: 1px solid black;")
        self.xLineInterval.setObjectName("xLineInterval")
        self.browserLineEdit = QtWidgets.QLineEdit(Form)
        self.browserLineEdit.setGeometry(QtCore.QRect(60, 30, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.browserLineEdit.setFont(font)
        self.browserLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;\n"
"border-radius:10\n"
"")
        self.browserLineEdit.setObjectName("browserLineEdit")
        self.plotPushButton = QtWidgets.QPushButton(Form)
        self.plotPushButton.setGeometry(QtCore.QRect(230, 440, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.plotPushButton.setFont(font)
        self.plotPushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.plotPushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10;\n"
"border: 1px solid black;")
        self.plotPushButton.setObjectName("plotPushButton")
        self.xMaxPushButton = QtWidgets.QPushButton(Form)
        self.xMaxPushButton.setGeometry(QtCore.QRect(60, 180, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.xMaxPushButton.setFont(font)
        self.xMaxPushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10;\n"
"border: 1px solid black;")
        self.xMaxPushButton.setObjectName("xMaxPushButton")
        self.xIntervalPushButton = QtWidgets.QPushButton(Form)
        self.xIntervalPushButton.setGeometry(QtCore.QRect(340, 130, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.xIntervalPushButton.setFont(font)
        self.xIntervalPushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10;\n"
"border: 1px solid black;")
        self.xIntervalPushButton.setObjectName("xIntervalPushButton")
        self.yIntervalPushButton = QtWidgets.QPushButton(Form)
        self.yIntervalPushButton.setGeometry(QtCore.QRect(340, 180, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.yIntervalPushButton.setFont(font)
        self.yIntervalPushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10;\n"
"border: 1px solid black;")
        self.yIntervalPushButton.setObjectName("yIntervalPushButton")
        self.xLabelPushButton = QtWidgets.QPushButton(Form)
        self.xLabelPushButton.setGeometry(QtCore.QRect(340, 230, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.xLabelPushButton.setFont(font)
        self.xLabelPushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10;\n"
"border: 1px solid black;")
        self.xLabelPushButton.setObjectName("xLabelPushButton")
        self.dosyaAdi = QtWidgets.QPushButton(Form)
        self.dosyaAdi.setGeometry(QtCore.QRect(120, 380, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.dosyaAdi.setFont(font)
        self.dosyaAdi.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10;\n"
"border: 1px solid black;")
        self.dosyaAdi.setObjectName("dosyaAdi")
        self.title = QtWidgets.QLineEdit(Form)
        self.title.setGeometry(QtCore.QRect(440, 500, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.title.setFont(font)
        self.title.setAutoFillBackground(False)
        self.title.setStyleSheet("border-radius:10;\n"
"background-color: rgb(0, 0, 255);")
        self.title.setObjectName("title")
        self.YminLineEdit = QtWidgets.QLineEdit(Form)
        self.YminLineEdit.setGeometry(QtCore.QRect(200, 230, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.YminLineEdit.setFont(font)
        self.YminLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10;\n"
"border: 1px solid black;")
        self.YminLineEdit.setObjectName("YminLineEdit")
        self.yMaxPushButton = QtWidgets.QPushButton(Form)
        self.yMaxPushButton.setGeometry(QtCore.QRect(60, 280, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.yMaxPushButton.setFont(font)
        self.yMaxPushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10;\n"
"border: 1px solid black;")
        self.yMaxPushButton.setObjectName("yMaxPushButton")
        self.YmaxLineEdit = QtWidgets.QLineEdit(Form)
        self.YmaxLineEdit.setGeometry(QtCore.QRect(200, 280, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.YmaxLineEdit.setFont(font)
        self.YmaxLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10;\n"
"border: 1px solid black;")
        self.YmaxLineEdit.setObjectName("YmaxLineEdit")
        self.yminPushButton = QtWidgets.QPushButton(Form)
        self.yminPushButton.setGeometry(QtCore.QRect(60, 230, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.yminPushButton.setFont(font)
        self.yminPushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10;\n"
"border: 1px solid black;")
        self.yminPushButton.setObjectName("yminPushButton")
        self.XintervalLineEdit = QtWidgets.QLineEdit(Form)
        self.XintervalLineEdit.setGeometry(QtCore.QRect(480, 130, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.XintervalLineEdit.setFont(font)
        self.XintervalLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10;\n"
"border: 1px solid black;")
        self.XintervalLineEdit.setObjectName("XintervalLineEdit")
        self.YintervalLineEdit = QtWidgets.QLineEdit(Form)
        self.YintervalLineEdit.setGeometry(QtCore.QRect(480, 180, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.YintervalLineEdit.setFont(font)
        self.YintervalLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10;\n"
"border: 1px solid black;")
        self.YintervalLineEdit.setObjectName("YintervalLineEdit")
        self.xLabelLineEdit = QtWidgets.QLineEdit(Form)
        self.xLabelLineEdit.setGeometry(QtCore.QRect(480, 230, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.xLabelLineEdit.setFont(font)
        self.xLabelLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10;\n"
"border: 1px solid black;")
        self.xLabelLineEdit.setObjectName("xLabelLineEdit")
        self.yLabelPushButton = QtWidgets.QPushButton(Form)
        self.yLabelPushButton.setGeometry(QtCore.QRect(340, 280, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.yLabelPushButton.setFont(font)
        self.yLabelPushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10;\n"
"border: 1px solid black;")
        self.yLabelPushButton.setObjectName("yLabelPushButton")
        self.yLabelLineEdit = QtWidgets.QLineEdit(Form)
        self.yLabelLineEdit.setGeometry(QtCore.QRect(480, 280, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.yLabelLineEdit.setFont(font)
        self.yLabelLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10;\n"
"border: 1px solid black;")
        self.yLabelLineEdit.setObjectName("yLabelLineEdit")
        self.legendLocationButton = QtWidgets.QPushButton(Form)
        self.legendLocationButton.setGeometry(QtCore.QRect(120, 330, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.legendLocationButton.setFont(font)
        self.legendLocationButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10;\n"
"border: 1px solid black;")
        self.legendLocationButton.setObjectName("legendLocationButton")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(340, 330, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10;\n"
"border: 1px solid black;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.calculateButton = QtWidgets.QPushButton(Form)
        self.calculateButton.setGeometry(QtCore.QRect(260, 80, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.calculateButton.setFont(font)
        self.calculateButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calculateButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10;\n"
"border: 1px solid black;")
        self.calculateButton.setObjectName("calculateButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.browserLineEdit, self.xminLineEdit)
        Form.setTabOrder(self.xminLineEdit, self.xmaxLineEdit)
        Form.setTabOrder(self.xmaxLineEdit, self.YminLineEdit)
        Form.setTabOrder(self.YminLineEdit, self.YmaxLineEdit)
        Form.setTabOrder(self.YmaxLineEdit, self.XintervalLineEdit)
        Form.setTabOrder(self.XintervalLineEdit, self.YintervalLineEdit)
        Form.setTabOrder(self.YintervalLineEdit, self.xLabelLineEdit)
        Form.setTabOrder(self.xLabelLineEdit, self.yLabelLineEdit)
        Form.setTabOrder(self.yLabelLineEdit, self.comboBox)
        Form.setTabOrder(self.comboBox, self.xLineInterval)
        Form.setTabOrder(self.xLineInterval, self.xMinPushButton)
        Form.setTabOrder(self.xMinPushButton, self.xMaxPushButton)
        Form.setTabOrder(self.xMaxPushButton, self.yminPushButton)
        Form.setTabOrder(self.yminPushButton, self.browserPushButton)
        Form.setTabOrder(self.browserPushButton, self.xIntervalPushButton)
        Form.setTabOrder(self.xIntervalPushButton, self.plotPushButton)
        Form.setTabOrder(self.plotPushButton, self.yLabelPushButton)
        Form.setTabOrder(self.yLabelPushButton, self.xLabelPushButton)
        Form.setTabOrder(self.xLabelPushButton, self.legendLocationButton)
        Form.setTabOrder(self.legendLocationButton, self.dosyaAdi)
        Form.setTabOrder(self.dosyaAdi, self.title)
        Form.setTabOrder(self.title, self.yMaxPushButton)
        Form.setTabOrder(self.yMaxPushButton, self.calculateButton)
        Form.setTabOrder(self.calculateButton, self.yIntervalPushButton)
        
        self.browserPushButton.clicked.connect(self.browseFolder)
        self.calculateButton.clicked.connect(self.calculation)
        self.plotPushButton.clicked.connect(self.plot)
        self.comboBox.activated.connect(self.legendLocation)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MEOS Isıl Tasarım Ekibi Plotv02"))
        self.xMinPushButton.setText(_translate("Form", "Xmin"))
        self.browserPushButton.setText(_translate("Form", "Browse..."))
        self.plotPushButton.setText(_translate("Form", "Plot+Save"))
        self.xMaxPushButton.setText(_translate("Form", "Xmax"))
        self.xIntervalPushButton.setText(_translate("Form", "Xinterval"))
        self.yIntervalPushButton.setText(_translate("Form", "Yinterval"))
        self.xLabelPushButton.setText(_translate("Form", "X"))
        self.dosyaAdi.setText(_translate("Form", "Document Name"))
        self.title.setText(_translate("Form", "   MEOS ISIL TASARIM EKİBİ"))
        self.yMaxPushButton.setText(_translate("Form", "Ymax"))
        self.yminPushButton.setText(_translate("Form", "Ymin"))
        self.yLabelPushButton.setText(_translate("Form", "Y"))
        self.legendLocationButton.setText(_translate("Form", "Legend Location"))
        self.comboBox.setItemText(0, _translate("Form", " "))
        self.comboBox.setItemText(1, _translate("Form", "best"))
        self.comboBox.setItemText(2, _translate("Form", "upper right"))
        self.comboBox.setItemText(3, _translate("Form", "upper left"))
        self.comboBox.setItemText(4, _translate("Form", "lower left"))
        self.comboBox.setItemText(5, _translate("Form", "lower right"))
        self.comboBox.setItemText(6, _translate("Form", "right"))
        self.comboBox.setItemText(7, _translate("Form", "center left"))
        self.comboBox.setItemText(8, _translate("Form", "center right"))
        self.comboBox.setItemText(9, _translate("Form", "lower center"))
        self.comboBox.setItemText(10, _translate("Form", "upper center"))
        self.comboBox.setItemText(11, _translate("Form", "center"))
        self.calculateButton.setText(_translate("Form", "Calculate"))

    def browseFolder(self):
        self.text, self.placeholder        = QFileDialog.getOpenFileName(None, 'Select file')
        fileName                           = self.browserLineEdit.setText(self.text)
    
    
    def calculation(self):
        try:
            data                           = pandas.read_excel("{}".format(self.text))
            
            headerList                     = data.columns.tolist()
            dataxAxisMax                   = data["{}".format(headerList[0])].max()
            dataxAxisMin                   = data["{}".format(headerList[0])].min()
            
            dataYAxisMaxList               = []
            dataYaxisMinList               = []
            
            i=1
            while i<len(headerList):
                dataYAxisMaxList.append(data["{}".format(headerList[i])].max())
                dataYaxisMinList.append(data["{}".format(headerList[i])].min())
                i+=1
            
            dataYAxisMax                  = max(dataYAxisMaxList)
            dataYaxisMin                  = min(dataYaxisMinList)
            
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle('Message Box')
            msg_box.setText(' X Min : {} \n X Max : {} \n Y Min : {} \n Y Max : {}'.format(dataxAxisMin,dataxAxisMax,dataYaxisMin,dataYAxisMax))
            msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            result = msg_box.exec_()
            
        except:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setWindowTitle('Error Box')
            msg_box.setText('There are errors in the inputs. Please check them.')
            msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            result = msg_box.exec_()
    
    def legendLocation(self,index):
        self.selectedLegendComboBox           = self.comboBox.itemText(index)
        
        
        
    def plot(self):
        
        try:
            self.xMinimum                      = float((self.xminLineEdit.text()))
            self.xMaximum                      = float((self.xmaxLineEdit.text()))
            self.yMinimum                      = float((self.YminLineEdit.text()))
            self.yMaximum                      = float((self.YmaxLineEdit.text()))
            self.xInterval                     = float((self.XintervalLineEdit.text()))
            self.yInterval                     = float((self.YintervalLineEdit.text()))
            self.xAxis                         = self.xLabelLineEdit.text()
            self.yAxis                         = self.yLabelLineEdit.text()
            self.documentName                  = self.xLineInterval.text()
            
            data                               = pandas.read_excel("{}.".format(self.text))
            xDataInterval                      = numpy.linspace(self.xMinimum, self.xMaximum, int(self.xInterval))
            yDataInterval                      = numpy.linspace(self.yMinimum, self.yMaximum, int(self.yInterval))
            
            headerList                         = data.columns.tolist()
            headerListSecond                   = headerList[1:]
            
            
        
            ax = data.plot(headerList[0],headerListSecond)
            plt.grid(True, color='gray', linestyle='--', linewidth=0.5)
            plt.xticks(xDataInterval)
            plt.yticks(yDataInterval)
            plt.xlim(self.xMinimum, self.xMaximum)    
            plt.ylim(self.yMinimum, self.yMaximum)   
            plt.xlabel(self.xAxis,fontweight="bold")
            plt.ylabel(self.yAxis,fontweight="bold")
            plt.legend(loc='{}'.format(self.selectedLegendComboBox))
            plt.savefig("{}.png".format(self.documentName),dpi=1000)
            plt.show()
        
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle('Message Box')
            msg_box.setText("The image has been saved.")
            msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            result = msg_box.exec_()
        
        except:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setWindowTitle('Error Box')
            msg_box.setText('There are errors in the inputs. Please check them.')
            msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            result = msg_box.exec_()
            
            
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
