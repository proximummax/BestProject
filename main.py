from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice
from PyQt5.QtWidgets import QMessageBox

BAUD_RATE = 9600

class Ui_portSelection(object):
           
    def setupUi(self, portSelection):
        # window drawing
        portSelection.setObjectName("portSelection")
        portSelection.resize(311, 149)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(portSelection.sizePolicy().hasHeightForWidth())
        portSelection.setSizePolicy(sizePolicy)
        portSelection.setMinimumSize(QtCore.QSize(311, 149))
        portSelection.setMaximumSize(QtCore.QSize(311, 149))
        self.horizontalLayoutWidget = QtWidgets.QWidget(portSelection)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 50, 261, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox_ports = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_ports.setObjectName("comboBox_ports")
        self.horizontalLayout.addWidget(self.comboBox_ports)
        self.pushButton_ok = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_ok.sizePolicy().hasHeightForWidth())
        self.pushButton_ok.setSizePolicy(sizePolicy)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.horizontalLayout.addWidget(self.pushButton_ok)
        self.label = QtWidgets.QLabel(portSelection)
        self.label.setGeometry(QtCore.QRect(20, 20, 281, 16))
        self.label.setObjectName("label")

        self.__retranslateUi(portSelection)
        QtCore.QMetaObject.connectSlotsByName(portSelection)

        self.comboBox_ports.addItems(self.__search_serial_ports()) # filling comboBox of ports
        self.pushButton_ok.clicked.connect(lambda: self.__open_main_window(portSelection))
        

    def __retranslateUi(self, portSelection):
        _translate = QtCore.QCoreApplication.translate
        portSelection.setWindowTitle(_translate("portSelection", "Выбор COM-порта"))
        self.pushButton_ok.setText(_translate("portSelection", "OK"))
        self.label.setText(_translate("portSelection", "Выберете COM-порт для связи с микроконтроллером"))

    def __search_serial_ports(self): # method of searching for list of available serial ports
        portlist = []
        for port in QSerialPortInfo().availablePorts():
            portlist.append(port.portName())
        return portlist
    
    def __open_main_window(self, portSelection):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow, self.comboBox_ports.currentText()) # opening the main window and specifying the selected port 
        self.MainWindow.show()
        portSelection.close()

class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow, currentSerialPort):
        # window drawing
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(380, 150)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(380, 150))
        MainWindow.setMaximumSize(QtCore.QSize(380, 150))
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
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(130, 40, 201, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_currentSerialPort = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_currentSerialPort.setObjectName("label_currentSerialPort")
        self.verticalLayout_2.addWidget(self.label_currentSerialPort)
        self.pushButton_changeSerialPort = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_changeSerialPort.setObjectName("pushButton_changeSerialPort")
        self.verticalLayout_2.addWidget(self.pushButton_changeSerialPort)
        self.pushButton_programInfo = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_programInfo.sizePolicy().hasHeightForWidth())
        self.pushButton_programInfo.setSizePolicy(sizePolicy)
        self.pushButton_programInfo.setObjectName("pushButton_programInfo")
        self.verticalLayout_2.addWidget(self.pushButton_programInfo)
        MainWindow.setCentralWidget(self.centralwidget)

        self.__retranslateUi(MainWindow, currentSerialPort)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # инициализация COM-porta, установка скорости передачи
        self.serial = QSerialPort()
        self.serial.setBaudRate(BAUD_RATE)
        self.serial.readyRead().connect(lambda: self.get_info_from_mc)
        
        self.__check_ports_states() # port state check method

        # user interface signals
        self.checkBox_port_1.stateChanged.connect(lambda: self.__change_port_state(1, self.checkBox_port_1.isChecked()))
        self.checkBox_port_2.stateChanged.connect(lambda: self.__change_port_state(2, self.checkBox_port_2.isChecked()))
        self.checkBox_port_3.stateChanged.connect(lambda: self.__change_port_state(3, self.checkBox_port_3.isChecked()))
        self.checkBox_port_4.stateChanged.connect(lambda: self.__change_port_state(4, self.checkBox_port_4.isChecked()))
        self.pushButton_programInfo.clicked.connect(self.__show_program_info)
        self.pushButton_changeSerialPort.clicked.connect(lambda: self.__open_portSelection_window(MainWindow))

    def __retranslateUi(self, MainWindow, currentSerialPort):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Система управления питанием СЗИ"))
        self.checkBox_port_1.setText(_translate("MainWindow", "Порт №1"))
        self.checkBox_port_2.setText(_translate("MainWindow", "Порт №2"))
        self.checkBox_port_3.setText(_translate("MainWindow", "Порт №3"))
        self.checkBox_port_4.setText(_translate("MainWindow", "Порт №4"))
        self.label_currentSerialPort.setText(_translate("MainWindow", "Текущий COM-порт: ")+currentSerialPort)
        self.pushButton_changeSerialPort.setText(_translate("MainWindow", "Изменить COM-порт"))
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

    def __open_portSelection_window(self, mainWindow):
        self.portSelection = QtWidgets.QMainWindow()
        self.ui = Ui_portSelection()
        self.ui.setupUi(self.portSelection)
        self.portSelection.show()
        mainWindow.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    startWindow = QtWidgets.QWidget()
    ui = Ui_portSelection()
    ui.setupUi(startWindow)
    startWindow.show()
    sys.exit(app.exec_())
