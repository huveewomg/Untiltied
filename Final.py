import sys
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QLabel
from PyQt5.QtGui import QIcon
from decimal import Decimal, DecimalException

class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'Green test'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.geth()
        self.getl()
        humidity_result, intensity_result = self.calculate_result()
        self.result_label = QLabel(self)
        self.result_label.setGeometry(QRect(100, 0, 500, 500))
        self.result_label.setText(f"{humidity_result}\n{intensity_result}")
        self.show()
 
 
    def geth(self): 
        self.h, okPressed = QInputDialog.getInt(self, "Humidity","Value:", 0, 0, 60, 50)
 
 
 
    def getl(self):
        self.l, okPressed = QInputDialog.getInt(self, "Light Intensity","Value:", 0, 0, 190000, 10)
    
    def calculate_result(self):
        minHumidity  = Decimal(50) 
        minIntensity = Decimal(10000)  
        maxHumidity = Decimal(60) #Humidity in air r/h
        maxIntensity = Decimal(19999) #light intensity 
        result = []

        if self.h < minHumidity:
            result.append('For Humidity: The humidity is too low try put somewhere with higher humidity!')
        elif self.h > maxHumidity:
            result.append('For Humidity: The humidity is too high try put somewhere with lower humidity!')    
        elif self.h >= minHumidity < maxHumidity:
            result.append('For Humidity: The humidity is suitable!') 
                    
        if self.l < minIntensity:
            result.append('For Light Intensity: The sunlight is weak try somewhere brighter!')
        elif self.l > maxIntensity:
            result.append('For Light Intensity: The sunlight is too strong try put somewhere shader!')    
        elif self.l >= minIntensity <= maxIntensity:
            result.append('For Light Intensity: The sunlight is suitable!')
    
        return tuple(result)
 
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())