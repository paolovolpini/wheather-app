import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMainWindow
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather App")
                     
        # city label setup
        self.city_label = QLabel("Enter a city name: ")  
        self.city_input = QLineEdit(self)
        
        # get weather button
        self.get_weather = QPushButton("Get Weather Info", self)
        self.temperature_label = QLabel("30°C", self)
    
        # icon and description
        self.emoji_label = QLabel("☼", self)
        self.description = QLabel("Sunny", self)

        self.setUI()
    def setUI(self):   

        # create vertical box layout
        vbox = QVBoxLayout()
        
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.description)
        vbox.addWidget(self.emoji_label)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description.setAlignment(Qt.AlignCenter)
        self.setLayout(vbox)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.temperature_label.setObjectName("temperature_label")
        self.get_weather.setObjectName("get_weather")
        self.emoji_label.setObjectName("emoji_label")
        self.description.setObjectName("description")

        self.setStyleSheet(""" 
            QLabel#city_label {
                    font-size: 40px;
                    font-family: arial;
                }
            QLineEdit#city_input {
                    font-size: 16px;
                    font-style: italic;
                }
            QPushButton#get_weather {
                    font-weight: bold;
                }
            QLabel#temperature_label {
                    font-size: 60px;
                }
            QLabel#emoji_label {
                    font-size: 80px;
                    font-style: Segoe UI emoji;
                }
            QLabel#description {
                    font-size: 50px;
                }

        """)
        self.get_weather.clicked.connect(self.get_weather_info)
        
    def get_weather_info(self):
        print("Weather gathered!")
    
    def display_weather(self, data):
        pass

if __name__ == "__main__":
    app = QApplication([])
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())       # sys.exit() sends the exit code returned from app.exec_()

