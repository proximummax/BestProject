from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice
from PyQt5.QtWidgets import QMessageBox
from enum import Enum

BAUD_RATE = 9600



class ExpectedSignalType(Enum):
    NO_WAITING = 1
    WAITING_PINS_INFO = 2
    WAITING_COMMAND_RESULT = 3

class PinState(Enum):
    OFF = 0
    ON = 1

COMMANDS = {(PinState.ON, 1) : "comm1\n", # словарь команд: (состояние пина, номер пина) -> команда
            (PinState.ON, 2) : "comm2\n",
            (PinState.ON, 3) : "comm3\n",
            (PinState.OFF, 1) : "comm4\n",
            (PinState.OFF, 2) : "comm5\n",
            (PinState.OFF, 3) : "comm6\n",
            }

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
        self.comboBox_pins = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_pins.setObjectName("comboBox_pins")
        self.horizontalLayout.addWidget(self.comboBox_pins)
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

        self.comboBox_pins.addItems(self.__search_serial_ports()) # filling comboBox of ports
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
        if (self.comboBox_pins.currentText() == ""): # проверка: есть ли COM-порт
            creators_info = QMessageBox()
            creators_info.setWindowTitle("Ошибка!")
            creators_info.setText("Отсутствуют COM-порты.")
            creators_info.exec_()
            self.__search_serial_ports() # повторный запуск функии определения COM-портов
            return
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow, self.comboBox_pins.currentText()) # opening the main window and specifying the selected port 
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
        self.checkBox_pin_1 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_pin_1.setObjectName("checkBox_pin_1")
        self.verticalLayout.addWidget(self.checkBox_pin_1)
        self.checkBox_pin_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_pin_2.setObjectName("checkBox_pin_2")
        self.verticalLayout.addWidget(self.checkBox_pin_2)
        self.checkBox_pin_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_pin_3.setObjectName("checkBox_pin_3")
        self.verticalLayout.addWidget(self.checkBox_pin_3)
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

        # инициализация COM-porta, установка скорости передачи, открытие порта
        self.serial = QSerialPort()
        self.serial.setBaudRate(BAUD_RATE)
        self.serial.setPortName(currentSerialPort)
        self.serial.open(QIODevice.ReadWrite)

        self.serial.readyRead.connect(lambda: self.__get_info_from_mc()) # надо ли оно??
       
        self.type_of_expected_mc_signal = ExpectedSignalType.NO_WAITING # тип ожидаемого сигнала от МК - остутствие сигнала
        self.__check_pins_states() # запрос состояний пинов

        # user interface signals
        self.checkBox_pin_1.clicked.connect(lambda: self.__change_pin_state(1, PinState((self.checkBox_pin_1.isChecked() + 1) // 2)))
        self.checkBox_pin_2.clicked.connect(lambda: self.__change_pin_state(2, PinState((self.checkBox_pin_2.isChecked() + 1) // 2)))
        self.checkBox_pin_3.clicked.connect(lambda: self.__change_pin_state(3, PinState((self.checkBox_pin_3.isChecked() + 1) // 2)))
        self.pushButton_programInfo.clicked.connect(self.__show_program_info)
        self.pushButton_changeSerialPort.clicked.connect(lambda: self.__open_portSelection_window(MainWindow))


    def __retranslateUi(self, MainWindow, currentSerialPort):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Система управления питанием СЗИ"))
        self.checkBox_pin_1.setText(_translate("MainWindow", "Пин №1"))
        self.checkBox_pin_2.setText(_translate("MainWindow", "Пин №2"))
        self.checkBox_pin_3.setText(_translate("MainWindow", "Пин №3"))
        self.label_currentSerialPort.setText(_translate("MainWindow", "Текущий COM-порт: ")+currentSerialPort)
        self.pushButton_changeSerialPort.setText(_translate("MainWindow", "Изменить COM-порт"))
        self.pushButton_programInfo.setText(_translate("MainWindow", "О программе"))


    def __get_info_from_mc(self):
        inputData = str(self.serial.readLine(), 'utf-8').strip()
        #print(inputData) # Для отладки 
        if (self.type_of_expected_mc_signal == ExpectedSignalType.NO_WAITING):
            print("Несканционированная передача данных с микроконтроллера.") 
            # MessageBox?
            #
            #
        elif (self.type_of_expected_mc_signal == ExpectedSignalType.WAITING_PINS_INFO):
            print("Получение инфы от МК...") 
            # здесь должен быть парсер
            #
            #
            return [0, 2, 0]
        elif (self.type_of_expected_mc_signal == ExpectedSignalType.WAITING_COMMAND_RESULT):
            self.type_of_expected_mc_signal = ExpectedSignalType.NO_WAITING
            if (inputData == "Command is correct"): return True
            else: return False


    def __check_pins_states(self):
        self.type_of_expected_mc_signal = ExpectedSignalType.WAITING_PINS_INFO
        # здесь должна быть команда запроса (?)
        #
        #

        states_of_pins = self.__get_info_from_mc()
        self.checkBox_pin_1.setCheckState(states_of_pins[0])
        self.checkBox_pin_2.setCheckState(states_of_pins[1])
        self.checkBox_pin_3.setCheckState(states_of_pins[2])
    

    def __change_pin_state(self, pinNumber, newPinState):
        command = COMMANDS.get(tuple([newPinState, pinNumber])).encode('utf-8')
        #print(command) # временно для отладки
        self.type_of_expected_mc_signal = ExpectedSignalType.WAITING_COMMAND_RESULT
        self.serial.write(command)
        self.serial.waitForBytesWritten()
        if (not self.__get_info_from_mc()): # обратное изменение состояния в случае ошибки
            print("Произошла ошибка") # временно для отладки (или message Box)
            if (pinNumber == 1):
                self.checkBox_pin_1.setCheckState((newPinState.value + 2) % 3)
            elif (pinNumber == 2):
                self.checkBox_pin_2.setCheckState((newPinState.value + 2) % 3)
            elif (pinNumber == 3):
                self.checkBox_pin_3.setCheckState((newPinState.value + 2) % 3)


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
        self.serial.close() #закрытие COM-порта
        mainWindow.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    startWindow = QtWidgets.QWidget()
    ui = Ui_portSelection()
    ui.setupUi(startWindow)
    startWindow.show()
    sys.exit(app.exec_())
