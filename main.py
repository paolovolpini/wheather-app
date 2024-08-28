import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather App")
                     
        # city label setup
        self.city_label = QLabel("Enter a city name: ")  
        self.city_input = QLineEdit(self)
        
        # get weather button
        self.get_weather = QPushButton("Get Weather Info", self)
        self.temperature_label = QLabel(self)
         
        # icon, description and humidity
        self.emoji_label = QLabel(self)
        self.emoji_pixmap = QPixmap()
        self.description = QLabel(self)
        self.humidity = QLabel(self)
        self.setUI()

    def setUI(self):   
        # create vertical box layout
        vbox = QVBoxLayout()
    
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.humidity)
        vbox.addWidget(self.description)
        vbox.addWidget(self.emoji_label)
        
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.humidity.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description.setAlignment(Qt.AlignCenter)
        self.setLayout(vbox)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.temperature_label.setObjectName("temperature_label")
        self.humidity.setObjectName("humidity")
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
            QLabel#humidity {
                    font-size: 40px;
                    font-weight: bold;
                }
            QLabel#emoji_label {
                    font-size: 100px;
                }
            QLabel#description {
                    font-size: 50px;
                }

        """)
        self.get_weather.clicked.connect(self.get_weather_info)
        
    def clearUI(self): 
        self.temperature_label.setText("")
        self.emoji_label.setPixmap(QPixmap())
        self.description.setText("")
        self.humidity.setText("")

    def get_weather_info(self): 
        api_key = sys.argv[1]
        city_name = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
        response = requests.get(url)
        if(response.status_code != 200):
            print("Error", response.status_code, "while gathering info")
            self.clearUI()
            
        else:
            weather_data = response.json()
            self.display_weather(weather_data)            
        
    
    def display_weather(self, weather_data):
        self.temperature_label.setText(str(round(weather_data["main"]["temp"] - 273.15)) + "°C")
        self.description.setText(weather_data["weather"][0]["main"])
        self.humidity.setText("Humidity: "+ str(weather_data["main"]["humidity"]) + "%")
        code = weather_data["weather"][0]["icon"] 
        self.getEmojiFromCode(code)
        print(weather_data)

    def getEmojiFromCode(self, code):
        icon_url = f"https://openweathermap.org/img/wn/{code}@2x.png"
        icon_request = requests.get(icon_url)
        self.emoji_pixmap.loadFromData(icon_request.content)
        self.emoji_label.setPixmap(self.emoji_pixmap)


if __name__ == "__main__":
    if(len(sys.argv) == 1):
        print("No API key was served! Exiting...")
        sys.exit()
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())       # sys.exit() sends the exit code returned from app.exec_()

