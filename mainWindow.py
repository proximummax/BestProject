from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice

class Ui_MainWindow(object):
    serial = QSerialPort()
    serial.setBaudRate(115200)

    def search_serial_port(self):
        portlist = []
        ports = QSerialPortInfo().availablePorts()
        for port in ports:
            portlist.append(port.portName())
        return portlist


    def setupUi(self, MainWindow):
        self.search_serial_port()

        # window drawing
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(350, 150)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(350, 150))
        MainWindow.setMaximumSize(QtCore.QSize(350, 150))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 91, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_port_1 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_port_1.setObjectName("checkBox_port_1")
        self.verticalLayout.addWidget(self.checkBox_port_1)
        self.checkBox_port_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_port_2.setObjectName("checkBox_port_2")
        self.verticalLayout.addWidget(self.checkBox_port_2)
        self.checkBox_port_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_port_3.setObjectName("checkBox_port_3")
        self.verticalLayout.addWidget(self.checkBox_port_3)
        self.checkBox_port_4 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_port_4.setObjectName("checkBox_port_4")
        self.verticalLayout.addWidget(self.checkBox_port_4)
        self.pushButton_programInfo = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_programInfo.setGeometry(QtCore.QRect(180, 40, 91, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_programInfo.sizePolicy().hasHeightForWidth())
        self.pushButton_programInfo.setSizePolicy(sizePolicy)
        self.pushButton_programInfo.setObjectName("pushButton_programInfo")
        MainWindow.setCentralWidget(self.centralwidget)

        self.__retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.__check_ports_states() # port state check method

        # user interface signals
        self.checkBox_port_1.stateChanged.connect(lambda: self.__change_port_state(1, self.checkBox_port_1.isChecked()))
        self.checkBox_port_2.stateChanged.connect(lambda: self.__change_port_state(2, self.checkBox_port_2.isChecked()))
        self.checkBox_port_3.stateChanged.connect(lambda: self.__change_port_state(3, self.checkBox_port_3.isChecked()))
        self.checkBox_port_4.stateChanged.connect(lambda: self.__change_port_state(4, self.checkBox_port_4.isChecked()))
        self.pushButton_programInfo.clicked.connect(self.__show_program_info)

    def __retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Система управления питанием"))
        self.checkBox_port_1.setText(_translate("MainWindow", "Порт №1"))
        self.checkBox_port_2.setText(_translate("MainWindow", "Порт №2"))
        self.checkBox_port_3.setText(_translate("MainWindow", "Порт №3"))
        self.checkBox_port_4.setText(_translate("MainWindow", "Порт №4"))
        self.pushButton_programInfo.setText(_translate("MainWindow", "О программе"))

    def __check_ports_states(self):
        self.checkBox_port_1.setCheckState(self.__check_port_state(1))
        self.checkBox_port_2.setCheckState(self.__check_port_state(2))
        self.checkBox_port_3.setCheckState(self.__check_port_state(3))
        self.checkBox_port_4.setCheckState(self.__check_port_state(4))

    def __check_port_state(self, portNumber):
        if (portNumber%2): return 2
        else: return 0 #0/2 results
    
    def __change_port_state(self, portNumber, newPortState):
        print("Номер порта: ", str(portNumber), " - ", str(newPortState))

    def __show_program_info(self):
        creators_info = QMessageBox()
        creators_info.setWindowTitle("О программе")
        creators_info.setText("Создатели:\nCтуденты группы АБ-920\nПольщиков Г.А., Попова Ю.А., Посуконько О.А., Репин С.Е.")
        creators_info.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
