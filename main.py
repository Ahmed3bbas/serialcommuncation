import sys

from PyQt5 import QtCore, QtGui,QtWidgets

from port import Ui_MainWindow

from PyQt5.QtWidgets import QMessageBox

import serial

import glob

import matplotlib.pyplot as plt

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
    def __init__(self, command_length = 7):
        
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        #command length and start
        self.command_length = command_length
        self.amp_start = 1
        self.amp_len = 1
        self.time_start =  self.amp_start + self.amp_len 
        self.time_len = 4
        self.time_end = self.time_start + self.time_len

        #to save reading values
        self.values = {'amp':[],'time':[]}
        
        #send button event
        self.send_btn.clicked.connect(self.send)
        
        #send form box event
        self.text_box.returnPressed.connect(self.send)
        
        #connect button event
        self.connect_btn.clicked.connect(self.connect)
        
        #disconnect button event
        self.disconnect_btn.clicked.connect(self.disconnect)
        
        #refresh button event
        self.refersh_btn.clicked.connect(self.refresh)
        
        # get ports name & set in  combobox
        self.ports_box.addItems(serial_ports())
        self.ser = serial.Serial();
        self.port_name = ''

        #read button click event
        self.read_btn.clicked.connect(self.read)




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
    

    def read(self):
    	print("read clicked")
    	if(self.ser.is_open):
    		while self.ser.inWaiting() > 0:
    			try:
	    			s = self.ser.read(self.command_length)
	    			starter = chr(s[0])
	    			print('start : ', starter)


	    			#Amplitude
	    			amp = int(s[self.amp_start : self.amp_len + 1].hex(),16)
	    			print('amp : ', amp)
	    			self.values['amp'].append(amp)

	    			#Time
	    			time = int(s[self.time_start : self.time_end].hex(),16)
	    			print('time : ', time)
	    			self.values['time'].append(time)

	    			end = chr(s[-1])
	    			print('end : ',end)

	    			self.read_box.setText('start : ' + str(starter) +' amplitude : ' + str(amp) + ' time : ' + str(time) + ' end ' + str(end))

	    		except:
	    			print('None')

	    	try:
	    		if(len(self.values['time']) != 0 or len(self.values['amp']) != 0):
		    		plt.plot(self.values['time'],self.values['amp'])
		    		plt.show()
		    		self.values['amp'] = []
		    		self.values['time'] = []
		    
		    	else:
		    		QMessageBox.about(self, "INFO", "There are not reading values to plot")
	    	
	    	except:
	    		QMessageBox.about(self, "WARNING", "Can't plotting")
    	
    	else:
    		QMessageBox.about(self, "WARNING", " connect on port firstly")

    def closeEvent(self, event):
        self.disconnect()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
