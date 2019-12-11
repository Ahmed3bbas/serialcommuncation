import sys

from PyQt5 import QtCore, QtGui,QtWidgets

from port import Ui_MainWindow

from PyQt5.QtWidgets import QMessageBox

import serial

import glob



def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


class Main(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        #click event
        self.send_btn.clicked.connect(self.send)
        #click event
        self.text_box.returnPressed.connect(self.send)
        #click event
        self.connect_btn.clicked.connect(self.connect)
        #click event
        self.disconnect_btn.clicked.connect(self.disconnect)
        #click event
        self.refersh_btn.clicked.connect(self.refresh)
        # get ports name & set in  combobox
        self.ports_box.addItems(serial_ports())
        self.ser = serial.Serial();
        self.port_name = ''



    def refresh(self):
        print("refresh clicked")
        # print(serial_ports())
        self.ports_box.clear()
        self.ports_box.addItems(serial_ports())

    def connect(self):
        print("connect clicked")
        self.port_name = self.ports_box.currentText()
        if len(self.port_name) != 0:
            self.ser = serial.Serial()
            self.ser.baudrate = 9600
            self.ser.port = self.port_name
            self.ser.bytesize = 8
            self.stopbits = 1
            if not self.ser.is_open:
                try:
                    self.ser.open()
                    self.state.setText("Connected")
                    self.state.setStyleSheet("QLabel { color : green; }");
                except:
                    QMessageBox.about(self, "WARNING", "Can't open port")


    def disconnect(self):
        print("disconnect clicked")
        if self.ser.is_open:
            try:
                self.ser.close()
                self.state.setText("Disconnected")
                self.state.setStyleSheet("QLabel { color : red; }");
            except:
                QMessageBox.about(self, "WARNING", "Can't close port")

    def send(self):
        print("send clicked")
        command = self.text_box.text()
        try:
            if(self.ser.is_open):
            	print("command : ", command)
            	self.ser.write(command.encode('utf-8'))
            else:
                QMessageBox.about(self, "WARNING", "Can't write to port (connect on port)")

        except Exception as e:
        	print(e)
        	QMessageBox.about(self, "WARNING", "Can't write to port, Exception Occured")
    
    def closeEvent(self, event):
        self.disconnect()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
